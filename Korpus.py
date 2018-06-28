#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path, cPickle, re
import Web2Korpus, News2Korpus, ConvertText
import locale
import text_graph
locale.setlocale(locale.LC_CTYPE, '')     # LC_CTYPE beeinflusst String-Operationen
locale.setlocale(locale.LC_COLLATE, '')   # LC_COLLATE beeinflusst das Sortier-Verhalten


class Korpus:
    def __init__(self, master=None):
        self.master = master
        self.db = None
        self.dbFile = None
        self.wordFreq = None
        self.anzahlTokens = 0
        self.suchKonk = None
        self.konkResultat = None
        self.LkonkResultat = None
        self.zitatDatei = None
        self.dbGeaendert = 0
        self.textGraph = None

    def newDb(self, ff):
        self.dbFile = ff
        self.db = {}
        f = open(self.dbFile, 'wb')
        cPickle.dump(self.db, f, 2)
        f.close() 

    def openDb(self, ff):
        """DB anlegen bzw. öffnen""" 
        try:
            ff = os.path.normpath(ff)
            f = open(ff, 'rb')
            self.db = cPickle.load(f)
            f.close()
            self.dbFile = ff
            # Testen, ob dies vielleicht ein altes TextSTAT 1.5-Korpus ist
            # versuchen zu importieren
            if isinstance(self.db, list):
                self.db = {}
                self.importOldKorpus(ff)
        except:
            pass
                                 
        
    def addDb(self, ff):
        """Korpus zu DB hinzufügen"""
        ff = os.path.normpath(ff)
        f = open(ff, 'rb')
        x = cPickle.load(f)
        f.close() 
        try:
            for k in x.keys():
                self.db[k] = x[k]
        except:
            # Wenn was schiefgeht ist es ja vielleicht ein altes Korpus
            if isinstance(x, list):
                del x
                self.importOldKorpus(ff)
                
        self.clearVars()
                     

    def saveDb(self):
        """DB schließen""" 
        # Wir speichern binär, Protokoll 2 (neu in Python 2.3)
        f = open(self.dbFile, 'wb')
        cPickle.dump(self.db, f, 2)
        f.close() 
        self.dbGeaendert = 0
        
    def getDbName(self):
        """Gibt Dateinamen des Korpus zurück"""
        return os.path.split(self.dbFile)[1]
        
    def getDbPath(self):
        """Gibt Dateipfad zurück"""
        return self.dbFile

    def getDbKeys(self):
        """Gibt sortierte Liste der Keys zurück (Strings)"""
        k = self.db.keys()
        k.sort()
        return k

    def getDbFileNames(self):
        """Gibt sortierte Liste der Filenamen zurück (Unicode)"""
        l = []
        for k in self.db.keys():
            l.append(self.db[k]['path'])
        l.sort()
        return l
        
    def getDbSize(self):
        """Gibt Summe der Dateigrößen zurück"""
        dbSize = 0
        for k in self.db.keys():
            dbSize = dbSize + len(self.db[k]['file'])
        return dbSize

    def getDbFile(self, k):
        """Lesbarerer Shortcut zum Ansprechen einer einzelnen Datei im Korpus"""
        return self.db[k]

    def countDbFiles(self):
        """Gibt Anzahl der Dateien im Korpus zurück"""
        return len(self.db.keys())       
        

    def addDbFiles(self, files, codepage):
        """Fügt Textfiles zum Korpus hinzu"""
        for f in files:
            # wegen Problemen beim Öffnen, jetzt erst einmal den Datipfad 'normalisieren'
            f = os.path.normpath(f)
            
            # Word-File?? sind wir unter Windows?
            # dann versuchen wir halt mal das zu lesen           
            if f[-4:] == '.doc' or f[-4:] == '.rtf' or f[-5:] == '.docx':
                try:
                    word = ConvertText.ReadWord(f)
                    ff = word.getData()
                except:
                    continue
            
            # OpenOffice-File??         
            elif f[-4:] == '.sxw' or f[-4:] == '.odt':

                oo = ConvertText.ReadOO(f)
                ff = oo.getData()
                ff = unicode(ff, 'utf-8', 'replace')
                    
            else:
                ff = open(f).read()
                # So, jetzt machen wir aus dem File ein Unicode-File
                ff = unicode(ff, codepage, 'replace')
                # Scripts und Styledefinitionen rauswerfen
                ff = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", ff)
                                
                # Haben wir es mit einem HTML-File zu tun? Dann HTML weg...
                if '.htm' in f:
                    st = Web2Korpus.HTMLStripper()
                    st.feed(ff)
                    st.close()
                    ff = st.gettext()
    
                               
            element = {'path':f, 'file':ff}
 
            self.db[f] = element
            
        self.clearVars()


    def addHTMLFiles(self, url, anzahl, codepage, basis):
        d = Web2Korpus.Web2Korpus(master=self.master, url=url, anzahl=anzahl, basis=basis, codepage=codepage)
        data = d.getData()
        for f in data.keys():
            # Umwandlung in Unicode findet jetzt in Web2Korpus statt
            # ff = unicode(data[f], codepage, 'replace')
            ff = data[f]
            element = {'path':f, 'file':ff}
            self.db[f] = element
        self.clearVars()


    def addNewsFiles(self, server='', gruppe='', anzahl=50, zitate=1, codepage='latin-1'):
        d = News2Korpus.News2Korpus(master=self.master, server=server, gruppe=gruppe, anzahl=anzahl, zitate=zitate)
        data = d.getData()
        for f in data.keys():
            ff = unicode(data[f], codepage, 'replace')
            element = {'path':f, 'file':ff}
            self.db[f] = element
        self.clearVars()

        
    def importOldKorpus(self, korpName):
        korpFile = open(korpName)
        dateien = cPickle.load(korpFile)
        korpFile.close()
        for dat in dateien:
            f = dat[0]
            ff = dat[1]
            element = {'path':f, 'file':ff}
            key = f.encode('utf-8', 'replace')
            self.db[key] = element
        self.clearVars()     

        
    def delDbFiles(self, files):
        """Entfernt Dateien aus dem Korpus"""
        for f in files:
            del self.db[f] 
        self.clearVars()

     
    def clearVars(self):
        # Frequenz- und Konkordanzliste löschen
        self.wordFreq = None
        self.anzahlTokens = 0
        self.konkResultat = None
        self.LkonkResultat = None
        self.dbGeaendert = 1


    def dbWordFreq(self):
        """Hilfsfunktion für getWordFreq(): erstellt das Dict mit Wortfrequenzen"""
        self.wordFreq = {}
        self.wordFreqKlein = {}
        # woerter = re.compile(r"[\w-]+", re.U | re.M)
        woerter = re.compile(r"\b([\w'-·]+)\b", re.U | re.M)
        dateien = self.getDbKeys()
        z = 0
        self.anzahlTokens = 0
        for dat in dateien:
            allewoerter = woerter.findall(self.db[dat]['file'])
            # Was jetzt kommt ist ein fürchterlicher Workaround; wir brauchen das,  
            # damit Unicode richtig alphabetisch sortiert wird (wie Locale es verlangt)
            # allewoerter = [x + ' ' for x in allewoerter]
            # >>> 08/2008: Workaround ist anscheinend nicht mehr nötig...
            
            self.anzahlTokens = self.anzahlTokens + len(allewoerter)
            for wort in allewoerter:
                self.wordFreq[wort] = self.wordFreq.get(wort, 0) + 1
                # und jetzt das ganze nochmal mit Kleinschreibung
                wort = wort.lower()
                self.wordFreqKlein[wort] = self.wordFreqKlein.get(wort, 0) + 1
                
            # Fortschritt in Statusbar anzeigen
            z = z + 1
            self.master.status.progress.updateProgress(newValue=z, newMax=len(dateien))


    def getWordFreq(self, sort='freq', grossklein=0, minFreq=0, maxFreq=0, suchFreq=''):
        """Gibt Wortfrequenzliste zurück; Basis dafür ist das Dict self.wordFreq """
        if self.wordFreq == None:
            self.dbWordFreq()

        freqListe = [] 

        if suchFreq != '':
        # wenn ein bestimmtes Suchwort angegeben ist.
            muster = re.compile(suchFreq, re.U | re.I)
            for wort in self.wordFreq.keys():
                if muster.search(wort) != None:
                    freqListe.append([wort, self.wordFreq[wort]])
              
        else:
        # wenn kein Suchwort da ist (also normalerweise...)
            try:
                minFreq = int(minFreq)
            except:
                minFreq = 0
            try:
                maxFreq = int(maxFreq)
            except:
                maxFreq = 0
                
            if grossklein == 1:
                freqDict = self.wordFreqKlein
            else:
                freqDict = self.wordFreq
                
            if minFreq ==0 and maxFreq==0:
                for k, v in freqDict.items():
                    freqListe.append([k, v])
            else:
                for k, v in freqDict.items():
                    if (maxFreq == 0 and v >= minFreq) or (v >= minFreq and v <= maxFreq):
                        freqListe.append([k, v])

        # Wir sortieren zunächst mal (default) alphabetisch
        def sortDeutsch(a,b):
            return locale.strcoll(a[0], b[0])
        freqListe.sort(sortDeutsch) 
    
        if sort == 'alpha':
            # explizit (noch einmal) alphabetisch
            freqListe.sort(sortDeutsch)
           
        elif sort == 'retro':
            # retrograde
            def sortRetro(a, b):
                a, b = list(a[0]), list(b[0])
                a.reverse()
                b.reverse()
                a = ''.join(a)
                b = ''.join(b)
                return locale.strcoll(a,b)
                # return cmp(a, b)
            freqListe.sort(sortRetro)

        else:
            # Default: absteigend nach Frequenz
            def sortFrequenz(a, b):
                return cmp(b[1], a[1])
            freqListe.sort(sortFrequenz)

        # Progressbar zurücksetzen                
        self.master.status.progress.updateProgress(0)

        return freqListe



    def dbWordConc(self, pattern='', ganzWort=0, grossklein=0, cL=50, cR=50):     
      
        if ganzWort == 1:
            # nur ganze Wörter
            suchmuster = r"\b%s\b" % self.suchKonk
        else:
            suchmuster = self.suchKonk
            
        if grossklein == 1:
            # Großschreibung ignorieren
            muster = re.compile(suchmuster, re.U | re.S | re.I)
        else:
            muster = re.compile(suchmuster, re.U | re.S)
                    
        self.konkResultat = []
        dateien = self.getDbKeys()
        z=0
        for dat in dateien:
            datei = self.db[dat]['file']
            
            pos = 0
            while 1:
                res = muster.search(datei, pos)
                if res == None:
                    break
    
                # ab pos weitersuchen, also pos erhöhen
                pos = res.start() + 1
    
                # Kontext festlegen
                anfang = res.start() - cL
                ende = res.end() + cR

                if anfang < 0:
                    anfang = 0
                if ende > len(datei):
                    ende = len(datei)
    
                # Gefundenen String ins Resultat (besteht aus drei Teilen) und auch den Dateinamen
                konk = [datei[anfang:res.start()], datei[res.start():res.end()], datei[res.end():ende]]
                self.konkResultat.append(['', konk, dat])            
              
            # Fortschritt in Statusbar anzeigen
            z = z + 1
            self.master.status.progress.updateProgress(newValue=z, newMax=len(dateien))
        # Progressbar zurücksetzen                
        self.master.status.progress.updateProgress(0)


    def getWordConc(self, pattern='', ganzWort=0, grossklein=0, cL='50', cR='50', sort='', markKonk=0):
        if pattern != '':
            self.suchKonk = pattern  
            
        try:
            cL = int(cL)
            cR = int(cR)
        except:
            cL = 50
            cR = 50
            
        # Hier könnte man eine Bedingung einbauen, so dass nicht immer alle
        # Files durchsucht werden müssen...
        self.dbWordConc(pattern=pattern, ganzWort=ganzWort, grossklein=grossklein, cL=cL, cR=cR)

        z = 0
        for k in range(len(self.konkResultat)):
            konk = self.konkResultat[k][1]
            if markKonk == 1:
                x = konk[1].upper()
                anzeigeString = konk[0].rjust(cL) + x + konk[2]
            else:
                anzeigeString = konk[0].rjust(cL) + konk[1] + konk[2]
            # Newline rauswerfen
            anzeigeString = anzeigeString.replace('\n', ' ')
            # Format: [Konk für Anzeige, Original Konk (Tuple), Dateiname]
            self.konkResultat[k][0] = anzeigeString
                
            # Fortschritt in Statusbar anzeigen
            z = z + 1
            self.master.status.progress.updateProgress(newValue=z, newMax=len(self.konkResultat))

        # Sortieren  
        def sort_konk(a, b):
            # Wir nehmen das Original zum sortieren (also das Tuple)
            a = a[1]
            b = b[1]
            if sort == 'rechts':
                return locale.strcoll(a[2], b[2])
            elif sort == 'links':
                a, b = a[0].split(), b[0].split()
                if len(a) == 0: a.insert(0, ' ')
                if len(b) == 0: b.insert(0, ' ')
                return locale.strcoll(a[-1], b[-1])
            else:            
                return locale.strcoll(a[1], b[1])
      
        
        self.konkResultat.sort(sort_konk)
        # Progressbar zurücksetzen                
        self.master.status.progress.updateProgress(0)
        
        return self.konkResultat
            

    def getContext(self, i, contextL=100, contextR=100):
        konk = self.konkResultat[i]
        konkordanz = ''.join(konk[1])
        self.zitatDatei = konk[2]
        datei = self.db[self.zitatDatei]['file']
        stelleL = datei.find(konkordanz)
        stelleR = stelleL + len(konkordanz)
        
        anfang = stelleL - contextL
        ende = stelleR + contextR

        # Leerzeichen suchen, damit nur ganze Wörter gezeigt werden
        if anfang < 0: 
            anfang = 0
        while datei[anfang] != ' ':
            anfang = anfang - 1
            if anfang <= 0:
                anfang = 0
                break
        if ende > len(datei): 
            ende = len(datei)-1
        while datei[ende] != ' ':
            ende = ende + 1
            if ende >= len(datei):
                ende = len(datei)
                break

        res = [datei[anfang:stelleL], datei[stelleL:stelleR], datei[stelleR:ende]]
        return res

    def getWordLConc(self, pattern='', ganzWort=0, grossklein=0, cL='5', cR='5', sort='', markKonk=0,separate=' ',sepBy='gaps'):
        if pattern != '':
            self.suchKonk = pattern  
            
        try:
            cL = int(cL)
            cR = int(cR)
        except:
            cL = 5
            cR = 5
        
        if sepBy==0:
            sepBy=False
        else:
            sepBy=True
        if not isinstance(separate,str) or separate=='':
            if sepBy:
                separate=re.compile('\w+')
            else:
                separate=re.compile('\W+')
        # Hier könnte man eine Bedingung einbauen, so dass nicht immer alle
        # Files durchsucht werden müssen...
        self.dbWordLConc(ganzWort=ganzWort, grossklein=grossklein, cL=cL, cR=cR,separate=separate,sepByWords=sepBy)

        z = 0
        for k in range(len(self.LkonkResultat)):
            konk = self.LkonkResultat[k][1]
            if markKonk == 1:
                x = konk[1].upper()
                anzeigeString = ';'.join(konk[0]).rjust(cL*12) +' ; '+ x +' ; '+ ';'.join(konk[2])
            else:
                anzeigeString = ';'.join(konk[0]).rjust(cL*12) +' ; '+ konk[1] +' ; '+ ';'.join(konk[2])
            # Newline rauswerfen
            anzeigeString = anzeigeString.replace('\n', ' ')
            # Format: [Konk für Anzeige, Original Konk (Tuple), Dateiname]
            self.LkonkResultat[k][0] = anzeigeString
            
            # Fortschritt in Statusbar anzeigen
            z = z + 1
            self.master.status.progress.updateProgress(newValue=z, newMax=len(self.LkonkResultat))

        def sort_konk(a, b):
            # Wir nehmen das Original zum sortieren (also das Tuple)
            a = a[1]
            b = b[1]
            if sort == 'rechts':
                return locale.strcoll(a[2], b[2])
            elif sort == 'links':
                a, b = a[0].split(), b[0].split()
                if len(a) == 0: a.insert(0, ' ')
                if len(b) == 0: b.insert(0, ' ')
                return locale.strcoll(a[-1], b[-1])
            else:            
                return locale.strcoll(a[1], b[1])
      
        
        self.LkonkResultat.sort(sort_konk)
        # Progressbar zurücksetzen                
        self.master.status.progress.updateProgress(0)
        
        return self.LkonkResultat

    def dbWordLConc(self,ganzWort=0, grossklein=0, cL=5, cR=5,separate=' ',sepByWords=False):
        if ganzWort == 1:
            # nur ganze Wörter
            suchmuster = r"\b%s\b" % self.suchKonk
        else:
            suchmuster = self.suchKonk
            
        if grossklein == 1:
            # Großschreibung ignorieren
            muster = re.compile(suchmuster, re.U | re.S | re.I)
        else:
            muster = re.compile(suchmuster, re.U | re.S)

        separate=re.compile(separate)
        
        self.LkonkResultat = []
        dateien = self.getDbKeys()
        for dat in dateien:
            datei = self.db[dat]['file']
            LConc=concordance(muster,dat,cL,cR,separate=separate,sepByWords=sepByWords)
            LConc._listFull_parsing(datei)
            self.LkonkResultat+=LConc.storage

    def dbTextGraph(self, search_query=None, stop_words=('-')):
        self.textGraph = []
        dateien = self.getDbKeys()
        i=0
        for dat in dateien:
            datei = self.db[dat]['file']
            tg = text_graph.text_graph(datei, 0, stop_words, word_pattern=search_query)
            self.textGraph.append((dat, tg,))
            self.master.status.progress.updateProgress(newValue=i, newMax=len(dateien))
            i+=1
        if (self.dbFile):
            f = open(self.dbFile+'_tg', 'wb')
            cPickle.dump(self.textGraph, f, 2)
            f.close()
        self.master.status.progress.updateProgress(0)

    def getTextGraph(self):
        f = open(self.dbFile+'_tg', 'rb')
        self.textGraph = cPickle.load(f)
        f.close()




class concordance:
    import re
    endFlag=0
    buffer=''
    listBuffer=['']
    sepByWords=False    #split by separatings(F) or by wordpattern(T)
    lenByLetters=False  #context length is by letters(T) or by words(F)
    sourceName=None
    storage='./concordance.csv'

    def __init__(s,key,sourceName,lenL=17,lenR=17,saveTo='list',separate=' ',sepByWords=False, lenByLetters=False):
        try:
            if not(isinstance(key,str)):
                key.match('')
        except AttributeError:
            print('Need str or regex key!')
            raise(AttributeError)# rex is not an re
        else:
            s.key=key
        s.lenR=lenR
        s.lenL=lenL
        s.sourceName=sourceName
        s.saveTo=saveTo
        try:
            if not(isinstance(separate,str)):
                separate.split('')
        except AttributeError:
            print('Need str or regex key!')
            raise(AttributeError)# rex is not an re
        else:
            s.separate=separate
        if(saveTo == 'list'):
            s.storage=[]
        if(saveTo == 'file'):
            s.storage='./concordance.csv'
        s.startFlag = True
        s.sepByWords=sepByWords
        s.lenByLetters=lenByLetters

    def add_record(s,record):
        if(s.saveTo=='list'):
            s.storage.append([record,tuple(record),s.sourceName])
        if(s.saveTo=='file'):
            with open(s.storage,mode='ab') as fstor:
                fstor.write(record)

    def storageReset(s):
        if(s.saveTo=='list'):
            s.storage=[]
        if(s.saveTo=='file'):
            with open(s.storage,mode='wb') as fstor:
                fstor.write('')
    
    def check_word(s,word):
        if(isinstance(s.key,str)):
            return s.key==word
        else:
            return bool(s.key.match(word))
        
    def split(s,string,noVoidStr=0):
        if s.sepByWords:
            return s.separate.findall(string)
        else:
            if(string==''):
                return []
            if(isinstance(s.separate,str)):
                return string.split(s.separate)
            else:
                res=s.separate.split(string)
                if(noVoidStr):
                    return [res[i] for i in range(len(res)) if res[i]!='']#or i==0]
                else:
                    return [res[i] for i in range(len(res)) if res[i]!='' or i==(len(res)-1) ]#or i==0]

    def _len(s,string):
        if(s.lenByLetters):
            return len(string)
        else:
            return len(s.split(string))

    def listFull_parsing(s,string):
        words = s.split(string)
        for wi in range(len(words)):
            if(s.check_word(words[wi])):
                k=wi-s.lenL#int(((wi-s.length)+abs(wi-s.length))/2)
                if(k<=0):k=0
                record = [words[k:wi], words[wi],words[wi+1:s.lenR+wi+1]]
                s.add_record(record)
        return s.storage

    def strFull_parsing(s,string):
        pos = 0
        while 1:
            res = s.key.search(string, pos)
            if res == None:
                break
            
            pos = res.start() + 1
            
            # Kontext festlegen
            begin = res.start() - s.lenL
            ende = res.end() + s.lenR
            
            if begin < 0:
                begin = 0
            if ende > len(string):
                ende = len(string)
            
            # Gefundenen String ins Resultat (besteht aus drei Teilen) und auch den Dateinamen
            konk = [string[begin:res.start()], string[res.start():res.end()], string[res.end():ende]]
            s.add_record(konk)
        return s.storage
    
    def _listFull_parsing(s,string):
        pos = 0
        cL=s.lenL*12
        cR=s.lenR*12
        while 1:
            res = s.key.search(string, pos)
            if res == None:
                break
            
            pos = res.start() + 1
            
            # Kontext festlegen
            begin = res.start() - cL
            ende = res.end() + cR
            
            if begin < 0:
                begin = 0
            if ende > len(string):
                ende = len(string)
            pos1=0
            LKeyGapPos=res.start()
            _str=string[begin:pos]
            while 1:                        #find last separate symbol before keyword, cause ..._prefxKWORDpstfx_... is valid
                _r = s.separate.search(_str,pos1)
                if _r==None:
                    break
                if s.sepByWords:
                    LKeyGapPos = _r.start()
                else:
                    LKeyGapPos = _r.end()
                pos1 = _r.start()+1
            LKeyGapPos=LKeyGapPos+begin
            
            RKeyGapPos=s.separate.search(string[begin:ende],res.end()-begin)
            if RKeyGapPos==None:
                if ende==len(string):
                    RKeyGapPos=ende
                else:
                    cR+=12
                    pos=0
                    s.storageReset()
                    continue
            else:
                RKeyGapPos=RKeyGapPos.start()+begin
            
            if(not s.check_word(string[LKeyGapPos:RKeyGapPos])):
                continue
            # Gefundenen String ins Resultat (besteht aus drei Teilen) und auch den Dateinamen
            #print('b=%i, LKGP=%i, RGKP=%i, e=%i'%(begin,LKeyGapPos,RKeyGapPos,ende))
            listLeftConc=s.split(string[begin:LKeyGapPos],1)
            if len(listLeftConc)<=s.lenL and pos>=cL:#усдлвие что это начло текста и перед ним не может хватать элементов:
                cL+=(s.lenL-len(listLeftConc))*12+12
                pos=0
                s.storageReset()
                continue
            listRightConc=s.split(string[RKeyGapPos:ende],1)
            if len(listRightConc)<=s.lenR and pos<=len(string)-cR:
                cR+=(s.lenR-len(listRightConc))*12+12
                pos=0
                s.storageReset()
                continue
            konk = [listLeftConc[-s.lenL:], string[LKeyGapPos:RKeyGapPos], listRightConc[:s.lenR]]
            s.add_record(konk)
        return s.storage
    
    
    def listStream_parsing(s,stream_string):
        listString = s.listBuffer[:-1]+s.split(s.listBuffer[-1]+stream_string)
        lastElement=listString[-1]
        listString=listString[:-1]
        if(len(listString)<=s.lenR+s.lenL and not s.lenByLetters):
            s.listBuffer=listString+[lastElement]
        else:
            startIndexChecking=len(s.listBuffer)-s.lenL-1
            if(startIndexChecking<0 or s.startFlag): 
                startIndexChecking=0
                s.startFlag=False
            if(s.endFlag):
                startIndexChecking-=s.lenR
            endIndexChecking=len(listString)#-s.lenR-1
            for wi in range(startIndexChecking,endIndexChecking):
                if(s.check_word(listString[wi])):# and (s.lenR+wi+1)<len(listString)):
                    if(wi<endIndexChecking-s.lenR+s.endFlag):
                        k=wi-s.lenL
                        if(k<=0):k=0
                        record = [listString[k:wi], listString[wi],listString[wi+1:s.lenR+wi+1]]
                        s.add_record(record)
            s.listBuffer=listString[-(s.lenL+1+s.lenR):]+[lastElement]
        return s.storage
    
    def closeConc(s):
        s.listBuffer+=['']*s.lenR;
        s.endFlag=1
        s.listStream_parsing('')
        for j in range(-len(s.listBuffer),0):
            s.storage[j][0][2]=[i for i in s.storage[j][1][2] if i!='']
        return s.storage

