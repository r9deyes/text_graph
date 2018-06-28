#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, cPickle, StringIO, webbrowser
from Tkinter import *
# mal sehen, wie 
# from ttk import *
import tkMessageBox, tkFileDialog
from UIParts import ToolBar, StatusBar, MultiListBox, TabPage
import Korpus, LangOpt
try:
    from win32com.client import Dispatch
except:
    pass


######################
# Konfigurieren...

# SkriptDir = os.path.dirname(os.path.abspath(__file__))
# Dies scheint besser zu funktionieren:
SkriptDir = os.path.dirname(sys.argv[0])
ImgDir = os.path.join(SkriptDir, 'Images')
# cfgFile = os.path.join(SkriptDir, 'TextSTAT.ini')
cfgFile = os.path.join(os.path.expanduser("~"), '.textstat2.ini')

try:
    f = open(cfgFile)
    cfg = cPickle.load(f)
    f.close()
except:
    cfg = {}
    cfg['Benutzersprache'] = 'en'
    cfg['KorpDir'] = SkriptDir
    cfg['FileDir'] = SkriptDir
    cfg['freqMin'] = '0'
    cfg['freqMax'] = '0'
    cfg['konkContextL'] = '40'
    cfg['konkContextR'] = '40'
    cfg['zitContextL'] = '350'
    cfg['zitContextR'] = '350'
    cfg['FileKodierung'] = 'utf_8'
    cfg['fenster'] = '700x580+10+10'    # d.i.: Breite x Höhe + xOffset + yOffset


# Sprache
if cfg['Benutzersprache'] == 'en':
    s = LangOpt.english
elif cfg['Benutzersprache'] == 'ru':
    s = LangOpt.russian
elif cfg['Benutzersprache'] == 'nl':
    s = LangOpt.nederlands
elif cfg['Benutzersprache'] == 'pt':
    s = LangOpt.portuguese
elif cfg['Benutzersprache'] == 'es':
    s = LangOpt.espanol
elif cfg['Benutzersprache'] == 'fr':
    s = LangOpt.francais
elif cfg['Benutzersprache'] == 'gl':
    s = LangOpt.galician
elif cfg['Benutzersprache'] == 'fi':
    s = LangOpt.suomi
elif cfg['Benutzersprache'] == 'po':
    s = LangOpt.polski
elif cfg['Benutzersprache'] == 'cs':
    s = LangOpt.czech
elif cfg['Benutzersprache'] == 'it':
    s = LangOpt.italiano
elif cfg['Benutzersprache'] == 'ca':
    s = LangOpt.catalan
else:
    s = LangOpt.deutsch


###############
# GUI

root = Tk()
root.title(s['Titel_lang'])
root.geometry(cfg['fenster'])
root.minsize(650, 550)   # (Breite, Höhe)

root.option_add('*Text*background', 'white')
root.option_add('*Listbox*background', 'white')
if sys.platform == 'win32':
    ico = os.path.join(SkriptDir, 'Images/TextSTAT.ico')
    root.iconbitmap(bitmap=ico)
    root.option_add('*Font', 'Verdana 8')
    root.option_add('*Listbox*font', (('Courier', 'New'), '9'))
    root.option_add('*Text*font', 'Verdana 10')
elif sys.platform == "darwin":
#    root.option_add('*Font', 'Arial 9 bold')
    root.option_add('*Font', 'Sans 13')
#    root.option_add('*Listbox*font', (('DejaVu', 'Sans', 'Mono'), '10'))
    root.option_add('*Listbox*font', 'Menlo 14')
    root.option_add('*Text*font', 'Sans 13')
else:
#    root.option_add('*Font', 'Arial 9 bold')
    root.option_add('*Font', 'Sans 10')
#    root.option_add('*Listbox*font', (('DejaVu', 'Sans', 'Mono'), '10'))
    root.option_add('*Listbox*font', 'Monospace 10')
    root.option_add('*Text*font', 'Sans 11')


class GUI:
    def __init__(self, root):
        self.root = root
        self.korpus = None
        try:	
            self.LetzteKorpusFiles=[]
            self.LetzteKorpusFiles.append(cfg['LetzteKorpusFiles0'])
            self.LetzteKorpusFiles.append(cfg['LetzteKorpusFiles1'])
            self.LetzteKorpusFiles.append(cfg['LetzteKorpusFiles2'])
            self.LetzteKorpusFiles.append(cfg['LetzteKorpusFiles3'])
        except:
            pass

        # Wenn Fenster über Windows-Fenstermanager geschlossen wird...
        self.root.protocol( 'WM_DELETE_WINDOW', self.ende )
        
        self.fenster = Frame(self.root)
        self.fenster.pack(expand=YES, fill=BOTH )

        # Das Menu
        MeinMenu = Menu(self.root)
        self.root.config(menu=MeinMenu)

        self.filemenu = Menu(MeinMenu, tearoff=0)
        MeinMenu.add_cascade(label=s['Korpus'], underline=0, menu = self.filemenu)
        self.filemenu.add_command(label=s['KorpusNew'], underline=0, command = self.korpus_new)
        self.filemenu.add_command(label=s['KorpusOpen'], underline=0, command = self.korpus_open)
        self.filemenu.add_command(label=s['KorpusHinzu'], underline=1, command = self.korpus_hinzu)
        self.filemenu.add_command(label=s['KorpusSave'], underline=2, command = self.korpus_save)
        self.filemenu.add_command(label=s['KorpusSaveAs'], underline=3, command = self.korpus_save_as)
        self.filemenu.add_command(label=s['KorpusDel'], underline=4, command = self.korpus_del)

        self.recentfilesmenu = Menu(self.filemenu, tearoff=0)
        self.filemenu.add_cascade(label=s['LetzteKorpora'], underline=0, state=DISABLED, menu=self.recentfilesmenu)
        self.update_recentfiles_menu()
        
        self.filemenu.add_separator()
        self.filemenu.add_command(label=s['DateiHinzu'], underline=0, command = self.datei_hinzu)
        self.filemenu.add_command(label=s['WebHinzu'], underline=0, command = self.WebDialog)
        self.filemenu.add_command(label=s['NewsHinzu'], underline=0, command = self.NewsDialog)
        self.filemenu.add_separator()
        self.filemenu.add_command(label=s['DateiWeg'], underline=2, command = self.datei_entfernen)
        self.filemenu.add_separator()
        self.filemenu.add_command(label=s['OptSave'], underline=0, command = self.optionen_speichern)
        self.filemenu.add_command(label=s['Exit'], underline=1, command = self.ende)

        exportmenu = Menu(MeinMenu, tearoff=0)
        MeinMenu.add_cascade(label=s['ImpEx'], underline=0, menu = exportmenu)
        exportmenu.add_command(label=s['Ex2csv'], underline=0, command = self.export2csv)
        exportmenu.add_command(label=s['Ex2txt'], underline=0, command = self.export2txt)
        exportmenu.add_command(label='text graph -> csv', underline=0, command = self.export_text_graph2csv)
        if os.name == 'nt':
            exportmenu.add_separator()
            exportmenu.add_command(label='text graph -> Excel', underline=1, command = self.export_text_graph2excel)
            exportmenu.add_command(label=s['Ex2excel'], underline=1, command = self.export2excel)
            exportmenu.add_command(label=s['Ex2word'], underline=1, command = self.export2word)
        # exportmenu.add_separator()
        # exportmenu.add_command(label=s['ImpKorpus'], underline=7, command = self.korpus_import)

        sprachmenu = Menu(MeinMenu, tearoff=0)
        MeinMenu.add_cascade(label=s['Sprache'], underline=0, menu = sprachmenu)
        self.sprache_aendern = StringVar()
        self.sprache_aendern.set(cfg['Benutzersprache'])
        oberflaechensprachen = [
            ['Deutsch', 'de'],
            ['English', 'en'],
            ['Русский', 'ru'],
            ['Nederlands', 'nl'],
            ['Español', 'es'],
            ['Português', 'pt'],
            ['Français', 'fr'],
            ['Italiano', 'it'],
            ['Català', 'ca'],
            ['Galego', 'gl'],
            ['Suomi', 'fi'],
            ['Polski', 'po'],
            ['Čeština', 'cs'],
            ]
        for sprach_label, sprach_abkz in oberflaechensprachen:
            sprachmenu.add_radiobutton(label=sprach_label, underline=0, variable=self.sprache_aendern, value=sprach_abkz, command=self.sprachwarnung)
            
        codepagemenu = Menu(MeinMenu, tearoff=1)
        MeinMenu.add_cascade(label=s['CodePage'], underline=1, menu = codepagemenu)
        self.dateiart = StringVar()
        self.dateiart.set(cfg['FileKodierung'])
        # self.dateiart.set('iso8859-1')
        kodierungen = [
            ['UTF-8 (Unicode)', 'utf_8'],
            ['UTF-16 (Unicode)', 'utf_16'],
            ['ISO-8859-1 (Latin-1)', 'iso8859_1'],
            ['ISO-8859-2 (Latin-2)', 'iso8859_2'],
            ['ISO-8859-5 (Cyrillic)', 'iso8859_5'],
            ['ISO-8859-6 (Arabic)', 'iso8859_6'],
            ['ISO-8859-7 (Greek)', 'iso8859_7'],
            ['ISO-8859-8 (Hebrew)', 'iso8859_8'],
            ['ISO-8859-9 (Turkish)', 'iso8859_9'],
            ['CP1252 (ANSI, WinLatin-1)', 'cp1252'],
            ['CP1250 (WinLatin-2)', 'cp1250'],
            ['CP1251 (WinCyrillic)', 'cp1251'],
            ['CP1254 (WinTurkish)', 'cp1254'],
            ['CP1255 (WinHebrew)', 'cp1255'],
            ['CP1256 (WinArabic)', 'cp1256'],
            ['CP850 (MS DOS)', 'cp850'],
            ['KOI 8 R (Russian)', 'koi8_r'],
            ['GB 2312 (Simplified Chinese)', 'gb2312'],
            ['BIG 5 (Traditional Chinese)', 'big5'],
            ]
        for bezeichnung, kodierung in kodierungen:
            codepagemenu.add_radiobutton(label=bezeichnung, variable=self.dateiart, value=kodierung)  

        # Hilfe- / Info-Menu
        hilfemenu = Menu(MeinMenu, tearoff=0)
        MeinMenu.add_cascade(label=s['Hilfe'], underline=1, menu = hilfemenu)
        hilfemenu.add_command(label=s['RegExpHelp'], underline=0, command = self.regex_hilfe)
        hilfemenu.add_separator()
        hilfemenu.add_command(label=s['History'], underline=0, command = self.zeigHistory)
        hilfemenu.add_command(label=s['License'], underline=0, command = self.zeigLicense)
        hilfemenu.add_separator()
        hilfemenu.add_command(label=s['Info'], underline=0, command = self.about)

        # Die Statuszeile
        self.status = StatusBar.StatusBar(self.root, ProgressBar=1)
        self.status.pack(fill=X)
        self.status.set(s['Willkommen'])
        self.status.indicator(s['StatusNoKorp'])

        # Der Toolbar
        # Die Icons stammen von http://www.trash.net/~ffischer/admin/icons/
        #
        self.toolbar = ToolBar.ToolBar(self.fenster, statusbar = self.status)
        self.toolbar.pack(side=TOP, fill=X)
        self.toolbar.add('NeuButton', s['KorpusNew'], ImgDir+'/New.gif', self.korpus_new, s['KorpusNew2'])
        self.toolbar.add('KorpusOeffnenButton', s['KorpusOpen'], ImgDir+'/Open.gif', self.korpus_open, s['KorpusOpen2'])
        self.toolbar.add('KorpusHinzuButton', s['KorpusHinzu'], ImgDir+'/FolderIn.gif', self.korpus_hinzu, s['KorpusHinzu2'])
        self.toolbar.add('SaveButton', s['KorpusSave'], ImgDir+'/Save.gif', self.korpus_save, s['KorpusSave2'])
        self.toolbar.add('WegButton', s['KorpusDel'], ImgDir+'/Delete.gif', self.korpus_del, s['KorpusDel2'])
        self.toolbar.add_separator()
        self.toolbar.add('HTMLhinzuButton', s['WebHinzu'], ImgDir+'/DataStoreGrey.gif', self.WebDialog, s['WebHinzu2'] )
        self.toolbar.add('HinzuButton', s['DateiHinzu'], ImgDir+'/DataStore.gif', self.datei_hinzu, s['DateiHinzu2'] )
        self.toolbar.add('EntfernButton', s['DateiWeg'], ImgDir+'/DataExtract.gif', self.datei_entfernen, s['DateiWeg2'])
        self.toolbar.add_separator()
        self.toolbar.add('FrequenzButton', s['FreqZeigen'], ImgDir+'/Column.gif', self.zeigWortfrequenz, s['FreqZeigen2'])
        self.toolbar.add_separator()
        self.toolbar.add('CopyButton', s['Kopieren'], ImgDir+'/Copy.gif', self.copy2clipboard, s['Kopieren2'])
        self.toolbar.add_separator()
        # self.toolbar.add('ExcelButton', s['Ex2excel'], ImgDir+'/NewSheet.gif', self.export2excel, s['Ex2excel2'])
        # self.toolbar.add('WordButton', s['Ex2word'], ImgDir+'/DocumentDraw.gif', self.export2word, s['Ex2word2'])
        # self.toolbar.add_separator()
        self.toolbar.add('HelpButton', s['Info'], ImgDir+'/Help.gif', self.about, s['Info2'])


        # Die Arbeitsflaeche
        self.tabPages = TabPage.TabPageSet(self.fenster,
                                           pageNames=[s['KorpusTab'], s['FormenTab'],
                                                      s['ConcTab'], s['ZitatTab'],
                                                      s['LConcTab'],  s['TextGraphTab']]) #s['ClustNGramsTab'], s['CollocatesTab'],
        self.tabPages.pack( expand=TRUE,fill=BOTH )
        self.machKorpusTab()
        self.machFormenTab()
        self.machKonkordanzTab()
        self.machZitatTab()
        self.machListKonkordanzTab()
        #self.machCollocatesTab()
        self.machTextGraphTab()
        self.tabPages.pages[s['KorpusTab']]['page'].lift()


        # Beim ersten Start: Sprache festlegen
        if not os.path.exists(cfgFile):
            self.info('TextSTAT language', 'Welcome to TextSTAT! \n\nYou can change the language of the TextSTAT interface (Menu > Language) \nAvailable Languages are: English, German, Russian, Dutch, French, Italian, Potuguese, Spanish, Galician, Finnish, Polish and Czech')
            self.optionen_speichern()

            
    def machKorpusTab(self):
        frame=self.tabPages.pages[s['KorpusTab']]['page']
        self.infotxt = StringVar()
        self.infolabel = Label(frame, wraplength=200, justify=LEFT, textvariable=self.infotxt)
        self.infolabel.pack(side=RIGHT, padx=10, pady=10)

        listframe = Frame(frame)
        listframe.pack(expand=YES, fill=BOTH, side=LEFT, padx=5, pady=5)
        vscrollbar = Scrollbar(listframe, orient=VERTICAL)
        hscrollbar = Scrollbar(listframe, orient=HORIZONTAL)
        self.datliste = Listbox(listframe, selectmode=EXTENDED, borderwidth=1, yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)
        vscrollbar.config(command=self.datliste.yview)
        hscrollbar.config(command=self.datliste.xview)
        vscrollbar.pack(side=RIGHT, fill=Y, padx=0)
        hscrollbar.pack(side=BOTTOM, fill=X, pady=0)
        self.datliste.pack(side=LEFT, expand=YES, fill=BOTH, padx=0)

        self.datliste.bind('<Enter>', self.statusAktualisieren)
        self.datliste.bind('<Button-3>', self.KorpusTabPopup)
        self.datliste.bind('<Double-Button-1>', self.datei_oeffnen)
        self.infotxt.set(s['KTinfo'])


    def KorpusTabPopup(self, event):
        self.KorpusPopupMenu = Menu(self.root, tearoff=0)
        self.KorpusPopupMenu.add_command(label=s['KTkopieren'], command=self.copy2clipboard)
        self.KorpusPopupMenu.add_command(label=s['KTopen'], command=self.datei_oeffnen)
        self.KorpusPopupMenu.add_command(label=s['KTdatinfo'], command=self.datei_info)
        self.KorpusPopupMenu.add_command(label=s['KTdatweg'], command=self.datei_entfernen)
        self.KorpusPopupMenu.tk_popup(*self.root.winfo_pointerxy())


    def machFormenTab(self):
        frame=self.tabPages.pages[s['FormenTab']]['page']
        listframe = Frame(frame)
        listframe.pack(side=LEFT, expand=YES, fill=BOTH, padx=5, pady=5)
        self.freqliste = MultiListBox.MultiListbox(listframe, ((s['FTwortform'], 55), (s['FTfrequenz'], 5)),
                                                   command=self.zeigKonkordanz, borderwidth=1, height=20)
        self.freqliste.pack(side=LEFT, fill=BOTH, expand=YES)
        for l in self.freqliste.lists:
            l.bind('<Enter>', self.statusAktualisieren)
            l.bind('<Button-3>', self.FormenTabPopup)

        optFrame = LabelFrame(frame, text=s['FTOptionen'])
        optFrame.pack(fill=X, padx=5, pady=5)
        # Label(optFrame, text=s['FTinfo'], justify=LEFT).pack(anchor=W)

        optFrame1 = Frame(optFrame)
        optFrame1.pack(fill=BOTH, pady=10)
        self.sortModusFreq = StringVar()
        Radiobutton(optFrame1, text=s['FTsortFreq'], value='freq', variable=self.sortModusFreq).pack(anchor=W)
        Radiobutton(optFrame1, text=s['FTsortAlpha'], value='alpha', variable=self.sortModusFreq).pack(anchor=W)
        Radiobutton(optFrame1, text=s['FTsortRetro'], value='retro', variable=self.sortModusFreq).pack(anchor=W)
        self.sortModusFreq.set('freq')

        optFrame2 = Frame(optFrame)
        optFrame2.pack(fill=X, padx=5)
        self.minFreq = StringVar()
        self.minFreq.set(cfg['freqMin'])
        Spinbox(optFrame2, width=5, textvariable=self.minFreq, values=('---',1,2,3,4,5,10,25,50,100,250,500,750,1000,2500,5000,10000)).pack(side=LEFT, anchor=W)
        Label(optFrame2, text=s['FTminFreq']).pack(side=LEFT, padx=5)

        optFrame3 = Frame(optFrame)
        optFrame3.pack(fill=X, padx=5)
        self.maxFreq = StringVar()
        self.maxFreq.set(cfg['freqMax'])
        Spinbox(optFrame3, width=5, textvariable=self.maxFreq, values=('---',1,2,3,4,5,10,25,50,100,250,500,750,1000,2500,5000,10000)).pack(side=LEFT, anchor=W)
        Label(optFrame3, text=s['FTmaxFreq']).pack(side=LEFT, padx=5)

        self.grosskleinFreq = IntVar()
        Checkbutton(optFrame, text=s['FTignGross'], variable=self.grosskleinFreq).pack(pady=10, anchor=W)

        self.suchFreq = StringVar()
        Label(optFrame, text=s['FTsuchFreq'], justify=LEFT).pack(anchor=W, padx=5)
        self.suchFreqEntry = Entry(optFrame, textvariable=self.suchFreq)
        self.suchFreqEntry.pack(anchor=W, padx=5)
        self.suchFreqEntry.bind('<Return>', self.zeigWortfrequenz)

        Button(optFrame, text=s['FTfreqliste'], command=self.zeigWortfrequenz).pack(anchor=W, padx=5, pady=10)


    def FormenTabPopup(self, event):
        self.FormenPopupMenu = Menu(self.root, tearoff=0)
        self.FormenPopupMenu.add_command(label=s['FTkopieren'], command=self.copy2clipboard)
        self.FormenPopupMenu.add_command(label=s['FTsuchKonk'], command=self.zeigKonkordanz)
        self.FormenPopupMenu.add_command(label=s['FTzeigInfo'], command=self.zeigFormInfo)
        self.FormenPopupMenu.tk_popup(*self.root.winfo_pointerxy())


    def machKonkordanzTab(self):
        frame=self.tabPages.pages[s['ConcTab']]['page']
        suchFrame = Frame(frame)
        suchFrame.pack(fill=X, padx=10, pady=5)
        self.suchwort = Entry(suchFrame, width=40, takefocus=1)
        self.suchwort.pack(side=LEFT)
        self.suchwort.bind("<Return>", self.zeigKonkordanz)
        Button(suchFrame, text=s['CTsuchen'], takefocus=1, command=self.zeigKonkordanz).pack(side=LEFT, padx=5, pady=10)
        Button(suchFrame, text=s['CTmachQuery'], command=self.QueryDialog).pack(anchor=W, padx=20, pady=10)

        listframe = Frame(frame)
        listframe.pack(expand=YES, fill=BOTH, side=LEFT, padx=5, pady=5)
        self.konkliste = MultiListBox.MultiListbox(listframe, ((s['ConcTab'], 60),),
                                                   command=self.zeigZitat, borderwidth=1, height=20)
        self.konkliste.pack(side=LEFT, fill=BOTH, expand=YES)
        for l in self.konkliste.lists:
            l.bind('<Enter>', self.statusAktualisieren)
            l.bind('<Button-3>', self.KonkTabPopup)
            l.bind('<Double-Button-1>', self.zeigZitat)

        optFrame = LabelFrame(frame, text=s['CTOptionen'])
        optFrame.pack(fill=X, padx=5, pady=5)

        self.konkGanzewoerter = IntVar()
        Checkbutton(optFrame, text=s['CTganzWort'], variable=self.konkGanzewoerter).pack(anchor=W)
        self.konkGrossklein = IntVar()
        self.konkGrosskleinCheckbutton = Checkbutton(optFrame, text=s['CTignGross'], variable=self.konkGrossklein)
        self.konkGrosskleinCheckbutton.pack(anchor=W)
        self.markKonk = IntVar()
        Checkbutton(optFrame, text=s['CTmarkSuch'], variable=self.markKonk).pack(anchor=W)

        optFrame2 = Frame(optFrame)
        optFrame2.pack(fill=X, padx=5, pady=10)
        optFrame2a = Frame(optFrame2)
        optFrame2a.pack(fill=BOTH)
        self.konkContextL = StringVar()
        self.konkContextL.set(cfg['konkContextL'])
        Spinbox(optFrame2a, width=4, textvariable=self.konkContextL, from_=10, to=100, increment=10).pack(side=LEFT, anchor=W)
        Label(optFrame2a, text=s['CTcontextL']).pack(side=LEFT, padx=5)
        optFrame2b = Frame(optFrame2)
        optFrame2b.pack(fill=BOTH)
        self.konkContextR = StringVar()
        self.konkContextR.set(cfg['konkContextR'])
        Spinbox(optFrame2b, width=4, textvariable=self.konkContextR, from_=10, to=100, increment=10).pack(side=LEFT, anchor=W)
        Label(optFrame2b, text=s['CTcontextR']).pack(side=LEFT, padx=5)

        self.sortModusKonk = StringVar()
        Radiobutton(optFrame, text=s['CTsortAlpha'], value='alpha', variable=self.sortModusKonk).pack(anchor=W)
        Radiobutton(optFrame, text=s['CTsortR'], value='rechts', variable=self.sortModusKonk).pack(anchor=W)
        Radiobutton(optFrame, text=s['CTsortL'], value='links', variable=self.sortModusKonk).pack(anchor=W)
        self.sortModusKonk.set('alpha')

        Button(optFrame, text=s['CTaktualisier'], command=self.zeigKonkordanz).pack(anchor=W, padx=5, pady=10)


    def KonkTabPopup(self, event):
        self.KonkPopupMenu = Menu(self.root, tearoff=0)
        self.KonkPopupMenu.add_command(label=s['CTkopieren'], command=self.copy2clipboard)
        self.KonkPopupMenu.add_command(label=s['CTzeigZitat'], command=self.zeigZitat)
        self.KonkPopupMenu.tk_popup(*self.root.winfo_pointerxy())


    def collTabPopup(self, event):
        self.collPopupMenu = Menu(self.root, tearoff=0)
        self.collPopupMenu.add_command(label=s['CTkopieren'], command=self.copy2clipboard)
        self.collPopupMenu.add_command(label=s['CTzeigZitat'], command=self.zeigZitat)
        self.collPopupMenu.tk_popup(*self.root.winfo_pointerxy())


    def machZitatTab(self):
        frame=self.tabPages.pages[s['ZitatTab']]['page']
        Label(frame, text=s['ZTinfo']).pack(padx=10, pady=10)

        txtframe = Frame(frame)
        txtframe.pack(expand=YES, fill=BOTH, side=LEFT, padx=5, pady=5)
        scrollbar = Scrollbar(txtframe, orient=VERTICAL)
        self.zitat = Text(txtframe, borderwidth=1, wrap=WORD, selectbackground='lightsteelblue', selectforeground='black', yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.zitat.yview)
        scrollbar.pack(side=RIGHT, fill=Y, padx=0)
        self.zitat.pack(side=LEFT, expand=YES, fill=BOTH, padx=0)
        self.zitat.tag_configure('blau', foreground='blue', underline=1)
        self.zitat.tag_configure('rot', foreground='red')
        self.zitat.tag_bind('oeffnen', '<Double-Button-1>', self.zitatDatei_oeffnen)
        self.zitat.bind('<Button-3>', self.ZitatTabPopup)
        self.zitat.config(cursor='arrow')
        self.zitat.insert(END, s['ZTInit'])



    def machListKonkordanzTab(self):
        frame=self.tabPages.pages[s['LConcTab']]['page']
        suchFrame = Frame(frame)
        suchFrame.pack(fill=X, padx=10, pady=5)
        self.suchwort = Entry(suchFrame, width=40, takefocus=1)
        self.suchwort.pack(side=LEFT)
        self.suchwort.bind("<Return>", self.zeigLKonkordanz)
        Button(suchFrame, text=s['CTsuchen'], takefocus=1, command=self.zeigLKonkordanz).pack(side=LEFT, padx=5, pady=10)
        Button(suchFrame, text=s['CTmachQuery'], command=self.QueryDialog).pack(anchor=W, padx=20, pady=10)

        listframe = Frame(frame)
        listframe.pack(expand=YES, fill=BOTH, side=LEFT, padx=5, pady=5)
        self.Lkonkliste = MultiListBox.MultiListbox(listframe, ((s['LConcTab'], 60), (s['Source'], 8)),
                                                    command=self.zeigZitat, borderwidth=1, height=20)
        self.Lkonkliste.pack(side=LEFT, fill=BOTH, expand=YES)
        for l in self.konkliste.lists:
            l.bind('<Enter>', self.statusAktualisieren)
            l.bind('<Button-3>', self.KonkTabPopup)
            l.bind('<Double-Button-1>', self.zeigZitat)

        optFrame = LabelFrame(frame, text=s['CTOptionen'])
        optFrame.pack(fill=X, padx=5, pady=5)

        self.konkGanzewoerter = IntVar()
        Checkbutton(optFrame, text=s['CTganzWort'], variable=self.konkGanzewoerter).pack(anchor=W)
        self.konkGrossklein = IntVar()
        self.konkGrosskleinCheckbutton = Checkbutton(optFrame, text=s['CTignGross'], variable=self.konkGrossklein)
        self.konkGrosskleinCheckbutton.pack(anchor=W)
        self.markKonk = IntVar()
        Checkbutton(optFrame, text=s['CTmarkSuch'], variable=self.markKonk).pack(anchor=W)

        optFrame2 = Frame(optFrame)
        optFrame2.pack(fill=X, padx=5, pady=10)
        optFrame2a = Frame(optFrame2)
        optFrame2a.pack(fill=BOTH)
        self.LkonkContextL = StringVar()
        self.LkonkContextL.set(5)#cfg['konkContextL'])
        Spinbox(optFrame2a, width=4, textvariable=self.LkonkContextL, from_=10, to=100, increment=10).pack(side=LEFT, anchor=W)
        Label(optFrame2a, text=s['CTcontextL']).pack(side=LEFT, padx=5)
        optFrame2b = Frame(optFrame2)
        optFrame2b.pack(fill=BOTH)
        self.LkonkContextR = StringVar()
        self.LkonkContextR.set(5)#cfg['konkContextR'])
        Spinbox(optFrame2b, width=4, textvariable=self.LkonkContextR, from_=10, to=100, increment=10).pack(side=LEFT, anchor=W)
        Label(optFrame2b, text=s['CTcontextR']).pack(side=LEFT, padx=5)
        
        optFrame2c = Frame(optFrame2)
        optFrame2c.pack(fill=BOTH)
        self.LkonkSeparate = StringVar()
        self.LkonkSeparate.set('\W+')
        Entry(optFrame2c, width=17, textvariable=self.LkonkSeparate).pack(anchor=W)
        Label(optFrame2c, text=s['LCTSeparate']).pack(side=LEFT,padx=5)
        optFrame2d = Frame(optFrame2)
        optFrame2d.pack(fill=BOTH)
        self.LkonkSepBy = IntVar()
        self.LkonkSepBy.set(0)
        Checkbutton(optFrame2d, width=4, variable=self.LkonkSepBy).pack(anchor=W)
        Label(optFrame2d, text=s['LCTSepBy']).pack(side=LEFT,padx=5)

        self.sortModusLKonk = StringVar()
        Radiobutton(optFrame, text=s['CTsortAlpha'], value='alpha', variable=self.sortModusLKonk).pack(anchor=W)
        Radiobutton(optFrame, text=s['CTsortR'], value='rechts', variable=self.sortModusLKonk).pack(anchor=W)
        Radiobutton(optFrame, text=s['CTsortL'], value='links', variable=self.sortModusLKonk).pack(anchor=W)
        self.sortModusLKonk.set('alpha')

        Button(optFrame, text=s['CTaktualisier'], command=self.zeigLKonkordanz).pack(anchor=W, padx=5, pady=10)


    def machCollocatesTab(self):
        frame=self.tabPages.pages[s['CollocatesTab']]['page']
        suchFrame = Frame(frame)
        suchFrame.pack(fill=X, padx=10, pady=5)
        self.collsuchwort = Entry(suchFrame, width=40, takefocus=1)
        self.collsuchwort.pack(side=LEFT)
        self.collsuchwort.bind("<Return>", self.zeigKonkordanz)
        Button(suchFrame, text=s['CTsuchen'], takefocus=1, command=self.zeigKonkordanz).pack(side=LEFT, padx=5, pady=10)
        Button(suchFrame, text=s['CTmachQuery'], command=self.QueryDialog).pack(anchor=W, padx=20, pady=10)

        listframe = Frame(frame)
        listframe.pack(expand=YES, fill=BOTH, side=LEFT, padx=5, pady=5)
        self.collliste = MultiListBox.MultiListbox(listframe, (('№', 3), (s['FTfrequenz'], 3), (s['ClTFreqL'], 3), (s['ClTFreqR'], 3), (s['ClTKoef'], 3), (s['ClTToken'], 47)),
                                                   command=self.zeigZitat, borderwidth=1, height=20)
        self.collliste.pack(side=LEFT, fill=BOTH, expand=YES)
        for l in self.collliste.lists:
            l.bind('<Enter>', self.statusAktualisieren)
            l.bind('<Button-3>', self.collTabPopup)
            l.bind('<Double-Button-1>', self.zeigZitat)

        optFrame = LabelFrame(frame, text=s['CTOptionen'])
        optFrame.pack(fill=X, padx=5, pady=5)

        self.collGanzewoerter = IntVar()
        Checkbutton(optFrame, text=s['CTganzWort'], variable=self.collGanzewoerter).pack(anchor=W)
        self.collGrossklein = IntVar()
        self.collGrosskleinCheckbutton = Checkbutton(optFrame, text=s['CTignGross'], variable=self.collGrossklein)
        self.collGrosskleinCheckbutton.pack(anchor=W)
        self.markKonk = IntVar()
        Checkbutton(optFrame, text=s['CTmarkSuch'], variable=self.markKonk).pack(anchor=W)

        optFrame2 = Frame(optFrame)
        optFrame2.pack(fill=X, padx=5, pady=10)
        optFrame2a = Frame(optFrame2)
        optFrame2a.pack(fill=BOTH)
        self.collContextL = StringVar()
        self.collContextL.set(cfg['konkContextL'])
        Spinbox(optFrame2a, width=4, textvariable=self.collContextL, from_=10, to=100, increment=10).pack(side=LEFT, anchor=W)
        Label(optFrame2a, text=s['CTcontextL']).pack(side=LEFT, padx=5)
        optFrame2b = Frame(optFrame2)
        optFrame2b.pack(fill=BOTH)
        self.collContextR = StringVar()
        self.collContextR.set(cfg['konkContextR'])
        Spinbox(optFrame2b, width=4, textvariable=self.collContextR, from_=10, to=100, increment=10).pack(side=LEFT, anchor=W)
        Label(optFrame2b, text=s['CTcontextR']).pack(side=LEFT, padx=5)

        self.sortModusColl = StringVar()
        Radiobutton(optFrame, text=s['CTsortAlpha'], value='alpha', variable=self.sortModusColl).pack(anchor=W)
        Radiobutton(optFrame, text=s['CTsortR'], value='rechts', variable=self.sortModusColl).pack(anchor=W)
        Radiobutton(optFrame, text=s['CTsortL'], value='links', variable=self.sortModusColl).pack(anchor=W)
        self.sortModusKonk.set('alpha')

        Button(optFrame, text=s['CTaktualisier'], command=self.zeigKonkordanz).pack(anchor=W, padx=5, pady=10)


    def machTextGraphTab(self):
        frame = self.tabPages.pages[s['TextGraphTab']]['page']
        searchFrame = Frame(frame)
        searchFrame.pack(fill=X, padx=10, pady=5)
        searchFrame2 = Frame(frame)
        searchFrame2.pack(fill=X, padx=10, pady=5)
        statFrame = Frame(frame)
        statFrame.pack(fill=X, padx=10, pady=5)
        Label(searchFrame, text=s['TGSWordPattern']).pack(side=LEFT)
        self.word_pattern = Entry(searchFrame, width=50, takefocus=1)
        self.word_pattern.insert(END, s['TGdefaultWordPattern'])
        self.word_pattern.pack(side=LEFT)
        Label(searchFrame2,text=s['TGStopWords']).pack(side=LEFT)
        self.stop_words = Entry(searchFrame2, width=50, takefocus=1)
        self.stop_words.insert(END, s['TGdefaultStopWords'])
        self.stop_words.pack(side=LEFT)
        Button(searchFrame, text=s['TGCompTextGraph'], takefocus=1, command=self.compute_text_graph_stat).pack(anchor=W, padx=5, pady=10)
        self.textGraphStatFrame = Frame(frame)
        self.textGraphStatFrame.pack(expand=YES, fill=BOTH, side=LEFT, padx=5, pady=5)
        self.textGraphList = MultiListBox.MultiListbox(
                            self.textGraphStatFrame, (('-',8), (s['TGmaxWord'],17), (s['TGmaxValue'],4),
                            (s['TGminWord'],17), (s['TGminValue'],3), (s['TGavgWord'],17), (s['TGavgValue'], 4)),
                            borderwidth=1, height=20)
        self.textGraphList.pack(side=LEFT, fill=BOTH, expand=YES)
        buttonsFrame = LabelFrame(frame,text=s['Also'])
        buttonsFrame.pack(fill=X, padx=5, pady=5)
        Button(buttonsFrame, text=s['tf-idf'], takefocus=1, command=self.compute_text_graph_tf_idf).pack(anchor=W, padx=5, pady=10)
        self.N_keywords = StringVar()
        Spinbox(buttonsFrame, textvariable=self.N_keywords,from_=1,to=25,increment=1,width=3).pack(anchor=S)
        Button(buttonsFrame, text=s['TGExport'], takefocus=1, command=self.text_graph_export).pack(anchor=W, padx=5, pady=10)
        Button(buttonsFrame, text=s['TGGraphs'], takefocus=1, command=self.text_graph_show_graphs).pack(anchor=W, padx=5, pady=10)
        Button(buttonsFrame, text=s['TGStemming'], takefocus=1, command=self.text_graph_stemming).pack(anchor=W, padx=5, pady=10)

        def upd(event=None):
            #tkMessageBox.askquestion(s['KorpusSave'], s['AbfrageSave'])
            if self.korpus != None:
                if self.korpus.textGraph == None:
                    try:
                        self.tabPages.ChangePage(s['TextGraphTab'])
                        self.status.set(s["TGLoadStatus"])
                        self.korpus.getTextGraph()
                    except:
                        return
                self.status.set(s['TGSuccessLoadStatus'])
                if self.textGraphList.size()<=1:
                    self.update_data_text_graph_tab()

        self.tabPages.pages[s['TextGraphTab']]['tab'].button.bind('<Button-1>', upd)
        #self.data_text_graph_tab_TEST()

        
    def compute_text_graph_tf_idf(self, event=None):
        keywords = dict()
        idf = dict()
        N_keywords=int(self.N_keywords.get())
        from math import log
        for f,tg in self.korpus.textGraph:
            tg.add_properties('edge',tf_idf=0)
            for e in tg.edge.keys():
                for ee in tg.edge[e].keys():
                    tg.edge[e][ee]['tf_idf']=((tg.edge[e][ee]['weight']*\
                                             (tg.edge[e][ee]['textPositionLast']-tg.edge[e][ee]['textPositionFirst']))/\
                                             ((tg.get('edge',tg.edge_list['textPositionLast'][0])['textPositionLast']+1)**2))
                    if idf.get((e,ee)):
                        idf[(e,ee)]+=1
                    else:
                        idf[(e,ee)]=1
        D = len(self.korpus.textGraph)
        for f,tg in self.korpus.textGraph:
            for e in tg.edge.keys():
                for ee in tg.edge[e].keys():
                    tg.edge[e][ee]['tf_idf']*=log(D/float(idf[(e,ee)]),2)
            tg.sort_edge(prop='tf_idf')
        i=0
        for f,tg in self.korpus.textGraph:
            keywords[f]=tg.edge_list['tf_idf'][:N_keywords/2]
            while (len(keywords[f]) < N_keywords and i<40):
                for ee in tg.edge_list['tf_idf'][N_keywords/2:]:
                    if ((ee[0] == e[0] or ee[0] == e[1]) and (e,ee) not in keywords[f]):
                        keywords[f].append(ee)
                        break
                i+=1
        text = ''
        for f in keywords.keys():
            text+=f+':\n'
            for k in keywords[f]:
                text += k[0]+' '+k[1]+'; '
            text += '\n\n'

        self.TF_IDF_Dialog(text=text)

    def text_graph_export(self, event=None):
        dd = tkFileDialog.askdirectory(initialdir=cfg['KorpDir'])
        for f,tg in self.korpus.textGraph:
            t0 = u' ; '.join((s['TGVertecesCount'], unicode(tg.number_of_nodes()),
                            s['TGEdgesCount'], unicode(tg.number_of_edges())))+u'\n'
            for p in tg.node_property:
                mx, mn, avg = tg.node_list[p][0], tg.node_list[p][-1], float(
                    sum([tg.node[s1][p] for s1 in tg.node_list[p]])) / tg.number_of_nodes()
                ca = tg.find('node', p, avg)
                t0 += u' ; '.join((p, mx, unicode(tg.node[mx][p]),
                                 mn, unicode(tg.node[mn][p]),
                                 ca, unicode(tg.node[ca][p])))+u'\n'
                # (p,mx,tg.node[mx][p],mn,tg.node[mn][p],avg,ca,tg.node[ca][p])
            t0 += u' ; '.join((' - ',) * 7)+u'\n'
            for p in tg.edge_property:
                mx, mn, avg = tg.edge_list[p][0], tg.edge_list[p][-1], float(
                    sum([tg.edge[s1[0]][s1[1]][p] for s1 in
                         tg.edge_list[p]])) / tg.number_of_edges()
                ca = tg.find('edge', p, avg)
                t0 += u' ; '.join((p, (mx[0]+u'-'+mx[1]),
                                   unicode(tg.edge[mx[0]][mx[1]][p]),
                                (mn[0]+u'-'+mn[1]),
                                   unicode(tg.edge[mn[0]][mn[1]][p]),
                                (ca[0]+u'-'+ca[1]),
                                   unicode(tg.edge[ca[0]][ca[1]][p])))+u'\n'
            d = open(dd + '/' + os.path.split(f)[-1][:245] + '_extr.csv', 'wb')
            d.write(t0.encode('utf-8'))
            d.close()

    def text_graph_show_graphs(self, event=None):
        import matplotlib.pyplot as plt
        for f, tg in self.korpus.textGraph:
            y = [tg.node[i]['weight'] for i in tg.node_list['weight'] if
                 tg.node[i]['weight'] > 1]
            if len(y) == 0:
                print('No inputs', fileName)
                return 0
            if (y[0] >= y[-1]):
                x = list(range(0, len(y)))
            else:
                x = list(range(len(y), 0))
            plt.plot(x, y, color='b')
            plt.title("Frequency of words in full text")
            plt.ylabel('Frequency')
            plt.xlabel('Order')
            plt.show()

            y = [tg.edge[i[0]][i[1]]['weight'] for i in tg.edge_list['weight']
                 if tg.edge[i[0]][i[1]]['weight'] > 1]
            if len(y) == 0:
                print('No inputs', fileName)
                return 0
            if (y[0] >= y[-1]):
                x = list(range(0, len(y)))
            else:
                x = list(range(len(y), 0))
            plt.plot(x, y, color='r')
            plt.title("Frequency of word's pairs in full text")
            plt.ylabel('Frequency')
            plt.xlabel('Order')
            plt.show()

    def text_graph_stemming(self, event=None):
        for f, tg in self.korpus.textGraph:
            tg = tg.get_morphem_absolut_grpah()

    def ZitatTabPopup(self, event):
        self.ZitatPopupMenu = Menu(self.root, tearoff=0)
        self.ZitatPopupMenu.add_command(label=s['ZTkopieren'], command=self.copy2clipboard)
        self.ZitatPopupMenu.add_command(label=s['ZToeffnen'], command=self.zitatDatei_oeffnen)
        self.ZitatPopupMenu.tk_popup(*self.root.winfo_pointerxy())


    def WebDialog(self):
        try:
            self.wd.focus_set()
        except:
            self.wd = Toplevel(self.root)
            self.wd.title("Web2corpus - TextSTAT WebSpider")
            frame = Frame(self.wd)
            frame.pack(expand=YES, fill=BOTH, padx=10, pady=10)
            Label(frame, justify=LEFT, text=s['WDinfo']).pack(anchor=W, padx=10, pady=5)
            self.webUrl = StringVar()
            url = Entry(frame, width=50, textvariable=self.webUrl)
            url.pack(anchor=W, padx=10, pady=5)
            Label(frame, text=s['WDfrageSeiten']).pack(anchor=W, padx=10, pady=5)

            frame1 = Frame(frame)
            frame1.pack(expand=YES, fill=BOTH)
            self.webAnzahl = StringVar()
            self.webAnzahl.set('1')
            Spinbox(frame1, width=5, textvariable=self.webAnzahl, values=(1,10,25,50,100,250,500,750,1000)).pack(side=LEFT, anchor=W, padx=10, pady=5)
            Label(frame1, text=s['WDanzahl']).pack(side=LEFT)
            self.webBasis = StringVar()
            self.webBasis.set('server')
            Radiobutton(frame, text=s['WDinSubdir'], value='subdir', variable=self.webBasis).pack(anchor=W, padx=10 )
            Radiobutton(frame, text=s['WDaufServer'], value='server', variable=self.webBasis).pack(anchor=W, padx=10 )
            Button(frame, text=s['WDok'], width=10, command=self.htmlFile_hinzu).pack(side=LEFT, padx=10, pady=10)
            Button(frame, text=s['WDcancel'], width=10, command=self.wd.destroy).pack(side=RIGHT, padx=10, pady=10)
            url.focus_set()


    def NewsDialog(self):
        try:
            self.nd.focus_set()
        except:
            self.nd = Toplevel(self.root)
            self.nd.title("News2corpus - TextSTAT NewsGrabber")
            frame = Frame(self.nd)
            frame.pack(expand=YES, fill=BOTH, padx=10, pady=10)
            Label(frame, justify=LEFT, text=s['NDinfo']).pack(anchor=W, padx=10, pady=5)

            frame1 = Frame(frame)
            frame1.pack(expand=YES, fill=BOTH)
            self.newsServer = StringVar()
            Entry(frame1, width=40, textvariable=self.newsServer).pack(side=LEFT, anchor=W, padx=10, pady=5)
            Label(frame1, text=s['NDserver']).pack(side=LEFT, padx=10, pady=5)

            frame2 = Frame(frame)
            frame2.pack(expand=YES, fill=BOTH)
            self.newsGruppe = StringVar()
            Entry(frame2, width=40, textvariable=self.newsGruppe).pack(side=LEFT, anchor=W, padx=10, pady=5)
            Label(frame2, text=s['NDgruppe']).pack(side=LEFT, padx=10, pady=5)

            frame3 = Frame(frame)
            frame3.pack(expand=YES, fill=BOTH)
            self.newsAnzahl = StringVar()
            self.newsAnzahl.set('50')
            Spinbox(frame3, width=5, textvariable=self.newsAnzahl, values=(1,10,25,50,100,250,500,750,1000)).pack(side=LEFT, anchor=W, padx=10, pady=5)
            Label(frame3, text=s['NDanzahl']).pack(side=LEFT)
            self.newsZitate = IntVar()
            self.newsZitate.set(1)
            Checkbutton(frame3, text=s['NDzitWeg'], variable=self.newsZitate).pack(side=LEFT, padx=20)

            Button(frame, text=s['NDok'], width=10, command=self.newsgroup_hinzu).pack(side=LEFT, padx=10, pady=10)
            Button(frame, text=s['NDcancel'], width=10, command=self.nd.destroy).pack(side=RIGHT, padx=10, pady=10)
            self.nd.focus_set()


    def QueryDialog(self):
        try:
            self.qd.focus_set()
        except:
            self.qd = Toplevel(self.root)
            self.qd.title("TextSTAT QueryEditor")
            frame = Frame(self.qd)
            frame.pack(expand=YES, fill=BOTH, padx=10, pady=10)
            Label(frame, justify=LEFT, text=s['QDinfo'], fg='blue').pack(anchor=W, padx=5, pady=15)

            frame1 = LabelFrame(frame, text=s['QDsuchFelder'])
            frame1.pack(fill=BOTH, expand=YES)
            frame1a = Frame(frame1)
            frame1a.pack(expand=YES, fill=BOTH)
            self.qAusdruck1 = Entry(frame1a)
            self.qAusdruck1.pack(side=LEFT, anchor=W, padx=5, pady=5)
            Label(frame1a, text=s['QAusdruck1']).pack(side=LEFT, padx=5, pady=5)
            frame1b = Frame(frame1)
            frame1b.pack(expand=YES, fill=BOTH)
            self.qAusdruck2 = Entry(frame1b)
            self.qAusdruck2.pack(side=LEFT, anchor=W, padx=5, pady=5)
            Label(frame1b, text=s['QAusdruck2']).pack(side=LEFT, padx=5, pady=5)

            frame2 = LabelFrame(frame, text=s['QAbstand'])
            frame2.pack(fill=BOTH, expand=YES, pady=30)
            self.qAbstandMin = Spinbox(frame2, width=5, from_=0, to=10)
            self.qAbstandMin.pack(side=LEFT, anchor=W, padx=5, pady=5)
            Label(frame2, text=s['QAbstandMin']).pack(side=LEFT, padx=5, pady=5)
            self.qAbstandMax = Spinbox(frame2, width=5, from_=0, to=10)
            self.qAbstandMax.pack(side=LEFT, anchor=W, padx=5, pady=5)
            Label(frame2, text=s['QAbstandMax']).pack(side=LEFT, padx=5, pady=5)

            Button(frame, text=s['QmachAusdruck'], command=self.query_machen).pack(side=LEFT, padx=10, pady=10)
            Button(frame, text=s['QDcancel'], width=10, command=self.qd.destroy).pack(side=RIGHT, padx=10, pady=10)
            self.qd.bind("<Return>", self.query_machen)
            self.qAusdruck1.focus_set()


    def query_machen(self, event=''):
        a1 = self.qAusdruck1.get()
        a1 = a1.replace('*', '\w*')
        a1 = a1.replace('?', '\w')
        a2 = self.qAusdruck2.get()
        a2 = a2.replace('*', '\w*')
        a2 = a2.replace('?', '\w')
        ab1 = self.qAbstandMin.get()
        ab2 = self.qAbstandMax.get()
        if a1 == '' and a2 == '':
            self.warnung(titel=s['Error'], text=s['ErrQuery'])
            self.qAusdruck1.focus_set()
            return

        if ab1 == '0' and ab2 == '0':
            such = "%s\W+%s" % (a1, a2)
        else:
            such = "%s(\W+\w+){%s,%s}\W+%s" % (a1, ab1, ab2, a2)
        self.busyCursorOn()
        self.suchwort.delete(0, END)
        self.suchwort.insert(END, such)
        self.konkGrossklein.set(1)
        self.konkGanzewoerter.set(1)
        self.zeigKonkordanz()
        self.busyCursorOff()


    def TextDialog(self, text='', titel='TextSTAT'):
        try:
            self.td.focus_set()
        except:
            self.td = Toplevel(self.root)
            self.td.transient(self.root)
            self.td.title(titel)
            self.td.geometry('600x400+50+50')
            frame = Frame(self.td)
            frame.pack(expand=YES, fill=BOTH)

            scrollbar = Scrollbar(frame, orient=VERTICAL)
            txt = Text(frame, borderwidth=1, height=15, wrap=WORD, font=(('Courier', 'New'), '9'), yscrollcommand=scrollbar.set)
            scrollbar.config(command=txt.yview)
            scrollbar.pack(side=RIGHT, fill=Y, padx=0)
            txt.pack(side=LEFT, expand=YES, fill=BOTH)
            Button(self.td, text=' OK ', command=self.td.destroy).pack(pady=10)
            txt.insert(END, text)
            self.td.focus_set()


    def zeigHistory(self):
        f = os.path.join(SkriptDir, 'History.txt')
        text = open(f).read()
        t = s['Titel'] + ' - ' + s['History']
        self.TextDialog(text=text, titel=t)


    def zeigLicense(self):
        f = os.path.join(SkriptDir, 'License.txt')
        text = open(f).read()
        t = s['Titel'] + ' - ' + s['License']
        self.TextDialog(text=text, titel=t)


    # Das Korpus
    # Dictionary von Dictionaries, der Dateipfad dient als Key
    # Format: db[dateipfad] = {'path':f, 'file':ff}
    # ansprechen als z.B.: self.korpus[dateipfad]['file']
    # ACHTUNG: in fruehen Versionen war das eine Liste von Listen [dateiname, datei]

    def korpus_new(self):
        # Wenn anderes Korpus geöffnet ist
        if self.korpus != None and self.korpus.dbGeaendert == 1: 
            jn = tkMessageBox.askquestion(s['KorpusSave'], s['AbfrageSave'])
            if jn == 'yes':
                self.korpus_save()
        try:
            f = tkFileDialog.asksaveasfilename(initialdir=cfg['KorpDir'], defaultextension='.crp', title=s['KorpusNew2'])
            if f:
                # Default-Dir neu setzen
                cfg['KorpDir'] = os.path.dirname(f)
                self.korpus = Korpus.Korpus(self)
                self.korpus.newDb(f)
                self.status.set(self.korpus.getDbName())
                self.root.title(s['Titel'] + ' - ' + self.korpus.getDbName())
                self.zeigDateiliste()
                self.add_recent(filename=f)
                self.info(titel=s['CodePage'], text=s['KodierungInfo'] % cfg['FileKodierung'])
        except:
            self.warnung(titel=s['Error'], text=s['ErrKorpNew'])


    def korpus_open(self, filename=''):
        # Wenn anderes Korpus geöffnet ist
        if self.korpus != None and self.korpus.dbGeaendert == 1: 
            jn = tkMessageBox.askquestion(s['KorpusSave'], s['AbfrageSave'])
            if jn == 'yes':
                self.korpus_save()
           
        if filename=='':
            f = tkFileDialog.askopenfilename(initialdir=cfg['KorpDir'], title=s['KorpusOpen'])
        else:
            f=filename
        
        if f:
            self.korpus = None
            self.zeigDateiliste()                         
            try:
                # Default-Dir neu setzen
                self.korpus = Korpus.Korpus(self) 
                self.korpus.openDb(f)
                cfg['KorpDir'] = os.path.dirname(f)
                self.korpusdatei = f
                self.status.set(self.korpus.getDbName())
                self.root.title(s['Titel'] + ' - ' + self.korpus.getDbName())
                self.zeigDateiliste()
                self.add_recent(filename=f)
            except StandardError, details:
                self.korpus = None
                self.root.title(s['Titel'])
                # s['ErrKorpOpen'] = s['ErrKorpOpen'] + '\n\n' + str(details)
                self.warnung(titel=s['Error'], text=s['ErrKorpOpen'])


    def korpus_hinzu(self):
        if self.korpus != None:
            try:
                f = tkFileDialog.askopenfilename(initialdir=cfg['KorpDir'], title=s['KorpusHinzu'])
                if f:
                    # Default-Dir neu setzen
                    cfg['KorpDir'] = os.path.dirname(f)
                    self.korpus.addDb(f)
                    self.status.set(self.korpus.getDbName())
                    self.zeigDateiliste()
                else:
                    pass
            except:
                self.warnung(titel=s['Error'], text=s['ErrKorpOpen'])
        else:
            self.korpus_open()


    def korpus_import(self):
        if self.korpus != None:
            try:
                f = tkFileDialog.askopenfilename(initialdir=cfg['KorpDir'], title=s['KorpusOpen'])
                # Default-Dir neu setzen
                cfg['KorpDir'] = os.path.dirname(f)
                self.korpus.importOldKorpus(f)
                self.status.set(s['StatusKorpImp'])
                self.zeigDateiliste()
            except:
                self.warnung(s['Error'], s['ErrKorpImp'])
        else:
            self.warnung(s['Error'], s['ErrNoKorp'])


    def korpus_save(self):
        try:
            self.korpus.saveDb()
            # self.optionen_speichern()
            self.status.set(s['StatusKorpSave'])
        except:
            self.warnung(titel=s['Error'], text=s['ErrKorpSave'])


    def korpus_save_as(self):
        try:
            f = tkFileDialog.asksaveasfilename(initialdir=cfg['KorpDir'], defaultextension='.crp', title=s['KorpusNew2'])
            # Default-Dir neu setzen
            cfg['KorpDir'] = os.path.dirname(f)
            self.korpusdatei = f
            self.korpus.dbFile = f
            self.korpus.saveDb()
            self.optionen_speichern()
            self.status.set(s['StatusKorpSave'])
            self.root.title(s['Titel'] + ' - ' + self.korpus.getDbName())
            self.add_recent(filename=f)
        except:
            self.warnung(titel=s['Error'], text=s['ErrKorpSave'])


    def korpus_del(self):
        if self.korpus != None:
            f = self.korpus.getDbPath()
            jn = tkMessageBox.askquestion(s['AskSure'], s['AskDelete'] % f)
            if jn == 'yes':
                f = self.korpus.getDbPath()
                self.korpus = None
                os.remove(f)
                self.remove_recent(filename=f)
                self.root.title(s['Titel'])
                self.zeigDateiliste()


    def datei_hinzu(self):
        # 'multiple' funktioniert nur ab Python 2.3, und ach da nicht wirklich, zumindest Win7...
        if self.korpus != None:
            self.statusAktualisieren()
            dateinamen = tkFileDialog.askopenfilename(initialdir=cfg['FileDir'], filetypes= (('All', '*.*'),('Text', '*.txt'),('HTML', '*.htm*'),('MS Word', '*.doc'),('MS Word 2007', '*.docx'),('OpenOffice 1.x', '*.sxw'),('OpenOffice 3.x', '*.odt')), multiple=1)
            
            # Workaround, da die Dateiliste unter Win7 fälschlicherweise als String übergeben wird
            # Dank an Vlastimil Brom für den Hinweis auf diese Lösung, vgl. 
            # http://bugs.python.org/issue5712#msg107935
            if sys.platform == 'win32':
                d = root.tk.splitlist(dateinamen)
                dateinamen = []
                for f in d:
                    dateinamen.append(f.decode('utf-8'))
            else:
                d = dateinamen
                dateinamen = []
                for f in d:
                    dateinamen.append(f.encode('utf-8'))

            if dateinamen:
                try:
                    self.korpus.addDbFiles(dateinamen, codepage=self.dateiart.get())
                    # Default-Dir neu setzen
                    cfg['FileDir'] = os.path.dirname(dateinamen[0])
                    self.zeigDateiliste()
                except StandardError, details:
                    meldung = s['ErrFileOpen'] + '\n\n' + str(details)
                    self.warnung(titel=s['Error'], text=meldung)
        else:
            self.warnung(s['Error'], s['ErrNoKorp'])


    def htmlFile_hinzu(self):
        if self.korpus != None:
            try:
                anzahl = int(self.webAnzahl.get())
            except:
                anzahl = 50

            self.busyCursorOn()
            self.status.set(s['StatusWeb'] % anzahl)
            try:
                self.korpus.addHTMLFiles(url=self.webUrl.get(), anzahl=anzahl,
                                        basis=self.webBasis.get(), codepage=self.dateiart.get())
                self.zeigDateiliste()
            except StandardError, details:
                self.status.set(s['Error'])
                f_meldung = s['ErrWeb'] + '\n\n' + str(details)
                self.warnung(s['Error'], f_meldung)
            self.status.set(' ')
            self.busyCursorOff()
        else:
            self.warnung(s['Error'], s['ErrNoKorp'])


    def newsgroup_hinzu(self):
        if self.korpus != None:
            try:
                anzahl = int(self.newsAnzahl.get())
            except:
                anzahl = 50

            self.busyCursorOn()
            self.status.set(s['StatusNews'] % anzahl)
            try:
                self.korpus.addNewsFiles(server=self.newsServer.get(), gruppe=self.newsGruppe.get(), anzahl=anzahl,
                                         zitate=self.newsZitate.get(), codepage=self.dateiart.get())
                self.zeigDateiliste()
            except StandardError, details:
                self.status.set(s['Error'])
                f_meldung = s['ErrNews'] + '\n\n' + str(details)
                self.warnung(s['Error'], f_meldung)
            self.status.set(' ')
            self.busyCursorOff()
        else:
            self.warnung(s['Error'], s['ErrNoKorp'])


    def datei_oeffnen(self, event=''):
        if self.datliste.curselection() != ():
            i = self.datliste.curselection()
            for x in i:
                dateipfad = self.datliste.get(x)
                try:
                    # os.startfile kann offenbar nicht mir Unicode-Filenamen umgehen... 
                    # webbrowser verwendet aus os.startfile... Tse...
                    dateipfad = dateipfad.encode(sys.getfilesystemencoding())
                    # os.startfile(dateipfad)
                    webbrowser.open(dateipfad)
                except StandardError, details:
                    meldung = s['ErrFileOpen'] + '\n\n' + str(details)
                    self.warnung(titel=s['Error'], text=meldung)
        else:
            self.warnung(titel=s['Error'], text=s['ErrSelect'])


    def datei_entfernen(self, event=''):
        if self.datliste.curselection() != ():
            i = self.datliste.curselection()
            d = []
            for x in i:
                dateipfad = self.datliste.get(x)
                if not sys.platform == 'win32':
                    dateipfad = dateipfad.encode('utf-8')
                d.append(dateipfad)
            self.korpus.delDbFiles(d)
            self.zeigDateiliste()
        else:
            self.warnung(titel=s['Error'], text=s['ErrSelect'])


    def datei_info(self, event=''):
        if self.datliste.curselection() != ():
            i = self.datliste.curselection()
            for x in i:
                dateipfad = self.datliste.get(x)
                key = dateipfad.encode('utf-8')
                f = self.korpus.getDbFile(key)
                info = s['DateiInfo2'] % (os.path.basename(dateipfad), f['path'].decode('utf-8'), len(f['file']))
                self.info(titel=s['DateiInfo'], text=info)
            self.zeigDateiliste()
        else:
            self.warnung(titel=s['Error'], text=s['ErrSelect'])


    def zeigDateiliste(self):
        # erst aufräumen
        self.datliste.delete(0, END)
        self.freqliste.delete(0, END)
        self.konkliste.delete(0, END)


        gesamtgroesse = 0
        if self.korpus != None:
            liste = self.korpus.getDbFileNames()
            for x in liste:
                self.datliste.insert(END, x)
            self.status.indicator(s['StatusFiles'] % (self.korpus.countDbFiles(), self.korpus.getDbSize()))
        else:
            self.status.indicator(s['StatusNoKorp'])
        self.tabPages.ChangePage(s['KorpusTab'])

        self.infotxt.set(s['InfoText'])


    def zeigWortfrequenz(self, event=''):
        if self.korpus != None:
            self.busyCursorOn()
            self.freqliste.delete(0, END)

            freq = self.korpus.getWordFreq( sort=self.sortModusFreq.get(),
                    grossklein=self.grosskleinFreq.get(), minFreq=self.minFreq.get(),
                    maxFreq=self.maxFreq.get(), suchFreq=self.suchFreq.get() )
            self.suchFreq.set('')

            retro = 0
            if self.sortModusFreq.get() == 'retro':
                retro = 1
            
            # Tab wechseln (und dann gleich wieder zurück) - offenbar nötig
            # für korrekte Anzeige auf MACs (Dank an Stian Haklev)
            self.tabPages.ChangePage(s['KorpusTab'])

            for x in freq:
                if retro==1:
                    self.freqliste.insert(END, (x[0].rjust(45), str(x[1]).rjust(9)))
                else:
                    self.freqliste.insert(END, ('  '+x[0], str(x[1]).rjust(9)))

            self.tabPages.ChangePage(s['FormenTab'])
            
            # Wenn Großschreibung hier ignoriert wird, dann sollte sie auch
            # bei den Konkordanzen ignoriert werden...
            if self.grosskleinFreq.get() == 1:
                self.konkGrosskleinCheckbutton.select()
            else:
                self.konkGrosskleinCheckbutton.deselect()        
            
            self.statusAktualisieren()
            self.busyCursorOff()
        else:
            self.warnung(s['Error'], s['ErrNoKorp'])


    def zeigFormInfo(self, event=''):
        such = self.freqliste.get(self.freqliste.curselection())
        form = such[0].strip()
        freq = int(such[1].strip())
        freqfloat = float(freq)
        prozent = freqfloat / self.korpus.anzahlTokens * 100
        txt = s['FTformInfo'] % (self.korpus.anzahlTokens, len(self.korpus.wordFreq), len(self.korpus.wordFreqKlein), form, freq, prozent)
        self.info(form, txt )


    def zeigKonkordanz(self, event=''):
        self.busyCursorOn()
        if self.tabPages.GetActivePage() == s['FormenTab']:
            self.konkGanzewoerter.set(1)
            such = self.freqliste.get(self.freqliste.curselection())
            such = such[0].strip()
        else:
            such = self.suchwort.get()

        try:
            # Stian Haklev: change tab so we can change back afterwards, 
            # and get an updated list view - at least needed on Mac
            self.tabPages.ChangePage(s['KorpusTab'])
            
            self.status.set(s['StatusSuchKonk'])
            self.konkliste.delete(0, END)
            konkRes = self.korpus.getWordConc( pattern=such, ganzWort=self.konkGanzewoerter.get(), grossklein=self.konkGrossklein.get(),
                        cL=self.konkContextL.get(), cR=self.konkContextR.get(),
                        sort=self.sortModusKonk.get(), markKonk=self.markKonk.get() )
            self.suchwort.delete(0, END)
            self.suchwort.insert(END, self.korpus.suchKonk)
            for x in konkRes:################################	inserting Results in multilist with only one column
                self.konkliste.insert(END, (x[0],))
            self.tabPages.ChangePage(s['ConcTab'])
            self.status.set(s['StatusTreffer'] % self.konkliste.size() )
        except StandardError, details:
            self.warnung(titel=s['Error'], text=s['ErrSelect'])
        self.busyCursorOff()


    def zeigLKonkordanz(self, event=''):
        self.busyCursorOn()
        if self.tabPages.GetActivePage() == s['FormenTab']:
            self.konkGanzewoerter.set(1)
            such = self.freqliste.get(self.freqliste.curselection())
            such = such[0].strip()
        else:
            such = self.suchwort.get()

        if 1:#try:
            # Stian Haklev: change tab so we can change back afterwards, 
            # and get an updated list view - at least needed on Mac
            self.tabPages.ChangePage(s['KorpusTab'])
            
            self.status.set(s['StatusSuchKonk'])
            self.Lkonkliste.delete(0, END)
            konkRes = self.korpus.getWordLConc( pattern=such, ganzWort=self.konkGanzewoerter.get(), grossklein=self.konkGrossklein.get(),
                        cL=self.LkonkContextL.get(), cR=self.LkonkContextR.get(),
                        sort=self.sortModusKonk.get(), markKonk=self.markKonk.get(),
                        separate=self.LkonkSeparate.get(),sepBy=self.LkonkSepBy.get())
            self.suchwort.delete(0, END)
            self.suchwort.insert(END, self.korpus.suchKonk)
            for x in konkRes:################################	inserting Results in multilist with only one column
                self.Lkonkliste.insert(END, (x[0],x[2][-8:]))
            self.tabPages.ChangePage(s['LConcTab'])
            self.status.set(s['StatusTreffer'] % self.Lkonkliste.size() )
#        except StandardError, details:
#            self.warnung(titel=s['Error'], text=s['ErrSelect'])
        self.busyCursorOff()


    def zeigZitat(self, event=''):
        self.zitat.delete(1.0, END)
        konk = self.konkliste.curselection()
        konk = int(konk[0])
        cL = int(cfg['zitContextL'])
        cR = int(cfg['zitContextR'])
        res = self.korpus.getContext(konk, contextL=cL, contextR=cR)
        self.zitat.insert(END, '\n')
        self.zitat.insert(END, self.korpus.db[self.korpus.zitatDatei]['path'], ('oeffnen', 'blau'))
        self.zitat.insert(END, s['ZToeffnen2'])
        self.zitat.insert(END, '\n- - - - -\n\n')
        self.zitat.insert(END, res[0])
        self.zitat.insert(END, res[1], 'rot')
        self.zitat.insert(END, res[2])
        self.tabPages.ChangePage(s['ZitatTab'])


    def zitatDatei_oeffnen(self, event=''):
        try:
            # etwas krampfig, da os.startfile()und webbrowser keine 
            # Unicode-Dateinamen unterstuetzen
            dateipfad = self.korpus.db[self.korpus.zitatDatei]['path']
            # dateipfad = dateipfad.encode(sys.getfilesystemencoding())
            webbrowser.open(dateipfad)
        except StandardError, details:
            meldung = s['ErrFileOpen'] + '\n\n' + str(details)
            self.warnung(titel=s['Error'], text=meldung)



    def compute_text_graph_stat(self, event=''):
        self.busyCursorOn()

        try:
            self.tabPages.ChangePage(s['KorpusTab'])

            self.status.set(s['TGComputeStatus'])
            self.korpus.dbTextGraph(search_query=self.word_pattern.get(),
                                    stop_words=self.stop_words.get().split(','))
            self.tabPages.ChangePage(s['TextGraphTab'])
            self.update_data_text_graph_tab()
            #self.status.set(s['StatusTreffer'] % self.konkliste.size())
        except StandardError, details:
            self.warnung(titel=s['Error'], text=s['ErrSelect'])
        self.busyCursorOff()

    def TF_IDF_Dialog(self, text='', titel='TextSTAT TF-IDF'):
        try:
            self.td.focus_set()
        except:
            self.td = Toplevel(self.root)
            self.td.transient(self.root)
            self.td.title(titel)
            self.td.geometry('600x400+50+50')
            frame = Frame(self.td)
            frame.pack(expand=YES, fill=BOTH)

            scrollbar = Scrollbar(frame, orient=VERTICAL)
            txt = Text(frame, borderwidth=1, height=15, wrap=WORD, font=(('Courier', 'New'), '9'), yscrollcommand=scrollbar.set)
            scrollbar.config(command=txt.yview)
            scrollbar.pack(side=RIGHT, fill=Y, padx=0)
            txt.pack(side=LEFT, expand=YES, fill=BOTH)
            Button(self.td, text=' OK ', command=self.td.destroy).pack(pady=10)
            txt.insert(END, text)
            self.td.focus_set()

    def compute_sentences_text_graph_stat(self, event=''):
        pass

    def lable_grid_row(self, parent, row_list, row=0):
        i=0
        for t in row_list:
            Label(parent, text=t).grid(column=i, row=row)
            i += 1

    def data_text_graph_tab_TEST(self):
        self.textGraphList.delete(0, END)
        for f in ('1) First text','2) Second text', '3) Third text'):
            self.textGraphList.insert(END, ('', f[-17:])+('',)*6)
            #self.textGraphList.insert(END, ('Property', 'Max', 'Value', 'Min', 'Value',
            #                        'Avg Value', 'Closest Avg', 'Value'))
            i=1
            for p in ('wV', 'fPV', 'aPV', 'lPV', 'Ei', 'Eo'):
                mx, mn, avg = 'TestWordMx', 'TestWordMn', 8 #tg.node_list[p][0], tg.node_list[p][-1], float(
                    #sum([tg.node[s][p] for s in tg.node_list[p]])) / tg.number_of_nodes()
                ca = 'Test-Word'#tg.find('node', p, avg)
                self.textGraphList.insert(END, (p, mx.encode('utf-8'), 17,
                                        mn.encode('utf-8'), 1, ca.encode('utf-8'), avg))
                i+=1
                # (p,mx,tg.node[mx][p],mn,tg.node[mn][p],avg,ca,tg.node[ca][p])
            self.textGraphList.insert(END, (' - ',)*7)
            #self.lable_grid_row(lf, ('Property', 'Max', 'Value', 'Min', 'Value',
            #                         'Avg Value', 'Closest Avg', 'Value'),i+2)
            #lf.pack()


    def update_data_text_graph_tab(self):
        global s
        self.textGraphList.delete(0, END)
        for f,tg in self.korpus.textGraph:
            self.textGraphList.insert(END, ('', f[-17:], s['TGVertecesCount'], str(tg.number_of_nodes()),
                                            s['TGEdgesCount'], str(tg.number_of_edges()),''))
            for p in tg.node_property:
                mx, mn, avg = tg.node_list[p][0], tg.node_list[p][-1], float(
                    sum([tg.node[s1][p] for s1 in tg.node_list[p]])) / tg.number_of_nodes()
                ca = tg.find('node', p, avg)
                self.textGraphList.insert(END, (p, mx.encode('utf-8'), tg.node[mx][p],
                                                mn.encode('utf-8'), tg.node[mn][p],
                                                ca.encode('utf-8'), tg.node[ca][p]))
                # (p,mx,tg.node[mx][p],mn,tg.node[mn][p],avg,ca,tg.node[ca][p])
            self.textGraphList.insert(END, (' - ',) * 7)
            for p in tg.edge_property:
                mx, mn, avg = tg.edge_list[p][0], tg.edge_list[p][-1], float(
                    sum([tg.edge[s1[0]][s1[1]][p] for s1 in
                         tg.edge_list[p]])) / tg.number_of_edges()
                ca = tg.find('edge', p, avg)
                self.textGraphList.insert(END,
                      (p, (mx[0]+u'-'+mx[1]).encode('utf-8'),
                       tg.edge[mx[0]][mx[1]][p],
                       (mn[0]+u'-'+mn[1]).encode('utf-8'),
                       tg.edge[mn[0]][mn[1]][p],
                       (ca[0]+u'-'+ca[1]).encode('utf-8'),
                       tg.edge[ca[0]][ca[1]][p]))
            self.textGraphList.insert(END, (' - ',) * 7)


###########
# Allerlei Hilfsfunktionen

    def optionen_speichern(self):
        try:
            cfg['Benutzersprache'] = self.sprache_aendern.get()
            cfg['fenster'] = self.root.geometry()
            cfg['freqMin'] = self.minFreq.get()
            cfg['freqMax'] = self.maxFreq.get()
            cfg['konkContextL'] = self.konkContextL.get()
            cfg['konkContextR'] = self.konkContextR.get()
            cfg['FileKodierung'] = self.dateiart.get()
            try:
                cfg['LetzteKorpusFiles0'] = self.LetzteKorpusFiles[0]
                cfg['LetzteKorpusFiles1'] = self.LetzteKorpusFiles[1]
                cfg['LetzteKorpusFiles2'] = self.LetzteKorpusFiles[2]
                cfg['LetzteKorpusFiles3'] = self.LetzteKorpusFiles[3]
            except:
                pass

            f = open(cfgFile, 'w')
            cPickle.dump(cfg, f)
            f.close()
        except:
            self.warnung(s['Error'], s['ErrOptSave'])

    def add_recent(self,filename=''):
        filename = os.path.normpath(filename)
        # SH: adds recent file to the recent files list, removing it first if it already exists
        if(self.LetzteKorpusFiles.count(filename)) > 0:
            self.LetzteKorpusFiles.remove(filename)
        self.LetzteKorpusFiles.insert(0,filename)
        self.update_recentfiles_menu()

    def remove_recent(self,filename=''):           # SH: remove file from recent files list if it is on the list
        if(self.LetzteKorpusFiles.count(filename)) > 0:
            self.LetzteKorpusFiles.remove(filename)
            self.update_recentfiles_menu()


    # SH: update recent files - deletes all previous menu entries and adds the last four opened
    def update_recentfiles_menu(self):
        try:											 # SH:designed so that if there are only 2 latest files,
            self.recentfilesmenu.delete(0,3)			 # they will be added, and it will fail gracefully
            filename=self.LetzteKorpusFiles[0]			 # SH: check if there are any latest files
            self.filemenu.entryconfigure(6,state=ACTIVE) # SH: only if the previous command worked, ie there is at least 
														 # one active file		   
            for i in range(0,4):
                f = self.LetzteKorpusFiles[i]
                callback = self.__korpus_open(f)
                self.recentfilesmenu.add_command(label=f, underline=0, command = callback)
        except:
            pass		

    # SH: helping function for the open recent files since Tk Menubuttons cannot accept commands with arguments 
    # (idea taken from IDLE source)
    def __korpus_open(self,f):
        def korpus_open_caller(f=f):
            self.korpus_open(f)
        return korpus_open_caller


    def export2excel(self):
        wortliste = self.freqliste.get(0, END)
        if len(wortliste) > 65000:
            self.warnung(s['ErrExport'], s['ErrExcel65K'] % len(wortliste))
        else:
            try:
                if len(wortliste) > 1:
                    wortliste = [(a.strip(), b.strip()) for (a, b) in wortliste]
                    meinXL = Dispatch("Excel.Application")
                    meinXL.Visible = 1
                    meinXL.Workbooks.Add()
                    tabelle = meinXL.Workbooks(1).Sheets(1)
                    tabelle.Cells(2,1).Value = 'ACHTUNG - ATTENTION'
                    tabelle.Cells(3,1).Value = 'Dies kann dauern...'
                    tabelle.Cells(4,1).Value = 'This can take a while...'
                    titel = '%(Titel)s %(Version)s' % s
                    tabelle.Cells(2,4).Value = titel
                    tabelle.Cells(3,4).Value = s['Copyright']
                    tabelle.Cells(4,4).Value = s['ProgURL']
                    tabelle.Range(tabelle.Cells(1,1), tabelle.Cells(len(wortliste),2)).Value=wortliste
                else:
                    self.warnung(s['ErrExport'], s['ErrNoFreqList'])
            except:
                self.warnung(s['ErrExport'], s['ErrExcel'])


    def export2csv(self):
        try:
            wortliste = self.freqliste.get(0, END)
            wortliste = [(a.strip(), b.strip()) for (a, b) in wortliste]
            inhalt = StringIO.StringIO()

            for x in wortliste:
                inhalt.write( '%s, %s\n' % (x[0], x[1]) )
            inhalt = inhalt.getvalue()
            inhalt = inhalt.encode('utf_8', 'replace')
            d = tkFileDialog.asksaveasfile(defaultextension='.csv', initialdir=cfg['KorpDir'])
            d.write(inhalt)
            d.close()
            self.status.set(s['StatusExpFreq'])
        except:
            self.warnung(s['ErrExport'], s['ErrExpFreq'])


    def export_text_graph2csv(self):
        textGraphs = self.korpus.textGraph
        dd = tkFileDialog.askdirectory(initialdir=cfg['KorpDir'])
        for f,tg in textGraphs:
            content = StringIO.StringIO()
            try:
                kn = tg.node.keys()
                kn.sort()
                wn = tg.node_property.keys()
                content.write('node,'+','.join(wn) + '\n')
                for k in kn:
                    content.write(k)#k.encode('utf-8')
                    for w in wn:
                        content.write(',%.3f' % tg.node[k][w])
                    content.write('\n')

                content = content.getvalue()
                content = content.encode(self.dateiart.get(), 'replace')
                d = open(dd+'/'+os.path.split(f)[-1][:245]+'_node.csv','w')
                d.write(content)
                d.close()
                self.status.set(s['TGExportNodeSuccess'])
            except(ArithmeticError):
                self.warnung(s['ErrExport'], s['TGExportError'])

            try:
                content = StringIO.StringIO()
                ke = tg.edges()
                ke.sort()
                we = tg.edge_property.keys()
                content.write('word1,word2,'+','.join(we) + '\n')
                for k in ke:
                    content.write(k[0]+','+k[1])
                    for w in we:
                        content.write(',%.3f' % tg.edge[k[0]][k[1]][w])
                    content.write('\n')

                content = content.getvalue()
                content = content.encode(self.dateiart.get(), 'replace')
                d = open(dd+'/'+ os.path.split(f)[-1][:245]+'_edge.csv','w')
                d.write(content)
                d.close()
                self.status.set(s['TGExportEdgeSuccess'])
            except(ArithmeticError):
                self.warnung(s['ErrExport'], s['TGExportError'])

    def export_text_graph2excel(self):
        return
        if len(wortliste) > 65000:
            self.warnung(s['ErrExport'], s['ErrExcel65K'] % len(wortliste))
        else:
            try:
                if len(wortliste) > 1:
                    wortliste = [(a.strip(), b.strip()) for (a, b) in wortliste]
                    meinXL = Dispatch("Excel.Application")
                    meinXL.Visible = 1
                    meinXL.Workbooks.Add()
                    tabelle = meinXL.Workbooks(1).Sheets(1)
                    tabelle.Cells(2,1).Value = 'ACHTUNG - ATTENTION'
                    tabelle.Cells(3,1).Value = 'Dies kann dauern...'
                    tabelle.Cells(4,1).Value = 'This can take a while...'
                    titel = '%(Titel)s %(Version)s' % s
                    tabelle.Cells(2,4).Value = titel
                    tabelle.Cells(3,4).Value = s['Copyright']
                    tabelle.Cells(4,4).Value = s['ProgURL']
                    tabelle.Range(tabelle.Cells(1,1), tabelle.Cells(len(wortliste),2)).Value=wortliste
                else:
                    self.warnung(s['ErrExport'], s['ErrNoFreqList'])
            except:
                self.warnung(s['ErrExport'], s['ErrExcel'])

    def export2word(self):
        konkliste = self.konkliste.get(0,END)
        if len(konkliste) > 0:
            inhalt = "%(Titel)s %(Version)s\n%(Copyright)s\n(%(ExportHinweis)s)\n\n" % s
            inhalt = inhalt + '\n\n'.join(konkliste)
            try:
                # Word starten, leeres Document öffnen, Text einfügen
                meinWord = Dispatch('Word.Application')
                meinWord.Visible = 1
                meinDoc = meinWord.Documents.Add()
                meinWo = meinDoc.Range(0,0)
                meinWo.InsertBefore(inhalt)
            except:
                self.warnung(s['ErrExport'], s['ErrWord'])
        else:
            self.warnung(s['ErrExport'], s['ErrNoKonkList'])


    def export2txt(self):
        konkliste = self.konkliste.get(0,END)
        if len(konkliste) > 1:
            inhalt = "%(Titel)s %(Version)s\n%(Copyright)s\n(%(ExportHinweis)s)\n\n" % s
            inhalt = inhalt + '\n'.join(konkliste)
            try:
                inhalt = inhalt.encode('utf_8', 'replace')
                d = tkFileDialog.asksaveasfile(defaultextension='.txt', initialdir=cfg['KorpDir'])
                d.write(inhalt)
                d.close()
                self.status.set(s['StatusExpKonk'])
            except:
                self.warnung(s['ErrExport'], s['ErrExpKonk'])


    def copy2clipboard(self):
        self.root.clipboard_clear()
        txt = ''

        if self.tabPages.GetActivePage() == s['ZitatTab']:
            try:
                txt = self.zitat.get(SEL_FIRST, SEL_LAST)
            except TclError, details:
                self.warnung(titel=s['Error'], text=s['ErrSelect'])
        elif self.tabPages.GetActivePage() == s['ConcTab']:
            txt = self.konkliste.get(self.konkliste.curselection())[0]
        elif self.tabPages.GetActivePage() == s['FormenTab']:
            a,b = self.freqliste.get(self.freqliste.curselection())
            a = a.strip()
            b = b.strip()
            txt = a + ' - ' + b
        elif self.tabPages.GetActivePage() == s['KorpusTab']:
            l = []
            for i in self.datliste.curselection():
                l.append(self.datliste.get(i))
                txt = '\n'.join(l)

        self.root.clipboard_append(txt)
        self.status.set(s['StatusClip'])
        # self.info('', txt)

    def busyCursorOn(self):
        # Cursor auf 'busy/wait'
        self.root.config(cursor='watch')
        self.root.update_idletasks()
        self.root.update()

    def busyCursorOff(self):
        # Cursor auf 'normal'
        self.root.config(cursor='')
        self.root.update_idletasks()
        self.root.update()

    def statusAktualisieren(self, event=''):
        if self.tabPages.GetActivePage() == s['FormenTab']:
            if self.korpus != None:
                self.status.set( s['StatusFormen'] % (self.freqliste.size(), self.korpus.anzahlTokens) )
            else:
                self.status.set(' ')
        if self.tabPages.GetActivePage() == s['ConcTab']:
            self.status.set( s['StatusTreffer'] % self.konkliste.size() )
        if self.tabPages.GetActivePage() == s['Korpus']:
            if self.korpus != None:
                self.status.set( s['StatusKorpDat'] % (self.korpus.getDbName(), self.dateiart.get()) )
            else:
                self.status.set( s['Willkommen'] )

    def info(self, titel='', text=''):
        tkMessageBox.showinfo(titel, text)

    def warnung(self, titel='', text=''):
        tkMessageBox.showwarning(titel, text)

    def sprachwarnung(self):
        self.optionen_speichern()
        self.warnung(s['SpracheAendern'], s['SpracheInfo'])

    def about(self):
        # self.info('', self.tabPages.GetActivePage())
        info = "%(Titel)s %(Version)s\n(%(VersionDatum)s)\n\n%(Copyright)s\n%(eMail)s\n\n%(ProgURL)s  \n\n%(ProgInfo)s" % s
        self.info('TextSTAT', info)

    def regex_hilfe(self):
        try:
            webbrowser.open("http://docs.python.org/lib/re-syntax.html")
        except:
            self.warnung(titel=s['Error'], text=s['ErrFileOpen'])

    def ende(self):
        self.optionen_speichern()
        if self.korpus != None and self.korpus.dbGeaendert == 1: 
            # self.info(text= str(self.korpus.dbGeaendert))
            m = tkMessageBox.Message(
                        title=s['ProgBeenden'],
                        message=s['AbfrageEnde'],
                        icon=tkMessageBox.QUESTION,
                        type=tkMessageBox.YESNOCANCEL)
            reply = m.show()
            if reply == 'yes':
                self.korpus_save()
                self.root.destroy()
                self.root.quit()
            elif reply == 'no':
                self.root.destroy()
                self.root.quit()
            else:
                pass
        else:
            self.root.destroy()
            self.root.quit()



if __name__ == '__main__':

    app = GUI(root)
    root.mainloop()
