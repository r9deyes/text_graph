#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# TextSTAT - Simples Text Analyse Tool
# 
# Copyright (c) 2001/2012, Matthias Hüning <matthias.huening@fu-berlin.de>
# All rights reserved.
#
# Sprachoptionen für TextSTAT
#
#   Russian local and text graph module changes
# by Daniil Andriyanov, 2016-2018 <8595dan@gmail.com>
#

##############################
# ein paar globale Variablen
Version = u"2.9c"
VersionDatum = u"20/02/2014"
Copyright = u"(c) Matthias Hüning 2000/2014\nDaniil Andriyanov 2018"
eMail = u"<matthias.huening@fu-berlin.de>"
ProgURL = u"http://neon.niederlandistik.fu-berlin.de/textstat/"


##############################
########### Deutsch ##########
##############################

deutsch  = {
"Titel"         : u"TextSTAT",
"Titel_lang"    : u"TextSTAT (Simples Text Analyse Tool)",
"Version"       : Version,
"VersionDatum"  : u"Version vom %s" % VersionDatum,
"Copyright"     : Copyright,
"eMail"         : eMail,
"ProgURL"       : ProgURL,
"ProgInfo"      : u"TextSTAT ist freie Software.\nDer Autor übernimmt keinerlei Haftung.",

###### Menu #####
"Korpus"        : u"Korpus",
"KorpusNew"     : u"Neues Korpus",
"KorpusOpen"    : u"Korpus öffnen",
"KorpusHinzu"   : u"Korpus hinzufügen",
"KorpusSave"    : u"Korpus speichern",
"KorpusSaveAs"  : u"Speichern unter",
"KorpusDel"     : u"Korpus löschen",
"LetzteKorpora" : u"Letzte Korpora",

"DateiHinzu"    : u"Datei von Festplatte hinzufügen",
"WebHinzu"      : u"Web-Datei hinzufügen",
"NewsHinzu"     : u"Newsgroup-Beiträge hinzufügen",
"DateiWeg"      : u"Datei(en) entfernen",

"OptSave"       : u"Optionen speichern",
"Exit"          : u"Beenden",

"ImpEx"         : u"Exportieren",
"Ex2csv"        : u"Frequenzliste > CSV-Datei",
"Ex2txt"        : u"Konkordanzen > TXT-Datei",
"Ex2excel"      : u"Frequenzliste > MS Excel",
"Ex2word"       : u"Konkordanzen > MS Word",
"ImpKorpus"     : u"Korpus importieren (TextSTAT 1.x)",

"Sprache"       : u"Sprache",
"CodePage"      : u"Datei-Kodierung",
"Hilfe"         : u" ? ",
"RegExpHelp"    : u"Regular Expressions - Hilfe",
"History"       : u"Änderungsprotokoll",
"License"       : u"Lizenz",
"Willkommen"    : u" Willkommen bei TextSTAT",


##### Toolbar #####
"KorpusNew2"    : u"Neues Korpus anlegen",
"KorpusOpen2"   : u"Ein bestehendes Korpus öffnen",
"KorpusHinzu2"  : u"Bestehendes Korpus zu momentan geöffnetem Korpus hinzufügen",
"KorpusSave2"   : u"Das momentane Korpus speichern",
"KorpusDel2"    : u"Das Korpus wird definitiv gelöscht",
"WebHinzu2"     : u"HTML-Datei(en) aus Internet zum Korpus hinzufügen",
"DateiHinzu2"   : u"Datei(en) von Festplatte zum Korpus hinzufügen",
"DateiWeg2"     : u"Datei(en) aus Korpus löschen",
"FreqZeigen"    : u"Wortfrequenzen anzeigen",
"FreqZeigen2"   : u"Frequenz der einzelnen Wortformen im Korpus anzeigen",
"Kopieren"      : u"Kopieren (in Zwischenablage)",
"Kopieren2"     : u"Auswahl in Zwischenablage kopieren",
"Ex2excel2"     : u"Frequenzliste nach MS Excel exportieren",
"Ex2word2"      : u"Konkordanzen nach MS Word exportieren",
"Info"          : u"Info zu TextSTAT",
"Info2"         : u"Informationen zum Programm",

##### Tabs #####
"KorpusTab"     : u"Korpus", 
"FormenTab"     : u"Wortformen",
"ConcTab"       : u"Konkordanz",
"ZitatTab"      : u"Zitat",
"ClustNGramsTab": u"Cluster/N-Grams",
"CollocatesTab" : u"Collocates",
"LConcTab" : u"KWIDC",
"TextGraphTab": u"Graph model",

"KTinfo"        : u"TextSTAT \n\nBitte füllen Sie Ihr Korpus mit einigen Files bzw. öffnen Sie ein bestehendes TextSTAT-Korpus.",
"KTkopieren"    : u"Dateinamen kopieren",
"KTopen"        : u"Datei öffnen",
"KTdatinfo"     : u"Datei-Info",
"KTdatweg"      : u"Datei(en) entfernen",

"FTinfo"        : u"FREQUENZ \nder Wortformen (Token)",
"FTsortFreq"    : u"nach Frequenz sortieren",
"FTsortAlpha"   : u"alphabetisch sortieren",
"FTsortRetro"   : u"retrograde sortieren",
"FTminFreq"     : u"min. Frequenz",
"FTmaxFreq"     : u"max. Frequenz",
"FTignGross"    : u"Groß/klein ignorieren (A=a)",
"FTsuchFreq"    : u"Definiere Filter (String oder\nregulärer Ausdruck):",
"FTfreqliste"   : u"Frequenzliste",
"FTwortform"    : u"Wortform",
"FTfrequenz"    : u"Frequenz",
"FTkopieren"    : u"Kopieren",
"FTsuchKonk"    : u"Konkordanzen suchen",
"FTzeigInfo"    : u"mehr Informationen",
"FTformInfo"    : u"Korpus-Informationen\n\nKorpusgröße: %s Wörter (Tokens)\n\n%s verschiedene Formen (Types, Großschreibung berücksichtigt) bzw. \n%s Types (Großschreibung ignoriert)\n\nDie Form '%s' kommt %s Mal vor (= %.2f %%)",
"FTOptionen"    : u"Frequenz / Optionen",

"CTsuchen"      : u"Suchen",
"CTganzWort"    : u"nur ganze Wörter",
"CTignGross"    : u"Großschreibung ignorieren (A=a)",
"CTcontextL"    : u"Kontext links",
"CTcontextR"    : u"Kontext rechts",
"CTmarkSuch"    : u"Suchwort markieren",
"CTsortAlpha"   : u"alphabetisch",
"CTsortR"       : u"sortiert Kontext rechts",
"CTsortL"       : u"sortiert Kontext links",
"CTaktualisier" : u"Aktualisieren",
"CTmachQuery"   : u"Suchanfragen-Editor",
"CTkopieren"    : u"Kopieren",
"CTzeigZitat"   : u"Mehr Kontext zeigen",
"CTOptionen"    : u"Suchoptionen",

"ZTinfo"        : u"Text der Belegstelle",
"ZTkopieren"    : u"Kopieren",
"ZToeffnen"     : u"Datei öffnen",
"ZToeffnen2"    : u"\n(Doppelklick um Datei zu öffnen)\n",
"ZTInit"        : u"\n Doppelklick auf eine Zeile im Konkordanz-Tab zeigt hier dieselbe Zeile mit mehr Kontext.",
"ClTFreqR"      :u"FreqR",
"ClTFreqL"      :u"FreqL",
"ClTKoef"       :u"Koef",
"ClTToken"      :u"Token",

"LCTSeparate"   :u"Separator",
"LCTSepBy"      :u"Separate by words",
"Source"        :u"Source",

"Also"         :u"also",
"TGCompTextGraph"   :u"Graph Modell berechnen",
"TGLoadStatus"   :u"Text graph uploads from file...",
"TGSuccessLoadStatus"   : u"erfolgreich aus Datei hochgeladen",
"tf-idf"        : u"TF-IDF",
"TGExport"      : u"Export",
"TGGraphs"      : u"Frequency plots",
"TGmaxWord"     : u"max Word",
"TGmaxValue"        :u"max Value",
"TGminWord"     :u"min Word",
"TGminValue"    :u"min value",
"TGavgWord"     :u"avg Word",
"TGavgValue"    :u"avg value",
"TGVertecesCount"  :u"Verteces count:",
    "TGEdgesCount"  :u"Edges count:",
"TGExportError" :u"text graph export error...",
    "TGExportNodeSuccess"   :u"Text graph\'s nodes exported to CSV succesfully",
    "TGExportEdgeSuccess"   :u"Text graph\'s edges exported to CSV succesfully",
"TGdefaultStopWords"    :u",".join((u'в', u'но', u'и', u'на', u'из', u'то', u'к', u'а', u'что', u'-')),
"TGdefaultWordPattern"    :ur"[a-zA-ZА-ЯёЁ\-]+",
"TGStopWords"       :u"Stop-words",
"TGSWordPattern"        :u"Word pattern",
"TGComputeStatus"       :u"Compute text graph",
"TGStemming"            :u"Stemming",

##### Webdialog #####
"WDinfo"        : u"Fügen sie HTML-Seiten direkt aus dem Internet hinzu.\nBitte geben Sie eine URL ein:",
"WDfrageSeiten" : u"Wieviele Seiten möchten Sie in Ihr Korpus laden?",
"WDanzahl"      : u"Anzahl der Seiten, die heruntergeladen werden sollen",
"WDinSubdir"    : u"im angegebenen Subdirectory suchen",
"WDaufServer"   : u"auf dem ganzen Server suchen",
"WDok"          : u"Suchen",
"WDcancel"      : u"Schließen",

##### NewsDialog #####
"NDinfo"        : u"Newsgroup-Beiträge hinzufügen", 
"NDserver"      : u"News-Server",  
"NDgruppe"      : u"Newsgruppe", 
"NDanzahl"      : u"Anzahl der Beiträge", 
"NDzitWeg"      : u"Zitate entfernen", 
"NDok"          : u"Suchen",
"NDcancel"      : u"Schließen",

##### QueryDialog #####
"QDinfo"        : u"Hilfe bei der Erstellung komplexer Suchanfragen \nSie können hier auch Wildcards verwenden (* und ?)",
"QDsuchFelder"  : u"Suchbegriffe",
"QAusdruck1"    : u"erster Suchbegriff",
"QAusdruck2"    : u"zweiter Suchbegriff",
"QAbstand"      : u"Anzahl der Wörter zwischen den Suchbegriffen",
"QAbstandMin"   : u"mindestens und   ",
"QAbstandMax"   : u"höchstens",
"QmachAusdruck" : u"Suchanfrage erstellen",
"QDcancel"      : u"Schließen",


##### Fehler #####
"Error"         : u"Fehler",
"ErrKorpNew"    : u"Korpusdatei konnte nicht angelegt werden!",
"ErrKorpOpen"   : u"Korpus konnte nicht geöffnet werden!\nSind Sie sich sicher, dass es sich um eine TextSTAT-Korpusdatei handelt?",
"ErrKorpImp"    : u"Korpus konnte nicht importiert werden!",
"ErrNoKorp"     : u"Sie müssen zunächst ein neues Korpus anlegen bzw. ein bestehendes öffnen.",
"ErrKorpSave"   : u"Korpusdatei konnte nicht gespeichert werden!",
"ErrFileOpen"   : u"Fehler beim Öffnen der Datei!",
"ErrSelect"     : u"Sie haben nichts ausgewählt!",
"ErrOptSave"    : u"Optionen konnten nicht gespeichert werden",
"ErrExport"     : u"Export-Fehler",
"ErrNoFreqList" : u"Keine Wortfrequenzliste vorhanden",
"ErrNoKonkList" : u"Keine Konkordanzliste vorhanden",
"ErrExcel"      : u"MS Excel Fehler!\nSowohl die Python win32-Extensions als auch MS Excel müssen ordnungsgemäß installiert sein.",
"ErrExcel65K"   : u"Fehler! MS Excel kann nur 65500 Zeilen verarbeiten. \nEs sind aber %s Zeilen vorhanden.",
"ErrWord"       : u"MS Word Fehler!\nSowohl die Python win32-Extensions als auch MS Word müssen ordnungsgemäß installiert sein.",
"ErrExpFreq"    : u"Beim Speichern der Wortfrequenzliste ist etwas schief gegangen.",
"ErrExpKonk"    : u"Beim Speichern der Konkordanzliste ist etwas schief gegangen.",
"ErrWeb"        : u"Beim Laden der HTML-Files aus dem Internet ist etwas schief gegangen.",
"ErrNews"       : u"Beim Laden der Newsgroup-Berichte ist etwas schief gegangen.",
"ErrQuery"      : u"Sie haben keinen Suchbegriff eingegeben.",


##### Mitteilungen und Fragen #####
"AskSure"       : u"Sind Sie Sicher?",
"AskDelete"     : u"Wollen Sie wirklich %s loeschen?",
"StatusWeb"     : u"Es werden %s Files aus dem Internet hinzugeladen...",
"StatusNews"    : u"Es werden %s Newsgroup-Beiträge geladen und hinzugefügt...",
"DateiInfo"     : u"Datei-Informationen",
"DateiInfo2"    : u"Datei: %s\n\nPfad: %s\n\nGröße: %s\n",
"InfoText"      : u"TextSTAT\
\nNachdem Sie ein Korpus angelegt bzw. geöffnet haben, können Sie weitere Dateien hinzufügen \
oder auch wieder einige löschen. Markieren einer Datei und dann die rechte Maustaste drücken \
für weitere Optionen. \nSie können übrigens das Korpus auch als Ganzes speichern.\
\nZur Textanalyse haben Sie mehrere Möglichkeiten: \nUnter 'Wortformen' finden sie \
die Frequenzangaben zu einzelnen Wortformen. 'Konkordanz' zeigt KWIC-Konkordanzen \
(KeyWord in Context), 'Zitat' einen größeren Textzusammenhang.",

"StatusKorpImp" : u"Korpus wurde erfolgreich importiert.",
"StatusKorpSave": u"Korpus wurde gespeichert.",
"StatusFiles"   : u" %s Dateien | %s Bytes ",
"StatusKorpDat" : u" Korpus: %s  (Einstellung Dateikodierung: %s)",
"KodierungInfo" : u"Sie können jetzt Dateien hinzufügen.\n\nTextverarbeitungsdateien:\n- MS Word-Dateien ('.doc' bzw. '.docx')\n- OpenOffice-Dateien ('.odt bzw. .sxw')\n\nTextdateien:\n- ASCII/ANSI-Textdateien (meist '.txt')\n- HTML-Files (von der Festplatte oder direkt aus dem Internet)\n- Newsgroup-Beiträge (direkt aus dem Internet)\nBitte achten Sie bei den reinen Textdateien auf die richtige\nEinstellung der Dateikodierung.\nDie momentan eingestellte Dateikodierung ist: %s",
"StatusFormen"  : u" %s Wortformen/Types (%s Wörter/Tokens im Korpus)",
"StatusNoKorp"  : u" kein Korpus ",
"StatusSuchKonk": u"Suche Konkordanzen...",
"StatusTreffer" : u" %s Treffer ",
"StatusExpFreq" : u"Frequenzliste wurde exportiert.",
"StatusExpKonk" : u"Konkordanzliste wurde exportiert.",
"ExportHinweis" : u"Am besten wählen Sie zur Darstellung eine nicht-proportionale Schriftart (wie Courier New)",
"StatusClip"    : u"Auswahl wurde in Zwischenablage kopiert", 
"SpracheAendern": u"Sprache ändern",
"SpracheInfo"   : u"Sie müssen das Programm neu starten, um den Sprachwechsel zu aktivieren.\n\nYou have to restart TextSTAT to activate the language change.",
"ProgBeenden"   : u"TextSTAT beenden",
"AbfrageEnde"   : u"Das aktuelle Korpus wurde geändert.\nMöchten Sie es speichern, bevor TextSTAT beendet wird?",
"AbfrageSave"   : u"Das aktuelle Korpus wurde geändert.\nMöchten Sie es speichern, bevor Sie ein neues Korpus laden?",
}


###################################
########### Nederlands ############
###################################

nederlands  = {
"Titel"         : u"TextSTAT",
"Titel_lang"    : u"TextSTAT (Simpel Text Analyse Tool)",
"Version"       : Version,
"VersionDatum"  : u"Versie van %s" % VersionDatum,
"Copyright"     : Copyright,
"eMail"         : eMail,
"ProgURL"       : ProgURL,
"ProgInfo"      : u"TextSTAT is vrije software.\nDe auteur is niet aansprakelijk voor eventuele gebreken en fouten.",

###### Menu #####
"Korpus"        : u"Corpus",
"KorpusNew"     : u"Nieuw corpus",
"KorpusOpen"    : u"Corpus openen",
"KorpusHinzu"   : u"Corpus toevoegen",
"KorpusSave"    : u"Corpus opslaan",
"KorpusSaveAs"  : u"Bewaren als",
"KorpusDel"     : u"Corpus wissen",
"LetzteKorpora" : u"Laatste corpora",

"DateiHinzu"    : u"Bestand van harde schijf toevoegen",
"WebHinzu"      : u"Web-bestand toevoegen",
"NewsHinzu"     : u"Newsgroup-bijdragen toevoegen",
"DateiWeg"      : u"Bestand(en) verwijderen",

"OptSave"       : u"Voorkeuren opslaan",
"Exit"          : u"Exit",

"ImpEx"         : u"Export",
"Ex2csv"        : u"Frequentielijst > CSV-file",
"Ex2txt"        : u"Concordanties > TXT-file",
"Ex2excel"      : u"Frequentielijst > MS Excel",
"Ex2word"       : u"Concordanties > MS Word",
"ImpKorpus"     : u"Corpus importeren (TextSTAT 1.x)",

"Sprache"       : u"Taal",
"CodePage"      : u"Codering",
"Hilfe"         : u" ? ",
"RegExpHelp"    : u"Regular Expressions - Hulp",
"History"       : u"Geschiedenis (Duits)",
"License"       : u"Licentie (Engels)",
"Willkommen"    : u" Welkom bij TextSTAT",


##### Toolbar #####
"KorpusNew2"    : u"Nieuw corpus maken",
"KorpusOpen2"   : u"Bestaand corpus openen",
"KorpusHinzu2"  : u"Bestaand corpus toevoegen aan corpus",
"KorpusSave2"   : u"Actuele corpus opslaan",
"KorpusDel2"    : u"Corpus bestand wordt gewist",
"WebHinzu2"     : u"HTML-bestanden uit Internet toevoegen aan corpus",
"DateiHinzu2"   : u"Bestand van harde schijf toevoegen aan corpus",
"DateiWeg2"     : u"Bestand(en) uit corpus verwijderen",
"FreqZeigen"    : u"Woordfrequenties tonen",
"FreqZeigen2"   : u"Frequentie van woordvormen in het corpus berekenen",
"Kopieren"      : u"Naar klembord kopiëren",
"Kopieren2"     : u"Selectie naar klembord kopiëren",
"Ex2excel2"     : u"Frequentielijst exporteren naar MS Excel",
"Ex2word2"      : u"Concordanties exporteren naar MS Word",
"Info"          : u"Informatie over TextSTAT",
"Info2"         : u"Informatie over het programma",

##### Tabs #####
"KorpusTab"     : u"Corpus", 
"FormenTab"     : u"Woordvormen",
"ConcTab"       : u"Concordantie",
"ZitatTab"      : u"Citaat",
"ClustNGramsTab": u"Cluster/N-Grams",
"CollocatesTab" : u"Collocates",
"LConcTab" : u"KWIDC",
"TextGraphTab": u"Graph model",

"KTinfo"        : u"TextSTAT \n\nEerst een paar bestanden toevoegen aan een nieuw corpus resp. een bestaand corpus openen.",
"KTkopieren"    : u"Bestandsnaam kopiëren",
"KTopen"        : u"Bestand openen",
"KTdatinfo"     : u"Informatie over bestand",
"KTdatweg"      : u"Bestand(en) uit corpus verwijderen",

"FTinfo"        : u"FREQUENTIE \nvan woordvormen (tokens)",
"FTsortFreq"    : u"sorteren op frequentie",
"FTsortAlpha"   : u"sorteren op alfabet",
"FTsortRetro"   : u"retrograde sorteren",
"FTminFreq"     : u"min. frequentie",
"FTmaxFreq"     : u"max. frequentie",
"FTignGross"    : u"hoofdletters negeren (A=a)",
"FTsuchFreq"    : u"Definieer filter (string of\nreguliere expressie):",
"FTfreqliste"   : u"Frequentielijst",
"FTwortform"    : u"Woordvorm",
"FTfrequenz"    : u"Frequentie",
"FTkopieren"    : u"Kopiëren",
"FTsuchKonk"    : u"Concordanties zoeken",
"FTzeigInfo"    : u"meer informatie",
"FTformInfo"    : u"Corpus informatie\n\nHet corpus bevat in totaal %s woorden (tokens)\n\n%s verschillende vormen (types, hoofdletters en kleine letter worden onderscheiden) resp. \n%s types (hoofdletters worden genegeerd)\n\nDe vorm '%s' komt %s keer voor (= %.2f %%)",
"FTOptionen"    : u"Frequentie / opties",

"CTsuchen"      : u"Zoeken",
"CTganzWort"    : u"alleen hele woorden",
"CTignGross"    : u"hoofdletters negeren",
"CTcontextL"    : u"Context links",
"CTcontextR"    : u"Context rechts",
"CTmarkSuch"    : u"Zoekbegrip markeren",
"CTsortAlpha"   : u"alfabetisch",
"CTsortR"       : u"sorteren op context rechts",
"CTsortL"       : u"sorteren op context links",
"CTaktualisier" : u"Aktualiseren",
"CTmachQuery"   : u"Query-editor",
"CTkopieren"    : u"Kopiëren",
"CTzeigZitat"   : u"Meer context tonen",
"CTOptionen"    : u"Opties",

"ZTinfo"        : u"Tekst van de bewijsplaats",
"ZTkopieren"    : u"Kopiëren",
"ZToeffnen"     : u"Bestand openen",
"ZToeffnen2"    : u"\n(Dubbele klik om bestand te openen)\n",
"ZTInit"        : u"\n Dubbele klik op een regel in de concordantie-tab toont hier diezelfde regel met meer context.",
"ClTFreqR"      :u"FreqR",
"ClTFreqL"      :u"FreqL",
"ClTKoef"       :u"Koef",
"ClTToken"      :u"Token",

"LCTSeparate"   :u"Separator",
"LCTSepBy"      :u"Separate by words",
"Source"        :u"Source",


##### WebDialog #####
"WDinfo"        : u"Voeg HTML-bestanden toe direct van Internet.\nVoer hier een URL in a.u.b.:",
"WDfrageSeiten" : u"Hoeveel pagina's wilt u toevoegen aan uw corpus?",
"WDanzahl"      : u"aantal pagina's om te downloaden",
"WDinSubdir"    : u"zoekdomein: deze map",
"WDaufServer"   : u"zoekdomein: hele server ",
"WDok"          : u"Zoeken",
"WDcancel"      : u"Sluiten",

##### NewsDialog #####
"NDinfo"        : u"Newsgroup-bijdragen toevoegen aan corpus", 
"NDserver"      : u"News server",  
"NDgruppe"      : u"Newsgroup", 
"NDanzahl"      : u"aantal bijdragen", 
"NDzitWeg"      : u"citaten uit bijdragen verwijderen", 
"NDok"          : u"Zoeken",
"NDcancel"      : u"Sluiten",

##### QueryDialog #####
"QDinfo"        : u"Hulp bij het formuleren van complexe zoekopdrachten \nU kunt hier ook wildcards gebruiken (* en ?)",
"QDsuchFelder"  : u"Zoekbegrippen",
"QAusdruck1"    : u"eerste zoekbegrip",
"QAusdruck2"    : u"tweede zoekbegrip",
"QAbstand"      : u"Aantal woorden tussen beide zoekbegrippen",
"QAbstandMin"   : u"minimaal en   ",
"QAbstandMax"   : u"maximaal",
"QmachAusdruck" : u"Zoekopdracht uitvoeren",
"QDcancel"      : u"Sluiten",

##### Fehler #####
"Error"         : u"Fout",
"ErrKorpNew"    : u"Corpusbestand kon niet worden aangemaakt!",
"ErrKorpOpen"   : u"Corpus kon niet worden geopend!\nIs dit wel een TextSTAT-corpus-bestand?",
"ErrKorpImp"    : u"Corpus kon niet worden geïmporteerd!",
"ErrNoKorp"     : u"U moet eerst een nieuw corpus aanmaken resp. een bestaand corpus openen.",
"ErrKorpSave"   : u"Korpusbestand kon niet worden opgeslagen!",
"ErrFileOpen"   : u"Fout bij het openen van het bestand!",
"ErrSelect"     : u"U heeft niets geselecteerd!",
"ErrOptSave"    : u"Opties konden niet worden opgeslagen!",
"ErrExport"     : u"Export fout",
"ErrNoFreqList" : u"Er is geen lijst met woordfrequenties",
"ErrNoKonkList" : u"Er is geen concordantielijst",
"ErrExcel"      : u"MS Excel fout!\n(Zijn de Python win32-extensies en MS Excel geïnstalleerd?)",
"ErrExcel65K"   : u"Fout! MS Excel kan maar 65500 rijen verwerken. \nEr zijn echter %s vormen.",
"ErrWord"       : u"MS Word fout!\n(Zijn de Python win32-extensies en MS Word geïnstalleerd?)",
"ErrExpFreq"    : u"Bij het opslaan van de frequentielijst is iets misgegaan.",
"ErrExpKonk"    : u"Bij het opslaan van de concordantielijst is iets misgegaan.",
"ErrWeb"        : u"Bij het ophalen van HTML-files is iets misgegaan.",
"ErrNews"       : u"Bij het ophalen van newsgroup-berichten is iets misgegaan.",
"ErrQuery"      : u"Er is geen zoekterm ingevoerd.",

##### Mitteilungen und Fragen #####
"AskSure"       : u"Weet u het zeker?",
"AskDelete"     : u"Wilt u werkelijk %s verwijderen?",
"StatusWeb"     : u"Er worden %s files van Internet gehaald en toegevoegd aan corpus...",
"StatusNews"    : u"Er worden %s newsgroup-bijdragen gedownload en toegevoegd...",
"DateiInfo"     : u"Informatie over bestand",
"DateiInfo2"    : u"Bestand: %s\n\nPad: %s\n\nGrootte: %s\n",
"InfoText"      : u"TextSTAT\
\nNadat u een corpus aangemaakt c.q. geopend hebt, kunt u bestanden toevoegen \
of ook weer verwijderen. Markeer een bestand en druk de rechter muistoets \
om meer opties te krijgen. U kunt ook het corpus als geheel opslaan. \
\nVoor de tekstanalyse zijn er meerdere mogelijkheden: \
\nOnder 'Woordvormen' kunt u de frequentie van de afzonderlijke vormen (tokens) laten \
berekenen. 'Concordantie' laat KWIC-concordanties zien (KeyWord in Context) en onder 'Citaat' \
vindt u meer context voor een bepaalde bewijsplaats.",

"StatusKorpImp" : u"Corpus is met succes geïmporteerd.",
"StatusKorpSave": u"Corpus is opgeslagen.",
"StatusFiles"   : u" %s bestanden | %s bytes ",
"StatusKorpDat" : u" Corpus: %s  (momentele codepage/codering: %s)",
"KodierungInfo" : u"U kunt nu bestanden toevoegen.\n\nTekstverwerkingsbestanden:\n- MS Word-bestanden ('.doc' bzw. '.docx'; alleen onder Windows)\n- OpenOffice-bestanden ('.odt of .sxw')\n\nTekstbestanden:\n- ASCII/ANSI-tekstbestanden (meestal '.txt')\n- HTML-bestanden (van uw harde schijf of direct van het Internet)\n- Newsgroup-bestanden (direct van het Internet)\nLet op: bij de platte-tekstbestanden moet u letten op de juiste codering.\nOp dit moment is de volgende codering geselecteerd: %s",
"StatusFormen"  : u" %s woordvormen/types (%s woorden/tokens in corpus)",
"StatusNoKorp"  : u" geen corpus ",
"StatusSuchKonk": u"Zoek concordanties...",
"StatusTreffer" : u" %s treffers ",
"StatusExpFreq" : u"Frequentielijst is geëxporteerd.",
"StatusExpKonk" : u"Concordantielijst is geëxporteerd.",
"ExportHinweis" : u"Voor adequate presentatie kies een niet-proportioneel lettertype (bijv. Courier New)",
"StatusClip"    : u"Selectie is naar het klembord gekopiëerd", 
"SpracheAendern": u"Taal wijzigen",
"SpracheInfo"   : u"U moet het programma opnieuw starten om de taalwijziging te activeren.",
"ProgBeenden"   : u"TextSTAT afsluiten",
"AbfrageEnde"   : u"Het actuele corpus is gewijzigd.\nWilt u het actuele corpus opslaan \nvoordat TextSTAT wordt beëindigd?",
"AbfrageSave"   : u"Het actuele corpus is gewijzigd.\nWilt u het actuele corpus opslaan \nvoordat een nieuw corpus wordt geopend?",
}



##############################
########### English ##########
##############################

english  = {
"Titel"         : u"TextSTAT",
"Titel_lang"    : u"TextSTAT (Simple Text Analysis Tool)",
"Version"       : Version,
"VersionDatum"  : u"Version date %s" % VersionDatum,
"Copyright"     : Copyright,
"eMail"         : eMail,
"ProgURL"       : ProgURL,
"ProgInfo"      : u"TextSTAT is free software.\nUse at your own risk.\nThe author accepts no responsibility.",

###### Menu #####
"Korpus"        : u"Corpus",
"KorpusNew"     : u"New corpus",
"KorpusOpen"    : u"Open corpus",
"KorpusHinzu"   : u"Add corpus",
"KorpusSave"    : u"Save corpus",
"KorpusSaveAs"  : u"Save as",
"KorpusDel"     : u"Delete corpus",
"LetzteKorpora" : u"Recent corpora",

"DateiHinzu"    : u"Add local file",
"WebHinzu"      : u"Add file from web",
"NewsHinzu"     : u"Add newsgroup postings",
"DateiWeg"      : u"Remove file(s)",

"OptSave"       : u"Save options",
"Exit"          : u"Exit",

"ImpEx"         : u"Export",
"Ex2csv"        : u"Frequency list > CSV file",
"Ex2txt"        : u"Concordance list > TXT file",
"Ex2excel"      : u"Frequency list > MS Excel",
"Ex2word"       : u"Concordance list > MS Word",
"ImpKorpus"     : u"Import corpus (TextSTAT 1.x)",

"Sprache"       : u"Language",
"CodePage"      : u"Encoding",
"Hilfe"         : u" ? ",
"RegExpHelp"    : u"Regular Expressions - Help",
"History"       : u"History (German)",
"License"       : u"License",
"Willkommen"    : u" Welcome to TextSTAT",


##### Toolbar #####
"KorpusNew2"    : u"Create new corpus",
"KorpusOpen2"   : u"Open existing corpus",
"KorpusHinzu2"  : u"Add existing corpus to actual corpus",
"KorpusSave2"   : u"Save corpus",
"KorpusDel2"    : u"Delete the corpus file",
"WebHinzu2"     : u"Add HTML file(s) from Internet to corpus",
"DateiHinzu2"   : u"Add local file(s) to corpus",
"DateiWeg2"     : u"Delete file(s) from corpus",
"FreqZeigen"    : u"Show word frequencies",
"FreqZeigen2"   : u"Show frequencies of word forms in corpus",
"Kopieren"      : u"Copy to clipboard",
"Kopieren2"     : u"Copy selection to clipboard",
"Ex2excel2"     : u"Export frequency list to MS Excel",
"Ex2word2"      : u"Export concordances to MS Word",
"Info"          : u"Information",
"Info2"         : u"Information about TextSTAT",

##### Tabs #####
"KorpusTab"     : u"Corpus", 
"FormenTab"     : u"Word forms",
"ConcTab"       : u"Concordance",
"ZitatTab"      : u"Citation",
"ClustNGramsTab": u"Cluster/N-Grams",
"CollocatesTab" : u"Collocates",
"LConcTab" : u"KWIDC",
"TextGraphTab": u"Graph model",

"KTinfo"        : u"TextSTAT \n\nPlease create a corpus and add some files (or open existing corpus).",
"KTkopieren"    : u"Copy file name",
"KTopen"        : u"Open file",
"KTdatinfo"     : u"File information",
"KTdatweg"      : u"Remove file(s)",

"FTinfo"        : u"FREQUENCY \nof word forms (tokens)",
"FTsortFreq"    : u"sort on frequency",
"FTsortAlpha"   : u"sort alphabetically",
"FTsortRetro"   : u"retrograde",
"FTminFreq"     : u"min. frequency",
"FTmaxFreq"     : u"max. frequency",
"FTignGross"    : u"sort case insensitive",
"FTsuchFreq"    : u"Define filter (string or\nregular expression):",
"FTfreqliste"   : u"Frequency list",
"FTwortform"    : u"Word form",
"FTfrequenz"    : u"Frequency",
"FTkopieren"    : u"Copy",
"FTsuchKonk"    : u"Look up concordances",
"FTzeigInfo"    : u"More information",
"FTformInfo"    : u"Corpus information\n\nThe corpus contains %s words (tokens)\n\n%s different forms (types, capital letters are distinctive) \n%s types (capital letters are ignored)\n\nThe form '%s' appears %s times (= %.2f %%)",
"FTOptionen"    : u"Frequency / options",

"CTsuchen"      : u"Search",
"CTganzWort"    : u"search whole words only",
"CTignGross"    : u"search case insensitive",
"CTcontextL"    : u"context left",
"CTcontextR"    : u"context right",
"CTmarkSuch"    : u"mark search string",
"CTsortAlpha"   : u"alphabetically",
"CTsortR"       : u"sort context right",
"CTsortL"       : u"sort context left",
"CTaktualisier" : u"Refresh",
"CTmachQuery"   : u"Query editor",
"CTkopieren"    : u"Copy",
"CTzeigZitat"   : u"Show more context",
"CTOptionen"    : u"Options",

"ZTinfo"        : u"Text of citation",
"ZTkopieren"    : u"Copy",
"ZToeffnen"     : u"Open file",
"ZToeffnen2"    : u"\n(Double click to open file)\n",
"ZTInit"        : u"\n Double click one of the hits in the concordance tab to show the same hit here with more context.",
"ClTFreqR"      :u"FreqR",
"ClTFreqL"      :u"FreqL",
"ClTKoef"       :u"Koef",
"ClTToken"      :u"Token",

"LCTSeparate"   :u"Separator",
"LCTSepBy"      :u"Separate by words",
"Source"        :u"Source",
"Also"         :u"Also",
"TGCompTextGraph":  u"Compute graph-based model",
"TGLoadStatus"   :u"Text graph uploads from file...",
"TGSuccessLoadStatus"   :u"Text graph successfully uploaded from file",
"tf-idf"        : u"TF-IDF",
"TGExport"      : u"Export",
"TGGraphs"      : u"Frequency plots",
"TGmaxWord"     : u"max Word",
"TGmaxValue"        :u"max Value",
"TGminWord"     :u"min Word",
"TGminValue"    :u"min value",
"TGavgWord"     :u"avg Word",
"TGavgValue"    :u"avg value",
"TGVertecesCount"  :u"Verteces count:",
"TGEdgesCount"  :u"Edges count:",
"TGExportError" :u"text graph export error...",
"TGExportNodeSuccess"   :u"Text graph\'s nodes exported to CSV succesfully",
"TGExportEdgeSuccess"   :u"Text graph\'s edges exported to CSV succesfully",
"TGdefaultStopWords"    :u",".join((u'в', u'но', u'и', u'на', u'из', u'то', u'к', u'а', u'что', u'-')),
"TGdefaultWordPattern"    :ur"[a-zA-ZА-ЯёЁ\-]+",
"TGSWordPattern"        :u"Word pattern",
"TGStopWords"       :u"Stop-words",
"TGComputeStatus"       :u"Compute text graph",
"TGStemming"            :u"Stemming",

##### Webdialog #####
"WDinfo"        : u"Add HTML files directly from the internet.\nPlease enter URL:",
"WDfrageSeiten" : u"How many pages do you want to add to your corpus?",
"WDanzahl"      : u"number of pages to retrieve",
"WDinSubdir"    : u"domain: only subdirectory",
"WDaufServer"   : u"domain: whole server",
"WDok"          : u"Search",
"WDcancel"      : u"Close",

##### NewsDialog #####
"NDinfo"        : u"Add newsgroup postings to corpus", 
"NDserver"      : u"news server",  
"NDgruppe"      : u"newsgroup", 
"NDanzahl"      : u"number of postings", 
"NDzitWeg"      : u"remove quotes from postings", 
"NDok"          : u"Search",
"NDcancel"      : u"Close",

##### QueryDialog #####
"QDinfo"        : u"Help function for formulating complex queries \nWildcards are allowed here (* and ?)",
"QDsuchFelder"  : u"Search term",
"QAusdruck1"    : u"first search term",
"QAusdruck2"    : u"second search term",
"QAbstand"      : u"Number of words between the two search terms",
"QAbstandMin"   : u"min. and   ",
"QAbstandMax"   : u"max.",
"QmachAusdruck" : u"Start search",
"QDcancel"      : u"Close",

##### Fehler #####
"Error"         : u"Error",
"ErrKorpNew"    : u"Corpus file could not be created!",
"ErrKorpOpen"   : u"Corpus file could not be opened!\nAre you sure this is a TextSTAT corpus file?",
"ErrKorpImp"    : u"Corpus file could not be imported!!",
"ErrNoKorp"     : u"You have to create a corpus first (or to open an existing corpus).",
"ErrKorpSave"   : u"Corpus file could not be saved!",
"ErrFileOpen"   : u"Error on opening file!",
"ErrSelect"     : u"Nothing selected!",
"ErrOptSave"    : u"Options could not be saved!",
"ErrExport"     : u"Export error",
"ErrNoFreqList" : u"No word frequency list available",
"ErrNoKonkList" : u"No word concordance list available",
"ErrExcel"      : u"MS Excel error!\n(Are the Python win32 extentions an MS Excel installed correctly?)",
"ErrExcel65K"   : u"Error! MS Excel cannot handle more than 65500 rows. \nWe have %s forms.",
"ErrWord"       : u"MS Word error!\n(Are the Python win32 extentions an MS Word installed correctly?)",
"ErrExpFreq"    : u"Error on saving the exported word frequency list.",
"ErrExpKonk"    : u"Error on saving the exported concordance list.",
"ErrWeb"        : u"Error while fetching HTML-files from the internet.",
"ErrNews"       : u"Error while fetching newsgroup postings.",
"ErrQuery"      : u"No search term defined.",


##### Mitteilungen und Fragen #####
"AskSure"       : u"Are you sure?",
"AskDelete"     : u"Do you really want to delete %s ?",
"StatusWeb"     : u"%s files are being retrieved from the internet...",
"StatusNews"    : u"%s newsgroup postings are being retrieved...",
"DateiInfo"     : u"File information",
"DateiInfo2"    : u"File: %s\n\nPath: %s\n\nSize: %s\n",
"InfoText"      : u"TextSTAT\
\nAfter creating (or opening) a corpus, you could add some files to it. \
You could also remove some files of course. The right mouse button will give you a context menu. \
The corpus can be saved as a whole. \
\nThere are some facilities for text analysis: under 'Word forms' you will find \
frequency numbers for the tokens in your texts. 'Concordance' will show you KWIC concordances \
(KeyWord in Context), 'Citation' presents more context.",

"StatusKorpImp" : u"Corpus was imported successfully.",
"StatusKorpSave": u"Corpus has been saved.",
"StatusFiles"   : u" %s files | %s bytes ",
"StatusKorpDat" : u" Corpus: %s  (actual CodePage setting: %s)",
"KodierungInfo" : u"You may now add some files to the corpus.\n\nWord processor files:\n- MS Word files ('.doc' or '.docx'; Windows only)\n- OpenOffice-files ('.odt or .sxw')\n\nText files:\n- ASCII/ANSI text files (often '.txt')\n- HTML files (from your hard disc or directly from Internet)\n- Newgroup postings (directly from Internet)\nWhen adding text files, make sure you are using the correct encoding.\nThe actual setting is: %s",
"StatusFormen"  : u" %s word forms/types (%s words/tokens in corpus)",
"StatusNoKorp"  : u" no corpus ",
"StatusSuchKonk": u"Look up concordances...",
"StatusTreffer" : u" %s hits ",
"StatusExpFreq" : u"Frequency list has been exported.",
"StatusExpKonk" : u"Concordance list has been exported",
"ExportHinweis" : u"You should use a non-proportional font (like Courier New)",
"StatusClip"    : u"Selection has been copied to clipboard", 
"SpracheAendern": u"Change language",
"SpracheInfo"   : u"You have to restart TextSTAT to activate the language change.",
"ProgBeenden"   : u"Exit TextSTAT",
"AbfrageEnde"   : u"The corpus has been changed. \nWould you like to save your corpus \nbefore closing TextSTAT?",
"AbfrageSave"   : u"The corpus has been changed. \nWould you like to save your corpus \nbefore opening another corpus?",
}


##############################
########### Portuguese #######
##############################
# Thanks to Hugo Sunayama <hugocogeae@yahoo.com.br> for the translation

portuguese  = {
"Titel"         : u"TextSTAT",
"Titel_lang"    : u"TextSTAT (Simple Text Analysis Tool)",
"Version"       : Version,
"VersionDatum"  : u"Data da versão %s" % VersionDatum,
"Copyright"     : Copyright,
"eMail"         : eMail,
"ProgURL"       : ProgURL,
"ProgInfo"      : u"TextSTAT é software livre.\nUse por sua conta e risco.\nO autor não aceita qualquer tipo de responsabilidade.\n\nPortuguese translation by Hugo Sunayama <hugocogeae@yahoo.com.br>",

###### Menu #####
"Korpus"        : u"Corpus",
"KorpusNew"     : u"Novo corpus",
"KorpusOpen"    : u"Abrir corpus",
"KorpusHinzu"   : u"Adicionar corpus",
"KorpusSave"    : u"Salvar corpus",
"KorpusSaveAs"  : u"Salvar como",
"KorpusDel"     : u"Deletar corpus",
# has to be translated:
"LetzteKorpora" : u"Recent corpora",

"DateiHinzu"    : u"Adicionar arquivo local",
"WebHinzu"      : u"Adicionar arquivo da web",
"NewsHinzu"     : u"Adicionar publicações de um grupo de notícias",
"DateiWeg"      : u"Remover arquivo(s)",

"OptSave"       : u"Salvar opções",
"Exit"          : u"Sair",

"ImpEx"         : u"Exportar",
"Ex2csv"        : u"Lista de freqüências > Arquivo CSV",
"Ex2txt"        : u"Lista de concordâncias > Arquivo TXT",
"Ex2excel"      : u"Lista de freqüências > MS Excel",
"Ex2word"       : u"Lista de concordâncias > MS Word",
"ImpKorpus"     : u"Importar corpus (TextSTAT 1.x)",

"Sprache"       : u"Língua",
"CodePage"      : u"Codificação",
"Hilfe"         : u" ? ",
"RegExpHelp"    : u"Expressões regulares - Ajuda",
"History"       : u"Histórico (em Alemão)",
"License"       : u"Licença",
"Willkommen"    : u" Bem-vindo ao TextSTAT",


##### Toolbar #####
"KorpusNew2"    : u"Criar novo corpus",
"KorpusOpen2"   : u"Abrir corpus existente",
"KorpusHinzu2"  : u"Adicionar corpus existente ao corpus atual",
"KorpusSave2"   : u"Salvar corpus",
"KorpusDel2"    : u"Deletar o arquivo do corpus",
"WebHinzu2"     : u"Adicionar arquivo(s) HTML de um corpus da internet",
"DateiHinzu2"   : u"Adicionar arquivo local ao corpus",
"DateiWeg2"     : u"Deletar arquivo(s) do corpus",
"FreqZeigen"    : u"Mostrar freqüência de palavras",
"FreqZeigen2"   : u"Mostrar freqüência de formas (de palavras) no corpus",
"Kopieren"      : u"Copiar para a área de transferência",
"Kopieren2"     : u"Copiar seleção para a área de transferência",
"Ex2excel2"     : u"Exportar lista de freqüência para o MS Excel",
"Ex2word2"      : u"Exportar concordâncias para o MS Word",
"Info"          : u"Informações",
"Info2"         : u"Informações a respeito do TextSTAT",

##### Tabs #####
"KorpusTab"     : u"Corpus", 
"FormenTab"     : u"Formas",
"ConcTab"       : u"Concordância",
"ZitatTab"      : u"Citação",
"ClustNGramsTab": u"Cluster/N-Grams",
"CollocatesTab" : u"Collocates",
"LConcTab" : u"KWIDC",
"TextGraphTab": u"Graph model",

"KTinfo"        : u"TextSTAT \n\nFavor, crie um corpus e adicione alguns arquivos (ou abra um corpus existente).",
"KTkopieren"    : u"Copie o nome do arquivo",
"KTopen"        : u"Abrir arquivo",
"KTdatinfo"     : u"Informações do arquivo",
"KTdatweg"      : u"Remover arquivo(s)",

"FTinfo"        : u"FREQÜÊNCIA \nde formas (tokens)",
"FTsortFreq"    : u"organizar por freqüência",
"FTsortAlpha"   : u"organizar alfabeticamente",
"FTsortRetro"   : u"ordem reversa",
"FTminFreq"     : u"freqüência min.",
"FTmaxFreq"     : u"freqüência max.",
"FTignGross"    : u"organizar sem distinção de tipo\n(letras maiúsculas ou minúsculas)",
"FTsuchFreq"    : u"OU buscar a freqüência de\npalavras contendo os caracteres:",
"FTfreqliste"   : u"Lista de freqüência",
"FTwortform"    : u"Formas",
"FTfrequenz"    : u"Freqüência",
"FTkopieren"    : u"Copiar",
"FTsuchKonk"    : u"Buscar concordâncias",
"FTzeigInfo"    : u"Mais informações",
"FTformInfo"    : u"Informação do corpus\n\nO corpus contém %s palavras (tokens)\n\n%s formas diferentes (tipos, letras maiúsculas são diferenciadas) \n%s tipos (letras maiúsculas são ignoradas)\n\nA forma '%s' aparece %s vezes (= %.2f %%)",
"FTOptionen"    : u"Freqüência / opções",

"CTsuchen"      : u"Pesquisar",
"CTganzWort"    : u"coincindir somente com a palavra inteira",
"CTignGross"    : u"não diferenciar letras maiúsculas e minúsculas",
"CTcontextL"    : u"contexto à esquerda",
"CTcontextR"    : u"contexto à direita",
"CTmarkSuch"    : u"destacar padrão ou palavra consultada",
"CTsortAlpha"   : u"alfabeticamente",
"CTsortR"       : u"organizar o contexto à direita",
"CTsortL"       : u"organizar o contexto à esquerda",
"CTaktualisier" : u"Atualizar",
"CTmachQuery"   : u"Editor de consultas",
"CTkopieren"    : u"Copiar",
"CTzeigZitat"   : u"Mostrar contexto mais amplo",
"CTOptionen"    : u"Opções",

"ZTinfo"        : u"Texto da citação",
"ZTkopieren"    : u"Copiar",
"ZToeffnen"     : u"Abrir arquivo",
"ZToeffnen2"    : u"\n(Clique duas vezes para abrir o arquivo)\n",
# Has to be translated:
"ZTInit"        : u"\n Double click one of the hits in the concordance tab to show the same hit here with more context.",
"ClTFreqR"      :u"FreqR",
"ClTFreqL"      :u"FreqL",
"ClTKoef"       :u"Koef",
"ClTToken"      :u"Token",

"LCTSeparate"   :u"Separator",
"LCTSepBy"      :u"Separate by words",
"Source"        :u"Source",


##### Webdialog #####
"WDinfo"        : u"Adicionar arquivo(s) HTML diretamente da Internet.\nFavor digite o endereço (URL):",
"WDfrageSeiten" : u"Quantas páginas você quer adicionar ao seu corpus?",
"WDanzahl"      : u"número de páginas a recuperar",
"WDinSubdir"    : u"domínio: somente subdiretório",
"WDaufServer"   : u"domínio: servidor inteiro",
"WDok"          : u"Buscar",
"WDcancel"      : u"Fechar",

##### NewsDialog #####
"NDinfo"        : u"Adicionar publicações de um grupo de notícias ao corpus", 
"NDserver"      : u"servidor de notícias",  
"NDgruppe"      : u"grupo de notícias", 
"NDanzahl"      : u"número de publicações (postings)", 
"NDzitWeg"      : u"remover citações das publicações", 
"NDok"          : u"Buscar",
"NDcancel"      : u"Fechar",

##### QueryDialog #####
"QDinfo"        : u"Função de ajuda para formular consultas complexas\nCaracteres curinga (wildcards) são permitidos aqui (* e ?)",
"QDsuchFelder"  : u"Consulta",
"QAusdruck1"    : u"primeiro padrão (palavra)",
"QAusdruck2"    : u"segundo padrão (palavra)",
"QAbstand"      : u"Número de palavras entre os padrões (palavras) consultados",
"QAbstandMin"   : u"min. e  ",
"QAbstandMax"   : u"max.",
"QmachAusdruck" : u"Iniciar consulta",
"QDcancel"      : u"Fechar",

##### Fehler #####
"Error"         : u"Erro",
"ErrKorpNew"    : u"Arquivo do corpus não pôde ser criado!",
"ErrKorpOpen"   : u"Arquivo do corpus não pôde ser aberto!\nVocê tem certeza de que este é um arquivo de corpus do TextSTAT?",
"ErrKorpImp"    : u"Arquivo do corpus não pôde ser importado!",
"ErrNoKorp"     : u"Você deve primeiramente criar um corpus (ou abrir um corpus existente).",
"ErrKorpSave"   : u"Arquivo do corpus não pôde ser salvo!",
"ErrFileOpen"   : u"Erro ao abrir o arquivo!",
"ErrSelect"     : u"Nada selecionado!",
"ErrOptSave"    : u"Opções não foram armazenadas!!",
"ErrExport"     : u"Erro ao exportar",
"ErrNoFreqList" : u"Nenhuma lista de freqüência disponível",
"ErrNoKonkList" : u"Nenhuma lista de concordâncias disponível",
"ErrExcel"      : u"Erro do MS Excel!\n(As extensões win32 do Python e o MS Excel estão instalados corretamente?)",
"ErrExcel65K"   : u"Erro! O MS Excel não pode gerenciar mais de 65500 linhas. \nTemos %s formas.",
"ErrWord"       : u"Erro do MS Word!\n(As extensões win32 do Python e o MS Word estão instalados corretamente?)",
"ErrExpFreq"    : u"Erro ao salvar a lista de freqüências de palavras exportada.",
"ErrExpKonk"    : u"Erro ao salvar a lista de concordâncias exportada.",
"ErrWeb"        : u"Erro ao buscar arquivos HTML da Internet.",
"ErrNews"       : u"Erro ao buscar publicações de grupos de notícias.",
"ErrQuery"      : u"Nenhuma palavra (padrão) de busca definida.",


##### Mitteilungen und Fragen #####
"AskSure"       : u"Você tem certeza?",
"AskDelete"     : u"Você realmente quer deletar %s ?",
"StatusWeb"     : u"%s arquivos estão sendo coletados da Internet...",
"StatusNews"    : u"%s publicações de grupos de notícias estão sendo coletadas...",
"DateiInfo"     : u"Informação do arquivo",
"DateiInfo2"    : u"Arquivo: %s\n\nCaminho: %s\n\nTamanho: %s\n",
"InfoText"      : u"TextSTAT\
\n\n\nApós criar (ou abrir) um corpus, você pode adicionar alguns arquivos a ele. \
Você pode, obviamente, remover alguns arquivos também. O botão direito do mouse mostrará um menu de opções. \
O corpus pode ser salvo como um todo. \
\n\nHá alguns utilitários para análise textual: \n\nEm 'Formas' você encontrará \
números de freqüências para tokens em seus textos. \nEm 'Concordâncias' você encontrará concordâncias KWIC \
(palavras - chave contextualizadas). \n'Citação' apresenta contextos amplificados.",

"StatusKorpImp" : u"O corpus foi importado com sucesso.",
"StatusKorpSave": u"O corpus foi salvo.",
"StatusFiles"   : u" %s arquivos | %s bytes ",
"StatusKorpDat" : u" Corpus: %s  (atual definição de codificação: %s)",
"KodierungInfo" : u"Agora você pode adicionar alguns arquivos ao corpus.\n\nArquivos de processadores de texto:\n- arquivos do MS Word ('.doc', '.docx'; somente Windows)\n- arquivos do OpenOffice ('.sxw', '.odt')\n\nArquivos de texto:\n- arquivos de texto ASCII/ANSI (frequentemente '.txt')\n- arquivos HTML (localizados em seu HD ou diretamente da Internet)\n- Publicações de grupos de notícias (diretamente da Internet)\nAo adicionar arquivos de texto, certifique-se de usar a codificação correta.\nA definição atual é: %s",
"StatusFormen"  : u" %s formas/tipos (%s palavras/tokens no corpus)",
"StatusNoKorp"  : u" nenhum corpus ",
"StatusSuchKonk": u"Buscar concordâncias...",
"StatusTreffer" : u" %s hits ",
"StatusExpFreq" : u"A lista de freqüências foi exportada.",
"StatusExpKonk" : u"A lista de concordâncias foi exportada",
"ExportHinweis" : u"Você deve utilizar uma fonte não-proporcional (como Courier New)",
"StatusClip"    : u"A seleção foi copiada para a área de transferência", 
"SpracheAendern": u"Mudar a língua",
"SpracheInfo"   : u"Você deve reiniciar o TextSTAT para ativar a mudança de língua.",
"ProgBeenden"   : u"Sair do TextSTAT",
"AbfrageEnde"   : u"O corpus foi alterado. \nVocê gostaria de salvar o seu corpus \nantes de fechar o TextSTAT?",
"AbfrageSave"   : u"O corpus foi alterado. \nVocê gostaria de salvar o seu corpus \nantes de abrir outro corpus?",
}

##############################
########### Français #########
##############################
# Thanks to Robert Caron <robert.caron@wanadoo.fr> for the translation!
# Contains some updates and changes by Christophe Combelles <ccomb@gorfou.fr>.
# Thanks!

francais  = {
"Titel"         : u"TextSTAT",
"Titel_lang"    : u"TextSTAT (Outil d'analyse de textes)",
"Version"       : Version,
"VersionDatum"  : u"Version date %s" % VersionDatum,
"Copyright"     : Copyright,
"eMail"         : eMail,
"ProgURL"       : ProgURL,
"ProgInfo"      : u"TextSTAT est un logiciel libre.\nL'auteur décline toute responsabilité.\npour d'éventuelles erreurs.\n\nFrench translation by Robert Caron <robert.caron@wanadoo.fr>",

###### Menu #####
"Korpus"        : u"Corpus",
"KorpusNew"     : u"Nouveau corpus",
"KorpusOpen"    : u"Ouvrir un corpus",
"KorpusHinzu"   : u"Ajouter un corpus",
"KorpusSave"    : u"Enregistrer le corpus",
"KorpusSaveAs"  : u"Enregistrer sous...",
"KorpusDel"     : u"Supprimer le corpus",
"LetzteKorpora" : u"Corpus récents",

"DateiHinzu"    : u"Ajouter un fichier",
"WebHinzu"      : u"Ajouter une URL",
"NewsHinzu"     : u"Ajouter des messages d'un Newsgroup",
"DateiWeg"      : u"Effacer fichier(s)",

"OptSave"       : u"Sauvegarder les options",
"Exit"          : u"Quitter",

"ImpEx"         : u"Exporter",
"Ex2csv"        : u"Liste de fréquences > Fichier CSV",
"Ex2txt"        : u"Liste de concordances > Fichier TXT",
"Ex2excel"      : u"Liste de fréquences > MS Excel",
"Ex2word"       : u"Liste de concordances > MS Word",
"ImpKorpus"     : u"Importer un corpus (TextSTAT 1.x)",

"Sprache"       : u"Langage",
"CodePage"      : u"Codage des caractères",
"Hilfe"         : u" ? ",
"RegExpHelp"    : u"Expressions rationnelles - Aide",
"History"       : u"Historique (Allemand)",
"License"       : u"Licence",
"Willkommen"    : u" Bienvenue dans TextSTAT",


##### Toolbar #####
"KorpusNew2"    : u"Nouveau corpus",
"KorpusOpen2"   : u"Ouvrir un corpus",
"KorpusHinzu2"  : u"Ajouter un corpus au corpus actuel",
"KorpusSave2"   : u"Enregistrer le corpus",
"KorpusDel2"    : u"Effacer le fichier du corpus",
"WebHinzu2"     : u"Ajouter des fichiers HTML depuis internet dans le corpus",
"DateiHinzu2"   : u"Ajouter des fichiers locaux au corpus",
"DateiWeg2"     : u"Effacer fichier(s) du corpus",
"FreqZeigen"    : u"Montrer les fréquences des mots",
"FreqZeigen2"   : u"Montrer les fréquences des formes de mots dans le corpus",
"Kopieren"      : u"Copier dans presse-papier",
"Kopieren2"     : u"Copier la sélection dans le presse-papier",
"Ex2excel2"     : u"Exporter la liste des fréquences vers MS Excel",
"Ex2word2"      : u"Exporter les concordances vers MS Word",
"Info"          : u"Informations",
"Info2"         : u"Informations à propos de TextSTAT",

##### Tabs #####
"KorpusTab"     : u"Corpus",
"FormenTab"     : u"Formes de mots",
"ConcTab"       : u"Concordances",
"ZitatTab"      : u"Citation",
"ClustNGramsTab": u"Cluster/N-Grams",
"CollocatesTab" : u"Collocates",
"LConcTab" : u"KWIDC",
"TextGraphTab": u"Graph model",

"KTinfo"        : u"TextSTAT \n\nCréer un corpus et ajouter quelques fichiers (ou ouvrir un corpus existant).",
"KTkopieren"    : u"Copier le nom du fichier",
"KTopen"        : u"Ouvrir le fichier",
"KTdatinfo"     : u"Informations sur le fichier",
"KTdatweg"      : u"Supprimer les fichiers",

"FTinfo"        : u"FREQUENCES \ndes formes de mots (signes)",
"FTsortFreq"    : u"Classer par fréquence",
"FTsortAlpha"   : u"Classer par ordre alphabétique",
"FTsortRetro"   : u"Classer par ordre alphabétique inverse",
"FTminFreq"     : u"Fréquence min.",
"FTmaxFreq"     : u"Fréquence max.",
"FTignGross"    : u"Trier entre MAJUSCULES et minuscules",
"FTsuchFreq"    : u"OU montrer les fréquences des\nmots contenant la chaîne de caractères :",
"FTfreqliste"   : u"Liste de fréquences",
"FTwortform"    : u"Formes de mots",
"FTfrequenz"    : u"Fréquences",
"FTkopieren"    : u"Copier",
"FTsuchKonk"    : u"Montrer les concordances",
"FTzeigInfo"    : u"Plus d'informations",
"FTformInfo"    : u"Information sur le corpus\n\nLe corpus contient %s mots (signes)\n\n%s formes différentes (types, lettres majuscules prises en compte) \n%s types (lettres majuscules sont ignorées)\n\nLa forme '%s' apparaît %s fois (= %.2f %%)",
"FTOptionen"    : u"Fréquences / options",

"CTsuchen"      : u"Rechercher",
"CTganzWort"    : u"Rechercher mots entiers seulement",
"CTignGross"    : u"Rechercher sans distinction \nmajuscule/minuscule",
"CTcontextL"    : u"Contexte gauche",
"CTcontextR"    : u"Contexte droit",
"CTmarkSuch"    : u"Marquer la chaîne recherchée",
"CTsortAlpha"   : u"Alphabétique",
"CTsortR"       : u"Classer par contexte droit",
"CTsortL"       : u"Classer par contexte gauche",
"CTaktualisier" : u"Actualiser",
"CTmachQuery"   : u"Éditeur de requête",
"CTkopieren"    : u"Copier",
"CTzeigZitat"   : u"Montrer plus de contexte",
"CTOptionen"    : u"Options",

"ZTinfo"        : u"Texte de la citation",
"ZTkopieren"    : u"Copier",
"ZToeffnen"     : u"Ouvrir le fichier",
"ZToeffnen2"    : u"\n(Double-cliquez pour ouvrir le fichier)\n",
"ZTInit"        : u"\n Double-cliquez une de ces concordances pour l'afficher dans son contexte.",
"ClTFreqR"      :u"FreqR",
"ClTFreqL"      :u"FreqL",
"ClTKoef"       :u"Koef",
"ClTToken"      :u"Token",

"LCTSeparate"   :u"Separator",
"LCTSepBy"      :u"Separate by words",
"Source"        :u"Source",


##### Webdialog #####
"WDinfo"        : u"Ajouter fichiers HTML directement depuis internet.\nEntrez son URL:",
"WDfrageSeiten" : u"Combien de pages voulez-vous ajouter à votre corpus ?",
"WDanzahl"      : u"Nombre de pages à trouver",
"WDinSubdir"    : u"Domaine : seulement les sous-répertoires",
"WDaufServer"   : u"Domaine : tout le serveur",
"WDok"          : u"Chercher",
"WDcancel"      : u"Fermer",

##### NewsDialog #####
"NDinfo"        : u"Ajouter des messages de Newsgroups dans le corpus",
"NDserver"      : u"Serveur de Newsgroups",
"NDgruppe"      : u"Newsgroup",
"NDanzahl"      : u"Nombre de messages",
"NDzitWeg"      : u"Supprimer les citations des messages",
"NDok"          : u"Chercher",
"NDcancel"      : u"Fermer",

##### QueryDialog #####
"QDinfo"        : u"Fonction d'aide de formulation de requêtes complexes \nCaractères de remplacement sont attribués ici (* et ?)",
"QDsuchFelder"  : u"Terme recherché",
"QAusdruck1"    : u"Premier terme recherché",
"QAusdruck2"    : u"Second terme recherché",
"QAbstand"      : u"Nombre de mots entre les deux termes recherchés",
"QAbstandMin"   : u"min. et   ",
"QAbstandMax"   : u"max.",
"QmachAusdruck" : u"Démarrer recherche",
"QDcancel"      : u"Fermer",

##### Fehler #####
"Error"         : u"Erreur",
"ErrKorpNew"    : u"Le fichier de corpus ne peut être créé !",
"ErrKorpOpen"   : u"Le fichier de corpus ne peut pas être ouvert !\nEtes-vous sûr qu'il s'agit d'un fichier corpus de TextSTAT ?",
"ErrKorpImp"    : u"Le fichier corpus ne peut être importé !!",
"ErrNoKorp"     : u"Vous devez d'abord créer un fichier de corpus (ou ouvrir un corpus existant).",
"ErrKorpSave"   : u"Le fichier de corpus ne peut pas être sauvegardé !",
"ErrFileOpen"   : u"Erreur à l'ouverture du fichier !",
"ErrSelect"     : u"Rien n'a été sélectionné !",
"ErrOptSave"    : u"Les Options ne peuvent pas être sauvegardées !",
"ErrExport"     : u"Erreur à l'exportation",
"ErrNoFreqList" : u"Pas de liste de fréquence de mots disponible",
"ErrNoKonkList" : u"Pas de liste de concordances de mots disponible",
"ErrExcel"      : u"Erreur MS Excel !\n(Est-ce que l'extension Python win32 et MS Excel sont installés correctement ?)",
"ErrExcel65K"   : u"Erreur ! MS Excel ne peut traiter plus de 65500 lignes. \nVous avez %s formes.",
"ErrWord"       : u"MS Word erreur !\n(Est-ce que l'extension Python win32 et MS Word sont installés correctement ??)",
"ErrExpFreq"    : u"Erreur lors de la sauvegarde de l'export de la liste de fréquences.",
"ErrExpKonk"    : u"Erreur lors de la sauvegarde de l'export de la liste de concordances.",
"ErrWeb"        : u"Erreur de chargement de fichiers HTML depuis internet.",
"ErrNews"       : u"Erreur de chargement de messages du Newsgroup.",
"ErrQuery"      : u"Pas de terme à rechercher.",


##### Mitteilungen und Fragen #####
"AskSure"       : u"Êtes-vous sûr ?",
"AskDelete"     : u"Voulez-vous vraiment effacer %s ?",
"StatusWeb"     : u"%s fichiers sont en récupération depuis internet...",
"StatusNews"    : u"%s messages du NewsGroup ont été trouvés...",
"DateiInfo"     : u"Informations sur le fichier",
"DateiInfo2"    : u"Fichier : %s\n\nChemin : %s\n\nTaille : %s\n",
"InfoText"      : u"TextSTAT\
\nAprès avoir créé (ou ouvert) un corpus, vous pourrez lui ajouter des fichiers. \
Vous pourrez, bien sûr, aussi supprimer des fichiers. Le clic-droit de la souris ouvre un menu contextuel. \
Le corpus peut être sauvegardé dans son ensemble. \
\nIl y a quelques outils pour l'analyse de textes : vous trouverez dans 'Formes de mots' \
les fréquences pour les signes de vos textes. 'Concordances' vous montre vos concordances KWIC \
(mots-clés en contexte), 'Citation' donne davantage de contexte.",

"StatusKorpImp" : u"Corpus a été importé correctement.",
"StatusKorpSave": u"Corpus a été sauvegardé.",
"StatusFiles"   : u" %s fichiers | %s octets ",
"StatusKorpDat" : u" Corpus: %s  (Code de caractères actuel : %s)",
"KodierungInfo" : u"Vous pouvez maintenant ajouter des fichiers à votre corpus.\n\nFichiers de Traitement de textes :\n- Fichiers MS Word ('.doc', '.docx'; Windows seulement)\n- Fichiers OpenOffice.org ('.sxw', '.odt')\n\nFichiers texte :\n- ASCII/ANSI fichiers texte (souvent '.txt')\n- Fichiers HTML (depuis votre disque dur ou directement depuis internet)\n- Messages du Newsgroup (directement depuis internet)\nLors de l'ajout de fichiers textes, vérifiez que le codage est correct.\nLe réglage actuel est : %s",
"StatusFormen"  : u" %s mots formes/types (%s mots/signes dans le corpus)",
"StatusNoKorp"  : u" pas de corpus ",
"StatusSuchKonk": u"Mettre en évidence les concordances...",
"StatusTreffer" : u" %s éléments ",
"StatusExpFreq" : u"La liste de fréquences a été exportée.",
"StatusExpKonk" : u"La liste de concordances a été exportée",
"ExportHinweis" : u"Vous devez utiliser une police non-proportionnelle (comme Courier New)",
"StatusClip"    : u"Sélection copiée dans le presse-papier",
"SpracheAendern": u"Changer le langage",
"SpracheInfo"   : u"Vous devez redémarrer TextSTAT pour que le changement soit pris en compte.",
"ProgBeenden"   : u"Quitter TextSTAT",
"AbfrageEnde"   : u"Le corpus a été modifié. \nVoulez-vous sauvegarder votre corpus \navant de quitter TextSTAT ?",
"AbfrageSave"   : u"Le corpus a été modifié. \nVoulez-vous sauvegarder votre corpus \navant d'ouvrir un autre corpus ?",
}


##############################
########### Galician ##########
##############################
# Thanks to Gonçalo Cordeiro <gzcordeiro@gmail.com> for the translation!

galician  = {
"Titel"         : u"TextSTAT",
"Titel_lang"    : u"TextSTAT (utilidade para a análise de textos)",
"Version"       : Version,
"VersionDatum"  : u"Data da versión %s" % VersionDatum,
"Copyright"     : Copyright,
"eMail"         : eMail,
"ProgURL"       : ProgURL,
"ProgInfo"      : u"O TextSTAT é software gratuíto.\nÚseo por súa conta e risco.\nO autor declina toda responsabilidade.\n\nTranslation into Galician by Gonçalo Cordeiro <gzcordeiro@gmail.com>",

###### Menu #####
"Korpus"        : u"Corpus",
"KorpusNew"     : u"Novo corpus",
"KorpusOpen"    : u"Abrir un corpus",
"KorpusHinzu"   : u"Engadir un corpus",
"KorpusSave"    : u"Gardar o corpus",
"KorpusSaveAs"  : u"Gardar como",
"KorpusDel"     : u"Eliminar corpus",
"LetzteKorpora" : u"Últimos corpora",

"DateiHinzu"    : u"Engadir un ficheiro local",
"WebHinzu"      : u"Engadir un ficheiro da Web",
"NewsHinzu"     : u"Engadir mensaxes dun grupo de noticias",
"DateiWeg"      : u"Eliminar ficheiro(s)",

"OptSave"       : u"Gardar as opcións",
"Exit"          : u"Saír",

"ImpEx"         : u"Exportar",
"Ex2csv"        : u"Lista de frecuencias > ficheiro CSV",
"Ex2txt"        : u"Lista de concordancias > ficheiro TXT",
"Ex2excel"      : u"Lista de frecuencias > MS Excel",
"Ex2word"       : u"Lista de frecuencias > MS Word",
"ImpKorpus"     : u"Importar corpus (TextSTAT 1.x)",

"Sprache"       : u"Idioma",
"CodePage"      : u"Codificación",
"Hilfe"         : u" ? ",
"RegExpHelp"    : u"Expresións regulares - Axuda",
"History"       : u"Historia (Alemán)",
"License"       : u"Licenza",
"Willkommen"    : u" Benvido ao TextSTAT",


##### Toolbar #####
"KorpusNew2"    : u"Crear un novo corpus",
"KorpusOpen2"   : u"Abrir un corpus existente",
"KorpusHinzu2"  : u"Engadir un corpus existente ao actual",
"KorpusSave2"   : u"Gardar o corpus",
"KorpusDel2"    : u"Eliminar o ficheiro de corpus",
"WebHinzu2"     : u"Engadir ficheiros HTML desde Internet ao corpus",
"DateiHinzu2"   : u"Engadir ficheiros locais ao corpus",
"DateiWeg2"     : u"Eliminar ficheiros do corpus",
"FreqZeigen"    : u"Mostrar as frecuencias de palabras",
"FreqZeigen2"   : u"Mostra as frecuencias de formas de palabra no corpus",
"Kopieren"      : u"Copiar no portapapeis",
"Kopieren2"     : u"Copia a selección no portapapeis",
"Ex2excel2"     : u"Exportar a lista de frecuencias para o MS Excel",
"Ex2word2"      : u"Exportar as concordancias para o MS Word",
"Info"          : u"Información",
"Info2"         : u"Información sobre o TextSTAT",

##### Tabs #####
"KorpusTab"     : u"Corpus", 
"FormenTab"     : u"Formas de palabra",
"ConcTab"       : u"Concordancias",
"ZitatTab"      : u"Contexto",
"ClustNGramsTab": u"Cluster/N-Grams",
"CollocatesTab" : u"Collocates",
"LConcTab" : u"KWIDC",
"TextGraphTab": u"Graph model",

"KTinfo"        : u"TextSTAT \n\nCree un corpus e engada algún ficheiro (ou abra un corpus existente).",
"KTkopieren"    : u"Copiar o nome do ficheiro",
"KTopen"        : u"Abrir ficheiro",
"KTdatinfo"     : u"Información de ficheiro",
"KTdatweg"      : u"Eliminar ficheiro(s)",

"FTinfo"        : u"FRECUENCIA \ndas formas de palabra (tokens)",
"FTsortFreq"    : u"ordenar por frecuencia",
"FTsortAlpha"   : u"ordenar alfabeticamente",
"FTsortRetro"   : u"orde inversa (d-e)",
"FTminFreq"     : u"frecuencia mín.",
"FTmaxFreq"     : u"frecuencia máx.",
"FTignGross"    : u"ordenar sen distinguir Maiús./min.",
"FTsuchFreq"    : u"OU procurar a frecuencia\ndas palabras que conteñan a cadea:",
"FTfreqliste"   : u"Lista de frecuencias",
"FTwortform"    : u"Forma de palabra",
"FTfrequenz"    : u"Frecuencia",
"FTkopieren"    : u"Copiar",
"FTsuchKonk"    : u"Procurar concordancias",
"FTzeigInfo"    : u"Máis información",
"FTformInfo"    : u"Información sobre o corpus\n\nO corpus contén %s palabras (tokens)\n\n%s formas diferentes (tipos, as maiúsculas son tidas en conta) \n%s tipos (ignorando as maiúsculas)\n\nA forma '%s' aparece %s veces (= %.2f %%)",
"FTOptionen"    : u"Frecuencia / opcións",

"CTsuchen"      : u"Procurar",
"CTganzWort"    : u"procurar só palabras completas",
"CTignGross"    : u"procurar sen distinguir Maiús./min.",
"CTcontextL"    : u"contexto á esquerda",
"CTcontextR"    : u"contexto á dereita",
"CTmarkSuch"    : u"marcar a cadea procurada",
"CTsortAlpha"   : u"alfabeticamente",
"CTsortR"       : u"ordenar o contexto á dereita",
"CTsortL"       : u"ordenar o contexto á esquerda",
"CTaktualisier" : u"Recargar",
"CTmachQuery"   : u"Editor de consultas",
"CTkopieren"    : u"Copiar",
"CTzeigZitat"   : u"Mostrar máis contexto",
"CTOptionen"    : u"Opcións",

"ZTinfo"        : u"Texto da citación",
"ZTkopieren"    : u"Copiar",
"ZToeffnen"     : u"Abrir ficheiro",
"ZToeffnen2"    : u"\n(Prema dúas veces para abrir o ficheiro)\n",
"ZTInit"        : u"\n Prema dúas veces nunha das ocorrencias do separador de concordancias para mostrar esta mesma ocorrencia con máis contexto.",
"ClTFreqR"      :u"FreqR",
"ClTFreqL"      :u"FreqL",
"ClTKoef"       :u"Koef",
"ClTToken"      :u"Token",

"LCTSeparate"   :u"Separator",
"LCTSepBy"      :u"Separate by words",
"Source"        :u"Source",


##### Webdialog #####
"WDinfo"        : u"Engadir ficheiros HTML directamente desde a Internet.\nIntroduza o URL:",
"WDfrageSeiten" : u"Cantas páxinas quere engadir ao seu corpus?",
"WDanzahl"      : u"número de páxinas para recuperar",
"WDinSubdir"    : u"dominio: só o subdirectorio",
"WDaufServer"   : u"dominio: todo o servidor",
"WDok"          : u"Procurar",
"WDcancel"      : u"Pechar",

##### NewsDialog #####
"NDinfo"        : u"Engadir mensaxes dun grupo de noticias ao corpus", 
"NDserver"      : u"servidor de noticias",  
"NDgruppe"      : u"grupo de noticias", 
"NDanzahl"      : u"número de mensaxes", 
"NDzitWeg"      : u"eliminar as citas das mensaxes", 
"NDok"          : u"Procurar",
"NDcancel"      : u"Pechar",

##### QueryDialog #####
"QDinfo"        : u"Función de axuda para formular consultas complexas \nAquí permítense os comodíns (* e ?)",
"QDsuchFelder"  : u"Termo de procura",
"QAusdruck1"    : u"primero termo de procura",
"QAusdruck2"    : u"segundo termo de procura",
"QAbstand"      : u"Número de palabras entre ambos os termos de procura",
"QAbstandMin"   : u"mín. e   ",
"QAbstandMax"   : u"máx.",
"QmachAusdruck" : u"Comezar a procura",
"QDcancel"      : u"Pechar",

##### Fehler #####
"Error"         : u"Erro",
"ErrKorpNew"    : u"Non se puido crear o ficheiro de corpus!",
"ErrKorpOpen"   : u"Non se puido abrir o ficheiro de corpus!\nEstá seguro de que se trata dun ficheiro de corpus do TextSTAT?",
"ErrKorpImp"    : u"Non se puido importar o ficheiro de corpus!!",
"ErrNoKorp"     : u"Primeiro hai que crear un corpus (ou abrir un corpus existente).",
"ErrKorpSave"   : u"Non se puido gardar o ficheiro de corpus!",
"ErrFileOpen"   : u"Erro ao abrir o ficheiro!",
"ErrSelect"     : u"Non se seleccionou nada!",
"ErrOptSave"    : u"Non se puido gardar as opcións!",
"ErrExport"     : u"Erro na exportación",
"ErrNoFreqList" : u"Non hai unha lista de frecuencias dispoñíbel",
"ErrNoKonkList" : u"Non hai unha lista concordancias dispoñíbel",
"ErrExcel"      : u"Erro do MS Excel!\n(Están instalados correctamente as extensións win32 do Python e o MS Excel?)",
"ErrExcel65K"   : u"Erro! O MS Excel non pode manipular máis de 65500 filas. \nHai %s formas.",
"ErrWord"       : u"Erro do MS Word!\n(Están instalados correctamente as extensións win32 do Python e o MS Excel?)",
"ErrExpFreq"    : u"Erro ao gardar a lista de frecuencias exportada.",
"ErrExpKonk"    : u"Erro ao gardar a lista de concordancias exportada.",
"ErrWeb"        : u"Erro ao obter os ficheiros HTML da Internet.",
"ErrNews"       : u"Erro ao obter as mensaxes do grupo de noticias.",
"ErrQuery"      : u"Non se definiu un termo de procura.",


##### Mitteilungen und Fragen #####
"AskSure"       : u"Está seguro?",
"AskDelete"     : u"Quere eliminar %s ?",
"StatusWeb"     : u"estase a obter %s ficheiros da Internet...",
"StatusNews"    : u"estase a obter %s mensaxes de grupo de noticias...",
"DateiInfo"     : u"Información de ficheiro",
"DateiInfo2"    : u"Ficheiro: %s\n\nCamiño: %s\n\nTamaño: %s\n",
"InfoText"      : u"TextSTAT\
\nDespois de crear (ou abrir) un corpus, pode engadirlle algúns ficheiros. \
Pode tamén eliminar ficheiros. O botón dereito do rato proporciona un menú de contexto. \
Pódese gardar o corpus como un conxunto. \
\nHai algunhas utilidades para a análise de textos: debaixo de 'Formas de palabra' encontrará \
os números de frecuencias dos tokens dos seus textos. 'Concordancia' mostra as concordancias KWIC \
(KeyWord in Context), 'Contexto' presenta os segmentos de texto onde aparece a palabra.",

"StatusKorpImp" : u"O corpus importouse correctamente.",
"StatusKorpSave": u"Gardouse o corpus.",
"StatusFiles"   : u" %s ficheiros | %s bytes ",
"StatusKorpDat" : u" Corpus: %s  (Codificación de caracteres actual: %s)",
"KodierungInfo" : u"Agora pode engadir algúns ficheiros ao corpus.\n\nFicheiros de procesador de palabras:\n- ficheiros do MS Word ('.doc' ou '.docx'; só no Windows)\n- ficheiros do OpenOffice.org ('.odt ou .sxw')\n\nFicheiros de texto:\n- ficheiros ASCII/ANSI (normalmente '.txt')\n- ficheiros HTML  (do seu disco ríxido ou directamente da Internet)\n- Mensaxes de grupos de noticias (directamente da Internet)\nAo engadir ficheiros de texto, asegúrese de que emprega a codificación correcta.\nA configuración actual é: %s",
"StatusFormen"  : u" %s formas/tipos de palabra (%s palabras/tokens no corpus)",
"StatusNoKorp"  : u" sen corpus ",
"StatusSuchKonk": u"Procurar concordancias...",
"StatusTreffer" : u" %s ocorrencias ",
"StatusExpFreq" : u"Exportouse a lista de frecuencias.",
"StatusExpKonk" : u"Exportouse a lista de concordancias",
"ExportHinweis" : u"Debe utilizar un tipo de letra non proporcional (como o Courier New)",
"StatusClip"    : u"Copiouse a selección no portapapeis", 
"SpracheAendern": u"Cambiar o idioma",
"SpracheInfo"   : u"É preciso reiniciar o TextSTAT para activar o cambio de idioma.",
"ProgBeenden"   : u"Saír do TextSTAT",
"AbfrageEnde"   : u"Modificouse o corpus. \nQuere gardar o corpus antes de \npechar o TextSTAT?",
"AbfrageSave"   : u"Modificouse o corpus. \nQuere gardar o corpus antes de \nabrir un outro corpus?",
}

##############################
########### Finnish ##########
##############################

#Translator: Lasse Ehrnrooth
#Date: 15/4/2009
#Contact: <lasse.ehrnrooth@helsinki.fi>
#Other translators/proofreaders: Please send email to me if you make changes to the Finnish translations below.

suomi  = {
"Titel"         : u"TextSTAT",
"Titel_lang"    : u"TextSTAT (yksinkertainen ohjelma tekstianalyyseihin)",
"Version"       : Version,
"VersionDatum"  : u"Version päiväys %s" % VersionDatum,
"Copyright"     : Copyright,
"eMail"         : eMail,
"ProgURL"       : ProgURL,
"ProgInfo"      : u"TextSTAT on ilmainen ohjelma.\nKäyttö omalla vastuulla.\nOhjelman tekijä ei vastaa mahdollisista haitoista.\n\nTranslation into Finnish by Lasse Ehrnrooth <lasse.ehrnrooth@helsinki.fi>",

###### Menu #####
"Korpus"        : u"Korpus",
"KorpusNew"     : u"Uusi korpus",
"KorpusOpen"    : u"Avaa korpus",
"KorpusHinzu"   : u"Lisää korpus",
"KorpusSave"    : u"Tallenna korpus",
"KorpusSaveAs"  : u"Tallenna nimellä",
"KorpusDel"     : u"Poista korpus",
"LetzteKorpora" : u"Viimeksi käytetyt korpukset",

"DateiHinzu"    : u"Lisää paikallinen tiedosto",
"WebHinzu"      : u"Lisää tiedosto internetistä",
"NewsHinzu"     : u"Lisää uutisryhmäviesti",
"DateiWeg"      : u"Poista tiedosto(ja)",

"OptSave"       : u"Tallenna asetukset",
"Exit"          : u"Sulje",

"ImpEx"         : u"Vie tiedosto",
"Ex2csv"        : u"Frekvenssilista > CSV tiedosto",
"Ex2txt"        : u"Konkordanssilista > TXT tiedosto",
"Ex2excel"      : u"Frekvenssilista > MS Excel",
"Ex2word"       : u"Konkordanssilista > MS Word",
"ImpKorpus"     : u"Tuo korpus (TextSTAT 1.x)",

"Sprache"       : u"Kieli",
"CodePage"      : u"Merkistökoodaus",
"Hilfe"         : u" ? ",
"RegExpHelp"    : u"Säännölliset lausekkeet - Ohje",
"History"       : u"Historia (saksaksi)",
"License"       : u"Lisenssi",
"Willkommen"    : u" Tervetuloa TextSTAT:in pariin",


##### Toolbar #####
"KorpusNew2"    : u"Luo uusi korpus",
"KorpusOpen2"   : u"Avaa aiemmin luotu korpus",
"KorpusHinzu2"  : u"Lisää aiempi korpus nykyiseen",
"KorpusSave2"   : u"Tallenna korpus",
"KorpusDel2"    : u"Poista korpus tiedosto",
"WebHinzu2"     : u"Lisää HTML tiedosto(ja) internetistä korpukseen",
"DateiHinzu2"   : u"Lisää paikallisia tiedostoja korpukseen",
"DateiWeg2"     : u"Poista tiedosto(ja) korpuksesta",
"FreqZeigen"    : u"Näytä sanojen frekvenssit",
"FreqZeigen2"   : u"Näytä sananmuotojen frekvenssit korpuksessa",
"Kopieren"      : u"Kopioi leikepöydälle",
"Kopieren2"     : u"Kopioi valinta leikepöydälle",
"Ex2excel2"     : u"Vie frekvenssilista MS Exceliin",
"Ex2word2"      : u"Vie konkordanssihaut MS Wordiin",
"Info"          : u"Tietoja",
"Info2"         : u"Tietoja TextSTAT:sta",

##### Tabs #####
"KorpusTab"     : u"Korpus", 
"FormenTab"     : u"Sananmuodot",
"ConcTab"       : u"Konkordanssi",
"ZitatTab"      : u"Sitaatti",
"ClustNGramsTab": u"Cluster/N-Grams",
"CollocatesTab" : u"Collocates",
"LConcTab" : u"KWIDC",
"TextGraphTab": u"Graph model",

"KTinfo"        : u"TextSTAT \n\nLuo korpus ja lisää siihen tiedostoja (tai avaa aiempi korpus).",
"KTkopieren"    : u"Kopioi tiedostonimi",
"KTopen"        : u"Avaa tiedosto",
"KTdatinfo"     : u"Tiedoston ominaisuudet",
"KTdatweg"      : u"Poista tiedosto(ja)",

"FTinfo"        : u"FREKVENSSI \nsaneiden lukumäärä (saneet)",
"FTsortFreq"    : u"järjestä frekvenssittäin",
"FTsortAlpha"   : u"järjestä aakkosittain",
"FTsortRetro"   : u"järjestä sananmuodot viimeisten kirjainten mukaan",
"FTminFreq"     : u"pienin frekvenssi",
"FTmaxFreq"     : u"suurin frekvenssi",
"FTignGross"    : u"laske ja järjestä kirjainkoosta riippumatta",
"FTsuchFreq"    : u"TAI \n\nEtsi frekvenssi\nsanalle tai sanoille merkkijonossa:",
"FTfreqliste"   : u"Luo frekvenssilista",
"FTwortform"    : u"Sananmuoto",
"FTfrequenz"    : u"Frekvenssi",
"FTkopieren"    : u"Kopioi",
"FTsuchKonk"    : u"Etsi konkordansseja",
"FTzeigInfo"    : u"Lisätietoja",
"FTformInfo"    : u"Tietoja korpuksesta\n\nKorpus sisältää sanoja (saneita)\n\n%s erilaisia muotoja (tyyppejä, isot kirjaimet huomioidaan) \n%s tyyppejä (isoja kirjaimia ei huomioida)\n\nMuoto '%s' esiintyy %s kertaa (= %.2f %%)",
"FTOptionen"    : u"Frekvenssiasetukset",

"CTsuchen"      : u"Etsi",
"CTganzWort"    : u"etsi vain kokonaisia sanoja",
"CTignGross"    : u"etsi kirjainkoosta riippumatta",
"CTcontextL"    : u"vasen konteksti",
"CTcontextR"    : u"oikea konteksti",
"CTmarkSuch"    : u"korosta etsittävä merkkijono",
"CTsortAlpha"   : u"esiintymisjärjestyksessä",
"CTsortR"       : u"järjestä oikea konteksti",
"CTsortL"       : u"järjestä vasen konteksti",
"CTaktualisier" : u"Päivitä",
"CTmachQuery"   : u"Hakueditori",
"CTkopieren"    : u"Kopioi",
"CTzeigZitat"   : u"Näytä enemmän kontekstia",
"CTOptionen"    : u"Konkordanssiasetukset",

"ZTinfo"        : u"Sitaatin teksti",
"ZTkopieren"    : u"Kopioi",
"ZToeffnen"     : u"Avaa tiedosto",
"ZToeffnen2"    : u"\n(kaksoisnapsauta tiedostoa)\n",
"ZTInit"        : u"\n Kaksoisnapsauta yhtä osumista konkordanssivälilehdessä nähdäksesi saman osuman laajemmalla kontekstilla.",
"ClTFreqR"      :u"FreqR",
"ClTFreqL"      :u"FreqL",
"ClTKoef"       :u"Koef",
"ClTToken"      :u"Token",

"LCTSeparate"   :u"Separator",
"LCTSepBy"      :u"Separate by words",
"Source"        :u"Source",


##### Webdialog #####
"WDinfo"        : u"Lisää HTML tiedostoja suoraan internetistä\nSyötä sivun osoite:",
"WDfrageSeiten" : u"Kuinka monta sivua haluat lisätä korpukseesi?",
"WDanzahl"      : u"Haettavien sivujen lukumäärä",
"WDinSubdir"    : u"haettava alue: vain alihakemisto",
"WDaufServer"   : u"haettava alue: koko palvelin",
"WDok"          : u"Etsi",
"WDcancel"      : u"Sulje",

##### NewsDialog #####
"NDinfo"        : u"Lisää uutisryhmän viestit korpukseen",
"NDserver"      : u"uutispalvelin",  
"NDgruppe"      : u"uutisryhmä", 
"NDanzahl"      : u"viestien lukumäärä", 
"NDzitWeg"      : u"poista lainausmerkit viesteistä", 
"NDok"          : u"Etsi",
"NDcancel"      : u"Sulje",

##### QueryDialog #####
"QDinfo"        : u"Aputoiminto monimutkaisempia hakuja varten. \nKorvausmerkit ovat sallittuja (* ja ?).",
"QDsuchFelder"  : u"Hakutermit",
"QAusdruck1"    : u"ensimmäinen hakutermi",
"QAusdruck2"    : u"toinen hakutermi",
"QAbstand"      : u"Sanojen lukumäärä hakutermien välillä",
"QAbstandMin"   : u"min ja   ",
"QAbstandMax"   : u"max",
"QmachAusdruck" : u"Käynnistä etsintä",
"QDcancel"      : u"Sulje",

##### Fehler #####
"Error"         : u"Virhe",
"ErrKorpNew"    : u"Korpustiedostoa ei voitu luoda.",
"ErrKorpOpen"   : u"Korpustiedostoa ei voitu avata.\nOnko tiedosto TextSTAT korpus tiedosto?",
"ErrKorpImp"    : u"Korpustiedostoa ei voitu tuoda.",
"ErrNoKorp"     : u"Sinun täytyy ensiksi luoda korpus (tai avata aiemmin luotu korpus).",
"ErrKorpSave"   : u"Korpustiedostoa ei voitu tallentaa.",
"ErrFileOpen"   : u"Virhe avattaessa tiedostoa.",
"ErrSelect"     : u"Mitään ei ole valittuna.",
"ErrOptSave"    : u"Asetuksia ei voitu tallentaa.",
"ErrExport"     : u"Tiedoston vientivirhe",
"ErrNoFreqList" : u"Sanafrekvenssilistaa ei saatavilla",
"ErrNoKonkList" : u"Sanakonkordanssilistaa ei saatavilla",
"ErrExcel"      : u"MS Excel virhe.\n(Ovatko Python win32 laajennukset ja MS Excel asennettu oikein?)",
"ErrExcel65K"   : u"Virhe. MS Excel ei pysty käsittelemään kuin 65500 riviä. \nKäsiteltävänä on %s muotoa.",
"ErrWord"       : u"MS Word virhe.\n(Ovatko Python win32 laajennukset ja MS Word asennettu oikein?)",
"ErrExpFreq"    : u"Virhe tallennettaessa vietyä sanafrekvenssilistaa.",
"ErrExpKonk"    : u"Virhe tallennettaessa vietyä konkordanssilistaa.",
"ErrWeb"        : u"Virhe haettaessa HTML tiedostoja internetistä.",
"ErrNews"       : u"Virhe haettaessa uutisryhmän viestejä.",
"ErrQuery"      : u"Hakutermiä ei ole määritelty.",

##### Mitteilungen und Fragen #####
"AskSure"       : u"Oletko varma?",
"AskDelete"     : u"Haluatko varmasti poistaa tiedoston %s ?",
"StatusWeb"     : u"%s tiedosto(a) haetaan internetistä...",
"StatusNews"    : u"%s uutisryhmäviestiä haetaan...",
"DateiInfo"     : u"Tietoja tiedostosta",
"DateiInfo2"    : u"Tiedosto: %s\n\nPolku: %s\n\nKoko: %s\n",
"InfoText"      : u"TextSTAT\n\nKorpuksen luomisen tai avaamisen jälkeen voit lisätä siihen tiedostoja. Voit myös poistaa tiedostoja. Oikea hiirenpainike avaa kontekstivalikon. Korpuksen voi tallentaa kokonaisuudessaan. \n\nTekstin analysointiin liittyvät ominaisuudet: \n\n'Sananmuodot' välilehden alta löytyvät frekvenssimäärät tekstin saneille. 'Konkordanssi' näyttää KWIC konkordanssit (KeyWord in Context) ja 'Sitaatti' näyttää laajemmin konkordanssiosumaan liittyvää kontekstia.",

"StatusKorpImp" : u"Korpuksen tuonti onnistui.",
"StatusKorpSave": u"Korpus on tallennettu.",
"StatusFiles"   : u" %s tiedosto(a) | %s tavua ",
"StatusKorpDat" : u" Korpus: %s  (nykyinen CodePage asetus: %s)",
"KodierungInfo" : u"Voit nyt lisätä tiedostoja korpukseen.\n\nTekstinkäsittelytiedostoja:\n- MS Word tiedostoja (.doc tai .docx (.docx vain Windowsissa))\n- OpenOffice tiedostoja (.odt tai .sxw)\n\nTekstitiedostoja:\n- ASCII/ANSI tekstitiedostoja (yleensä .txt)\n- HTML tiedostoja (levyasemalta tai suoraan internetistä)\n- Uutisryhmän viestejä  (suoraan internetistä)\n\nKun lisäät tekstitiedoston, tarkista että käytät oikeaa koodausta.\nMerkistökoodaus on nyt: %s",
"StatusFormen"  : u" %s sananmuotoja/tyyppejä (%s sanoja/saneita korpuksessa)",
"StatusNoKorp"  : u" ei korpusta ",
"StatusSuchKonk": u"Hae konkordanssit...",
"StatusTreffer" : u" %s osumat ",
"StatusExpFreq" : u"Frekvenssilista on viety.",
"StatusExpKonk" : u"Konkordanssilista on viety.",
"ExportHinweis" : u"Käytä suhteuttamatonta kirjasintyyppiä (esim. Courier New)",
"StatusClip"    : u"Valinta on kopioitu leikepöydälle", 
"SpracheAendern": u"Vaihda kieli",
"SpracheInfo"   : u"Käynnistä TextSTAT uudelleen aktivoidaksesi kielen vaihto.",
"ProgBeenden"   : u"Poistu TextSTAT:sta",
"AbfrageEnde"   : u"Korpusta on muutettu. \nTallennetaanko muutokset \nennen TextSTAT:n sulkemista?",
"AbfrageSave"   : u"Korpusta on muutettu. \nTallennetaanko muutokset \nennen kuin uusi korpus avataan?",
}

##############################
########### Polski ##########
##############################
# Thanks to Erik-Jan Kuipers <erik.kuipers@uj.edu.pl> for the translation into Polish!

polski  = {
"Titel"         : u"TextSTAT",
"Titel_lang"    : u"TextSTAT (Proste Narzedzie Analizy Tekstu)",
"Version"       : Version,
"VersionDatum"  : u"Data wersji %s" % VersionDatum,
"Copyright"     : Copyright,
"eMail"         : eMail,
"ProgURL"       : ProgURL,
"ProgInfo"      : u"TextSTAT jest darmowym oprogramowaniem. Uzywaj na wlasne ryzyko.\nAutor programu nie przyjmuje zadnej odpowiedzialnosci za funkcjonowanie i skutki uzywania programu.\n\nTranslation into Polish by Erik-Jan Kuipers <erik.kuipers@uj.edu.pl>",

###### Menu #####
"Korpus"        : u"Korpus",
"KorpusNew"     : u"Nowy korpus",
"KorpusOpen"    : u"Otworz korpus",
"KorpusHinzu"   : u"Dodaj korpus",
"KorpusSave"    : u"Zapisz korpus",
"KorpusSaveAs"  : u" Zapisz jako",
"KorpusDel"     : u"Usun korpus",
"LetzteKorpora" : u"Ostatnie korpusy",

"DateiHinzu"    : u"Dodaj plik z dysku lokalnego",
"WebHinzu"      : u"Dodaj plik z internetu",
"NewsHinzu"     : u"Dodaj posty z grupy dyskusyjnej",
"DateiWeg"      : u"Usun plik(i)",

"OptSave"       : u"Zapisz opcje",
"Exit"          : u"Zakoncz",

"ImpEx"         : u"Eksportuj",
"Ex2csv"        : u"Lista frekwencyjna > plik CSV",
"Ex2txt"        : u"Lista konkordancyjna > plik TXT",
"Ex2excel"      : u"Lista frekwencyjna > MS Excel",
"Ex2word"       : u"Lista konkordancji > MS Word",
"ImpKorpus"     : u"Importuj korpus (TextSTAT 1.x)",

"Sprache"       : u"Jezyk",
"CodePage"      : u"Kodowanie plikow",
"Hilfe"         : u" ? ",
"RegExpHelp"    : u"Wyrazenia regularne - Pomoc",
"History"       : u"Historia (w j. niemieckim)",
"License"       : u"Licencja",
"Willkommen"    : u" Witamy w programie TextSTAT",


##### Toolbar #####
"KorpusNew2"    : u"Utworz nowy korpus",
"KorpusOpen2"   : u"Otworz istniejacy korpus",
"KorpusHinzu2"  : u"Dodaj istniejacy korpus do otwartego korpusu",
"KorpusSave2"   : u"Zapisz korpus",
"KorpusDel2"    : u"Usun korpus",
"WebHinzu2"     : u"Dodaj plik(i) HTML z internetu do korpusu",
"DateiHinzu2"   : u"Dodaj plik(i) z dysku lokalnego do korpusu",
"DateiWeg2"     : u"Usun plik(i) z korpusu",
"FreqZeigen"    : u"Pokaz frekwencji slow",
"FreqZeigen2"   : u"Pokaz frekwencji formy slow w korpusie",
"Kopieren"      : u"Kopiuj do schowka",
"Kopieren2"     : u"Kopiuj wybrane elementy do schowka",
"Ex2excel2"     : u"Eksportuj liste frekwencyjna do MS Excel",
"Ex2word2"      : u"Eksportuj liste konkordancji do MS Word",
"Info"          : u"TextSTAT - informacje",
"Info2"         : u"Informacje o programie",

##### Tabs #####
"KorpusTab"     : u"Korpus", 
"FormenTab"     : u"Formy slow",
"ConcTab"       : u"Konkordancja",
"ZitatTab"      : u"Cytat",
"ClustNGramsTab": u"Cluster/N-Grams",
"CollocatesTab" : u"Collocates",
"LConcTab" : u"KWIDC",
"TextGraphTab": u"Graph model",

"KTinfo"        : u"TextSTAT \n\nUtworz korpus i dodaj kilka plikow wzglednie otworz istniejacy korpus TextSTAT.",
"KTkopieren"    : u"Kopiuj nazwa pliku",
"KTopen"        : u"Otworz plik",
"KTdatinfo"     : u"Informacje o pliku",
"KTdatweg"      : u"Usun plik(i)",

"FTinfo"        : u"FREKWENCJA \nformy slow (tokenow)",
"FTsortFreq"    : u"sortuj wedlug frekwencji",
"FTsortAlpha"   : u"sortuj alfabetycznie",
"FTsortRetro"   : u"sortuj odwrotnie",
"FTminFreq"     : u"frekwencja minimalna",
"FTmaxFreq"     : u"frekwencja maksymalna",
"FTignGross"    : u"ignoruj duze litery (A=a)",
"FTsuchFreq"    : u"LUB szukaj frekwencja \nslow zawierajace ciag znakow:",
"FTfreqliste"   : u"Lista frekwencyjna",
"FTwortform"    : u"Forma slowa",
"FTfrequenz"    : u"Frekwencja",
"FTkopieren"    : u"Kopiuj",
"FTsuchKonk"    : u"Szukaj konkordancje",
"FTzeigInfo"    : u"Wiecej informacji",
"FTformInfo"    : u"Informacje o korpusie\n\nKorpus zawiera %s slow (tokeny)\n\n%s rozne formy (typy, z duzymi literami) wzglednie \n%s typy (duze litery sa zignorowane)\n\nForma '%s' ukazuje sie %s razy (= %.2f %%)",
"FTOptionen"    : u"Frekwencja / opcje",

"CTsuchen"      : u"Szukaj",
"CTganzWort"    : u"tylko calych wyrazow",
"CTignGross"    : u"Ignoruj duze litery (A=a)",
"CTcontextL"    : u"Kontekst po lewej stronie",
"CTcontextR"    : u"Kontekst po prawej stronie",
"CTmarkSuch"    : u"zaznac wyszukiwany ciag znakow",
"CTsortAlpha"   : u"alfabetycznie",
"CTsortR"       : u"sortuj kontekst z prawej strony",
"CTsortL"       : u"sortuj kontekst z lewej strony",
"CTaktualisier" : u"Odswiez",
"CTmachQuery"   : u"Edytor zapytan",
"CTkopieren"    : u"Kopiuj",
"CTzeigZitat"   : u"Pokaz wiecej kontekstu",
"CTOptionen"    : u"Opcje",

"ZTinfo"        : u"Tekst cytatu",
"ZTkopieren"    : u"Kopiuj",
"ZToeffnen"     : u"Otworz plik",
"ZToeffnen2"    : u"\n(Kliknij dwukrotnie, aby otworzyc plik)\n",
"ZTInit"        : u"\n Kliknij dwukrotnie na dowolne zdanie w zakladce konkordancje, by zobaczyc to zdanie w rozszerzonym.",
"ClTFreqR"      :u"FreqR",
"ClTFreqL"      :u"FreqL",
"ClTKoef"       :u"Koef",
"ClTToken"      :u"Token",

"LCTSeparate"   :u"Separator",
"LCTSepBy"      :u"Separate by words",
"Source"        :u"Source",


##### Webdialog #####
"WDinfo"        : u"Dodaj stron HTML bezposrednio z internetu.\nWprowadz adres URL:",
"WDfrageSeiten" : u"Ile stron chcesz dodac do swojego korpusu?",
"WDanzahl"      : u"Liczba stron do sciagania",
"WDinSubdir"    : u"Szukaj w tym folderze",
"WDaufServer"   : u"Szukaj na calym serwerze",
"WDok"          : u"Szukaj",
"WDcancel"      : u"Zamknij",

##### NewsDialog #####
"NDinfo"        : u"Dodaj postow grupy dyskusyjnej do korpusu", 
"NDserver"      : u"Serwer grup dyskusyjnych",  
"NDgruppe"      : u"Grupa dyskusyjna", 
"NDanzahl"      : u"Liczba postow", 
"NDzitWeg"      : u"Usun cytaty z postow", 
"NDok"          : u"Szukaj",
"NDcancel"      : u"Zamknij",

##### QueryDialog #####
"QDinfo"        : u"Pomoc w formulowaniu zlozonych pytan \nZnaki wieloznaczne (* i ?) sa dopuszczone",
"QDsuchFelder"  : u"Terminy wyszukiwawcze",
"QAusdruck1"    : u"Pierwszy termin wyszukiwawczy",
"QAusdruck2"    : u"Drugi termin wyszukiwawczy",
"QAbstand"      : u"Ilosc slow miedzy dwoma terminami",
"QAbstandMin"   : u"minimalnie i   ",
"QAbstandMax"   : u"maksymalnie",
"QmachAusdruck" : u"Zacznij wyszukiwanie",
"QDcancel"      : u"Zamknij",

##### Fehler #####
"Error"         : u"Blad",
"ErrKorpNew"    : u"Nie udalo sie utworzyc pliku korpusowego!",
"ErrKorpOpen"   : u"Nie udalo sie utworzyc pliku korpusowego!\nCzy to na pewno plik korpusu TextSTAT?",
"ErrKorpImp"    : u"Nie udalo sie zaimportowac pliku korpusowego!!",
"ErrNoKorp"     : u"Nalezy najpierw utworzyc nowy korpus (albo otworzyc istniejacy korpus).",
"ErrKorpSave"   : u"Nie udalo sie zapisac pliku korpusowego!",
"ErrFileOpen"   : u"Blad przy otwarciu pliku!",
"ErrSelect"     : u"Nie wybrano nic!",
"ErrOptSave"    : u"Nie udalo sie zapisac opcje!",
"ErrExport"     : u"Blad eksportu",
"ErrNoFreqList" : u"Lista frekwencyjna slow niedostepna",
"ErrNoKonkList" : u"Lista konkordancji niedostepna",
"ErrExcel"      : u"Blad MS Excel!\nZarowno rozszerzenie win32 w programie Pythona jak i MS Excel nalezy zainstalowac poprawnie.",
"ErrExcel65K"   : u"Blad! MS Excel nie moze zawierac wiecej niz 65500 wierszy. \nIlosc wierszy to obecnie: %s.",
"ErrWord"       : u"Blad MS Word!\nZarowno rozszerzenie win32 w programie Pythona jak i MS Excel nalezy zainstalowac poprawnie.",
"ErrExpFreq"    : u"Blad przy zapisaniu listy frekwencyjnej slow.",
"ErrExpKonk"    : u"Blad przy zapisaniu listy konkordancji.",
"ErrWeb"        : u"Blad przy sciaganiu plikow HTML z internetu.",
"ErrNews"       : u"Blad przy sciaganiu postow z grupy dyskusyjnej.",
"ErrQuery"      : u"Brak terminu wyszukiwawczego.",

##### Mitteilungen und Fragen #####
"AskSure"       : u"Czy jestes pewny?",
"AskDelete"     : u"Czy naprawde chcesz usunac %s ?",
"StatusWeb"     : u"ladowanie %s plikow z internetu...",
"StatusNews"    : u"ladowanie %s posty z grupy dyskusyjnej...",
"DateiInfo"     : u"Informacje o pliku",
"DateiInfo2"    : u"Plik: %s\n\nsciezka: %s\n\nRozmiar: %s\n",
"InfoText"      : u"TextSTAT\
\nPo utworzenia (lub otworzenia) korpusu, mozna dodawac nastepne pliki \
lub mozna tez usunac kilka plikow. Zaznac jakies plik i kliknij prawym przyciskiem myszy \
dla dalszych opcji. Mozna rowniez zapisac korpus w calosci. \
\nAnaliza tekstu mozna dokonac w roznych sposobach: \
\npod 'Formy slowa' znajdziesz \
frekwencje wystapien pojedynczych form slow. 'Konkordancja' pokazuje konkordancje typu KWIC \
(slowo kluczowe w kontekscie), 'Cytat' zaprezentuje wiecej kontekstu.",

"StatusKorpImp" : u"Korpus zaimportowany pomyslnie.",
"StatusKorpSave": u"Korpus zostal zapisany.",
"StatusFiles"   : u" %s plikow | %s bajtow ",
"StatusKorpDat" : u" Korpus: %s  (ustawienia kodowania pliku: %s)",
"KodierungInfo" : u"Teraz mozna dodac plikow do korpusu.\n\nDokumenty programu Word:\n- Pliki programu MS Word ('.doc' lub '.docx'\n- Pliki w formacie OpenOffice ('.odt' lub '.sxw')\n\nPliki tekstowe:\n- pliki tekstowe ASCII/ANSI (czesto '.txt')\n- Pliki HTML (z twardego dysku lub bezposrednio z internetu)\n- Posty grupy dyskusyjnej (bezposrednio z internetu)\nPrzy dodawanie plikow tekstowych, wybieraj poprawny \nkodowanie plikow.\nObecny kodowanie plikow to: %s",
"StatusFormen"  : u" %s formy slow/typy (%s slow/tokenow w korpusie)",
"StatusNoKorp"  : u" nie ma korpusu ",
"StatusSuchKonk": u"Szukaj konkordancje...",
"StatusTreffer" : u" %s wynikow ",
"StatusExpFreq" : u"Lista frekwencyjna zostal wyeksportowane.",
"StatusExpKonk" : u"Lista konkordancji zostal wyeksportowane",
"ExportHinweis" : u"Należy używać czcionki nieproporcjonalnej (jak np. Courier New)",
"StatusClip"    : u"Wybrany tekst został skopiowany do schowka",
"SpracheAendern": u"Zmień język",
"SpracheInfo"   : u"Aby aktywować zmiana języka, należy ponownie uruchomić TextSTAT.",
"ProgBeenden"   : u"Zakończ TextSTAT",
"AbfrageEnde"   : u"Korpus się zmienił. \nChcesz zapisać zmiany \nprzed zamknięciem TextSTAT?",
"AbfrageSave"   : u"Korpus się zmienił. \nChcesz zapisać zmiany w korpusu \nzanim otworzysz nowy korpus?",
}

##############################
###########  Spanish   #######
##############################
# Thanks to Pedro Lagonell <plagonell@yahoo.es> for the translation

espanol  = {
"Titel"         : u"TextSTAT",
"Titel_lang"    : u"TextSTAT (Herramienta de Análisis Textual)",
"Version"       : Version,
"VersionDatum"  : u"Fecha de versión %s" % VersionDatum,
"Copyright"     : Copyright,
"eMail"         : eMail,
"ProgURL"       : ProgURL,
"ProgInfo"      : u"TextSTAT y software libre.\nEl uso de este programa es por cuenta propia.\nEl Autor no asume ningún tipo de responsabilidad.\n\nTraduccion al Español por Pedro Lagonell <plagonell@yahoo.es>",

###### Menu #####
"Korpus"        : u"Unidad de Análisis",
"KorpusNew"     : u"Nueva Unidad de Análisis",
"KorpusOpen"    : u"Abrir Unidad de Análisis",
"KorpusHinzu"   : u"Adicionar Unidad de Análisis",
"KorpusSave"    : u"Grabar Unidad de Análisis",
"KorpusSaveAs"  : u"Grabar como",
"KorpusDel"     : u"Eliminar Unidad de Análisis",
# has to be translated:
"LetzteKorpora" : u"Unidad(es) reciente(s)",

"DateiHinzu"    : u"Adicionar archivo local",
"WebHinzu"      : u"Adicionar archivo de web",
"NewsHinzu"     : u"Adicionar publicación de un grupo de notícias",
"DateiWeg"      : u"Remover archivo(s)",

"OptSave"       : u"Grabar opciones",
"Exit"          : u"Salir",

"ImpEx"         : u"Exportar",
"Ex2csv"        : u"Lista de frecuencias > Archivo CSV",
"Ex2txt"        : u"Lista de concordancias > Archivo TXT",
"Ex2excel"      : u"Lista de frecuencias > MS Excel",
"Ex2word"       : u"Lista de concordancias > MS Word",
"ImpKorpus"     : u"Importar Unidad de Análisis (TextSTAT 1.x)",

"Sprache"       : u"Lenguaje",
"CodePage"      : u"Codificación",
"Hilfe"         : u" ? ",
"RegExpHelp"    : u"Expresiones regulares - Ayuda",
"History"       : u"Histórico (en Alemán)",
"License"       : u"Licencia",
"Willkommen"    : u" Bienvenid@s a TextSTAT",


##### Toolbar #####
"KorpusNew2"    : u"Crear nueva Unidad de Análisis",
"KorpusOpen2"   : u"Abrir Unidad de Análisis existente",
"KorpusHinzu2"  : u"Adicionar Unidad de Análisis existente a Unidad de Análisis actual",
"KorpusSave2"   : u"Grabar Unidad de Análisis",
"KorpusDel2"    : u"Eliminar archivo de la Unidad de Análisis",
"WebHinzu2"     : u"Adicionar archivo(s) HTML a una Unidad de Análisis de Internet",
"DateiHinzu2"   : u"Adicionar archivo local a la Unidad de Análisis",
"DateiWeg2"     : u"Eliminar archivo(s) de la Unidad de Análisis",
"FreqZeigen"    : u"Mostrar frecuencia de palabras",
"FreqZeigen2"   : u"Mostrar frecuencia de formas (de palabras) en la Unidad de Análisis",
"Kopieren"      : u"Copiar para el área de transferencia",
"Kopieren2"     : u"Copiar selección para el área de transferencia",
"Ex2excel2"     : u"Exportar lista de frecuencia para MS Excel",
"Ex2word2"      : u"Exportar concordancias para MS Word",
"Info"          : u"Información",
"Info2"         : u"Información con respecto a TextSTAT",

##### Tabs #####
"KorpusTab"     : u"Unidad de Analisis", 
"FormenTab"     : u"Formas",
"ConcTab"       : u"Concordancia",
"ZitatTab"      : u"Cita",
"ClustNGramsTab": u"Cluster/N-Grams",
"CollocatesTab" : u"Collocates",
"LConcTab" : u"KWIDC",
"TextGraphTab": u"Graph model",

"KTinfo"        : u"TextSTAT \n\nFavor, cree una Unidad de Análisis y adicione algunos archivos (o abra una Unidad de Análisis existente).",
"KTkopieren"    : u"Copiar o renombrar el archivo",
"KTopen"        : u"Abrir archivo",
"KTdatinfo"     : u"Información de archivo",
"KTdatweg"      : u"Remover archivo(s)",

"FTinfo"        : u"FRECUENCIA \nde formas (tokens)",
"FTsortFreq"    : u"organizar por frecuencia",
"FTsortAlpha"   : u"organizar alfabeticamente",
"FTsortRetro"   : u"orden reverso",
"FTminFreq"     : u"frecuencia min.",
"FTmaxFreq"     : u"frecuencia max.",
"FTignGross"    : u"organizar sin distinción de tipo\n(letras mayúsculas o minúsculas)",
"FTsuchFreq"    : u"buscar una frecuencia de\npalabras contenido de caracteres:",
"FTfreqliste"   : u"Lista de frecuencia",
"FTwortform"    : u"Formas",
"FTfrequenz"    : u"frecuencia",
"FTkopieren"    : u"Copiar",
"FTsuchKonk"    : u"Buscar concordancias",
"FTzeigInfo"    : u"Más información",
"FTformInfo"    : u"Información de Unidad de Análisis\n\nLa Unidad de Análisis contiene %s palabras (tokens)\n\n%s formas diferentes (tipos, letras mayúsculas son diferenciadas) \n%s tipos (letras minúsculas son ignoradas)\n\nLa forma '%s' aparece %s veces (= %.2f %%)",
"FTOptionen"    : u"frecuencia / opciones",

"CTsuchen"      : u"Consultar",
"CTganzWort"    : u"coincindir solamente con una palabra entera",
"CTignGross"    : u"no diferenciar letras mayúsculas y minúsculas",
"CTcontextL"    : u"contexto a izquierda",
"CTcontextR"    : u"contexto a derecha",
"CTmarkSuch"    : u"destacar de la palabra consultada",
"CTsortAlpha"   : u"alfabeticamente",
"CTsortR"       : u"organizar el contexto a la derecha",
"CTsortL"       : u"organizar el contexto a ls izquierda",
"CTaktualisier" : u"Actualizar",
"CTmachQuery"   : u"Editor de consultas",
"CTkopieren"    : u"Copiar",
"CTzeigZitat"   : u"Mostrar contexto más amplio",
"CTOptionen"    : u"Opciones",

"ZTinfo"        : u"Texto de citación",
"ZTkopieren"    : u"Copiar",
"ZToeffnen"     : u"Abrir archivo",
"ZToeffnen2"    : u"\n(Presione click dos veces para abrir el archivo)\n",
# Has to be translated:
"ZTInit"        : u"\n Presione click dos veces en una de la opciones generadas en la pestaña de Concordancia, para mostrarla con mayor información (contexto).",
"ClTFreqR"      :u"FreqR",
"ClTFreqL"      :u"FreqL",
"ClTKoef"       :u"Koef",
"ClTToken"      :u"Token",

"LCTSeparate"   :u"Separator",
"LCTSepBy"      :u"Separate by words",
"Source"        :u"Source",


##### Webdialog #####
"WDinfo"        : u"Adicionar archivo(s) HTML directamente de Internet.\nFavor digite la dirección (URL):",
"WDfrageSeiten" : u"Cuantas páginas quiere adicionar a su Unidad de Análisis?",
"WDanzahl"      : u"número de páginas a recuperar",
"WDinSubdir"    : u"dominio: solamente subdirectorio",
"WDaufServer"   : u"dominio: servidor interno",
"WDok"          : u"Ok",
"WDcancel"      : u"Cancelar",

##### NewsDialog #####
"NDinfo"        : u"Adicionar publicaciones de un grupo de noticias a la Unidad de Análisis", 
"NDserver"      : u"servidor de notícias",  
"NDgruppe"      : u"grupo de notícias", 
"NDanzahl"      : u"número de publicaciones (postings)", 
"NDzitWeg"      : u"remover citaciones de publicaciones", 
"NDok"          : u"Ok",
"NDcancel"      : u"Cancelar",

##### QueryDialog #####
"QDinfo"        : u"Función de ayuda para formular consultas complejas\nCaracteres comodines (wildcards) se permiten aqui (* e ?)",
"QDsuchFelder"  : u"Consulta",
"QAusdruck1"    : u"primero palabta",
"QAusdruck2"    : u"segundo palabra",
"QAbstand"      : u"Número de palabras entre las palabras consultadas",
"QAbstandMin"   : u"min. e  ",
"QAbstandMax"   : u"max.",
"QmachAusdruck" : u"Iniciar consulta",
"QDcancel"      : u"Cancelar",

##### Fehler #####
"Error"         : u"Error",
"ErrKorpNew"    : u"El Archivo de la Unidad de Análisis no puede ser creado!",
"ErrKorpOpen"   : u"El archivo de la Unidad de Análisis no puede ser abierto!\nEs este un archivo de Unidad de Análisis de TextSTAT?",
"ErrKorpImp"    : u"El archivo de la Unidad de Análisis no puede ser importado!",
"ErrNoKorp"     : u"Debe crear primero una Unidad de Análisis (o abrir una Unidad de Análisis existente).",
"ErrKorpSave"   : u"El archivo de la Unidad de Análisis no puede ser grabado!",
"ErrFileOpen"   : u"Error al abrir el archivo!",
"ErrSelect"     : u"Nada selecionado!",
"ErrOptSave"    : u"Opciones no fueron grabadas !!",
"ErrExport"     : u"Error al exportar",
"ErrNoFreqList" : u"No hay ninguna lista de frecuencia disponible",
"ErrNoKonkList" : u"No hay ninguna lista de concordancias disponible",
"ErrExcel"      : u"Error de MS Excel!\n(Las extensiones win32 de Python o MS Excel están instaladas correctamente?)",
"ErrExcel65K"   : u"Error! MS Excel no puede contener mas de 65500 lineas. \nHay %s formas.",
"ErrWord"       : u"Error de MS Word!\n(Las extensiones win32 de Python o MS Word están instaladas correctamente?)",
"ErrExpFreq"    : u"Error al grabar la lista de frecuencias de palabras exportada.",
"ErrExpKonk"    : u"Error al grabar la lista de concordancias exportada.",
"ErrWeb"        : u"Error al buscar archivos HTML de Internet.",
"ErrNews"       : u"Error al buscar publicaciones de grupos de noticias.",
"ErrQuery"      : u"No existe ninguna palabra de búsqueda definida.",


##### Mitteilungen und Fragen #####
"AskSure"       : u"Está seguro?",
"AskDelete"     : u"Realmente quiere eliminar %s ?",
"StatusWeb"     : u"%s archivos estan siendo recuperados de Internet...",
"StatusNews"    : u"%s publicaciones de grupos de noticias estan siendo recuperadas...",
"DateiInfo"     : u"Información del archivo",
"DateiInfo2"    : u"archivo: %s\n\nDirectorio: %s\n\nTamaño: %s\n",
"InfoText"      : u"TextSTAT\
\n\n\nDespués de crear o abrir una Unidad de Análisis, puede adicionar archivos a ella. \
También puede remover de la Unidad de Análisis los archivos que desee, o presionar el boton derecho del mouse para desplegar un menú de opciones. \
La Unidad de Análisis puede ser guardada como un todo. \
\n\nExisten algunos utilitarios para análisis textual: \n\nEn 'Formas' encontrará \
números de frecuencias para palabras claves en sus textos. \nEn 'Concordancias' encontrará concordancias KWIC \
(palabras - clave contextualizadas). \n'Cita' presenta contextos amplificados.",

"StatusKorpImp" : u"La Unidad de Análisis fue importada con éxito.",
"StatusKorpSave": u"La Unidad de Análisis fue grabada.",
"StatusFiles"   : u" %s archivos | %s bytes ",
"StatusKorpDat" : u" Unidad de Análisis: %s  (actual definición de codificación: %s)",
"KodierungInfo" : u"Ahora puede adicionar algunos archivos a la Unidad de Análisis.\n\narchivos de procesadores de texto:\n- archivos de MS Word ('.doc', '.docx'; solo en  Windows)\n- archivos de OpenOffice ('.sxw', '.odt')\n\narchivos de texto:\n- archivos de texto ASCII/ANSI (extensión '.txt')\n- archivos HTML (localizados en su HD o directamente de Internet)\n- Publicaciones de grupos de notícias (directamente de Internet)\nAl adicionar archivos de texto, veifique que usa una codificación correcta.\nLa definición actual es: %s",
"StatusFormen"  : u" %s formas/tipos (%s palabras/tokens en la Unidad de Análisis)",
"StatusNoKorp"  : u" No existe ninguna Unidad de Análisis ",
"StatusSuchKonk": u"Buscar concordancias...",
"StatusTreffer" : u" %s encontrados ",
"StatusExpFreq" : u"La lista de frecuencias fue exportada.",
"StatusExpKonk" : u"La lista de concordancias fue exportada",
"ExportHinweis" : u"Debe utilizar una fuente no-proporcional (como Courier New)",
"StatusClip"    : u"La selección fue copiada al área de transferencia (clipboard)", 
"SpracheAendern": u"Cambiar de lenguaje",
"SpracheInfo"   : u"Debe reiniciar TextSTAT para activar el cambio de lenguaje.",
"ProgBeenden"   : u"Salir de TextSTAT",
"AbfrageEnde"   : u"La Unidad de Análisis fue cambiada. \nVa a grabar la Unidad de Análisis \nantes de salir de TextSTAT?",
"AbfrageSave"   : u"La Unidad de Análisis fue cambiada. \nVa a grabar la Unidad de Análisis \nantes de abrir otra Unidad de Análisis?",
}

##############################
########### Italian ##########
##############################
# Italian translation by Daniele Lucchini <lucchini@litterae.eu>
# Other translators/proofreaders, please, email me if you make changes to the Italian translation.

italiano  = {
"Titel"         : u"TextSTAT",
"Titel_lang"    : u"TextSTAT (Simple Text Analysis Tool)",
"Version"       : Version,
"VersionDatum"  : u"Data della versione %s" % VersionDatum,
"Copyright"     : Copyright,
"eMail"         : eMail,
"ProgURL"       : ProgURL,
"ProgInfo"      : u"TextSTAT è un programma gratuito.\nL'utilizzo è a proprio rischio.\nL'autore non si assume responsabilità.",

###### Menu #####
"Korpus"        : u"Corpus",
"KorpusNew"     : u"Nuovo corpus",
"KorpusOpen"    : u"Apri corpus",
"KorpusHinzu"   : u"Aggiungi corpus",
"KorpusSave"    : u"Salva corpus",
"KorpusSaveAs"  : u"Salva come",
"KorpusDel"     : u"Cancella corpus",
"LetzteKorpora" : u"Corpora recenti",

"DateiHinzu"    : u"Aggiungi file locale",
"WebHinzu"      : u"Aggiungi file da internet",
"NewsHinzu"     : u"Aggiungi messaggi da newsgroup",
"DateiWeg"      : u"Rimuovi file",

"OptSave"       : u"Salva opzioni",
"Exit"          : u"Esci",

"ImpEx"         : u"Esporta",
"Ex2csv"        : u"Lista frequenze > file CSV",
"Ex2txt"        : u"Lista concordanze > file TXT",
"Ex2excel"      : u"Lista frequenze > MS Excel",
"Ex2word"       : u"Lista concordanze > MS Word",
"ImpKorpus"     : u"Importa corpus (TextSTAT 1.x)",

"Sprache"       : u"Lingua",
"CodePage"      : u"Codifica",
"Hilfe"         : u" ? ",
"RegExpHelp"    : u"Espressioni regolari - Aiuto",
"History"       : u"Storico (in tedesco)",
"License"       : u"Licenza",
"Willkommen"    : u"Benvenuto in TextSTAT",


##### Toolbar #####
"KorpusNew2"    : u"Crea nuovo corpus",
"KorpusOpen2"   : u"Apri corpus esistente",
"KorpusHinzu2"  : u"Aggiungi corpus esistente al corpus attuale",
"KorpusSave2"   : u"Salva corpus",
"KorpusDel2"    : u"Cancella file corpus",
"WebHinzu2"     : u"Aggiungi al corpus file HTML da internet",
"DateiHinzu2"   : u"Aggiungi al corpus file locali",
"DateiWeg2"     : u"Cancella file dal corpus",
"FreqZeigen"    : u"Mostra frequenze parole",
"FreqZeigen2"   : u"Mostra frequenze forme verbali nel corpus",
"Kopieren"      : u"Copia negli appunti",
"Kopieren2"     : u"Copia selezione negli appunti",
"Ex2excel2"     : u"Esporta lista frequenze in MS Excel",
"Ex2word2"      : u"Esporta concordanze in MS Word",
"Info"          : u"Informazioni",
"Info2"         : u"Informazioni su TextSTAT",

##### Tabs #####
"KorpusTab"     : u"Corpus", 
"FormenTab"     : u"Forme verbali",
"ConcTab"       : u"Concordanza",
"ZitatTab"      : u"Citazione",
"ClustNGramsTab": u"Cluster/N-Grams",
"CollocatesTab" : u"Collocates",
"LConcTab" : u"KWIDC",
"TextGraphTab": u"Graph model",

"KTinfo"        : u"TextSTAT \n\nCrea un corpus e aggiungi almeno un file (oppure apri un corpus esistente).",
"KTkopieren"    : u"Copia nome file",
"KTopen"        : u"Apri file",
"KTdatinfo"     : u"Informazioni file",
"KTdatweg"      : u"Rimuovi file",

"FTinfo"        : u"FREQUENZA \nforme verbali (occorrenze)",
"FTsortFreq"    : u"ordina per frequenza",
"FTsortAlpha"   : u"ordina alfabeticamente",
"FTsortRetro"   : u"ordina alfabeticamente per terminazione",
"FTminFreq"     : u"frequenza minima",
"FTmaxFreq"     : u"frequenza massima",
"FTignGross"    : u"ignora maiuscole-minuscole",
"FTsuchFreq"    : u"oppure cerca la frequenza \nparole contenenti la stringa:",
"FTfreqliste"   : u"Lista frequenze",
"FTwortform"    : u"Forma verbale",
"FTfrequenz"    : u"Frequenza",
"FTkopieren"    : u"Copia",
"FTsuchKonk"    : u"Cerca concordanze",
"FTzeigInfo"    : u"Maggiori informazioni",
"FTformInfo"    : u"Informazioni corpus\n\nIl corpus contiene %s parole (occorrenze)\n\n%s forme diverse (varianti e maiuscole sono differenziate) \n%s varianti (le maiuscole sono ignorate)\n\nLa forma '%s' appare %s volte (= %.2f %%)",
"FTOptionen"    : u"Frequenza / opzioni",

"CTsuchen"      : u"Cerca",
"CTganzWort"    : u"cerca solo parole intere",
"CTignGross"    : u"cerca ignorando maiuscole-minuscole",
"CTcontextL"    : u"contesto a sinistra",
"CTcontextR"    : u"contesto a destra",
"CTmarkSuch"    : u"evidenzia stringa di ricerca",
"CTsortAlpha"   : u"alfabeticamente",
"CTsortR"       : u"ordina contesto a destra",
"CTsortL"       : u"ordina contesto a sinistra",
"CTaktualisier" : u"Aggiorna",
"CTmachQuery"   : u"Editore interrogazioni",
"CTkopieren"    : u"Copia",
"CTzeigZitat"   : u"Mostra contesto ampliato",
"CTOptionen"    : u"Opzioni",

"ZTinfo"        : u"Testo citazione",
"ZTkopieren"    : u"Copia",
"ZToeffnen"     : u"Apri file",
"ZToeffnen2"    : u"\n(Doppio clic per aprire file)\n",
"ZTInit"        : u"\n Doppio clic su una voce nella tabella concordanze per visualizzarla qui con contesto ampliato.",
"ClTFreqR"      :u"FreqR",
"ClTFreqL"      :u"FreqL",
"ClTKoef"       :u"Koef",
"ClTToken"      :u"Token",

"LCTSeparate"   :u"Separator",
"LCTSepBy"      :u"Separate by words",
"Source"        :u"Source",


##### Webdialog #####
"WDinfo"        : u"Aggiungi file HTML direttamente da internet.\nInserisci URL:",
"WDfrageSeiten" : u"Quante pagine desideri aggiungere al corpus?",
"WDanzahl"      : u"numero di pagine da recuperare",
"WDinSubdir"    : u"dominio: solo sottodirectory",
"WDaufServer"   : u"dominio: tutto il server",
"WDok"          : u"Cerca",
"WDcancel"      : u"Chiudi",

##### NewsDialog #####
"NDinfo"        : u"Aggiungi al corpus messaggi da newsgroup", 
"NDserver"      : u"server delle news",  
"NDgruppe"      : u"newsgroup", 
"NDanzahl"      : u"numero di messaggi", 
"NDzitWeg"      : u"rimuovi citazioni dai messaggi", 
"NDok"          : u"Cerca",
"NDcancel"      : u"Chiudi",

##### QueryDialog #####
"QDinfo"        : u"Funzione d'aiuto per formulare interrogazioni complesse \nQui sono consentiti caratteri jolly (* e ?)",
"QDsuchFelder"  : u"Termine di ricerca",
"QAusdruck1"    : u"primo termine di ricerca",
"QAusdruck2"    : u"secondo termine di ricerca",
"QAbstand"      : u"Numero di parole tra i due termini di ricerca",
"QAbstandMin"   : u"minimo e   ",
"QAbstandMax"   : u"massimo",
"QmachAusdruck" : u"Avvia ricerca",
"QDcancel"      : u"Chiudi",

##### Fehler #####
"Error"         : u"Errore",
"ErrKorpNew"    : u"Impossibile creare file corpus!",
"ErrKorpOpen"   : u"Impossibile aprire file corpus!\nSei certo che sia un file corpus di TextSTAT?",
"ErrKorpImp"    : u"Impossibile importare file corpus!",
"ErrNoKorp"     : u"Creare prima un corpus (o aprire un corpus esistente).",
"ErrKorpSave"   : u"Impossibile salvare file corpus!",
"ErrFileOpen"   : u"Errore apertura file!",
"ErrSelect"     : u"Nessuna selezione!",
"ErrOptSave"    : u"Impossibile salvare opzioni!",
"ErrExport"     : u"Errore esportazione",
"ErrNoFreqList" : u"Nessuna lista frequenze disponibile",
"ErrNoKonkList" : u"Nessuna lista concordanze disponibile",
"ErrExcel"      : u"Errore MS Excel!\n(Le estensioni Python win32 per MS Excel sono installate correttamente?)",
"ErrExcel65K"   : u"Errore! MS Excel non può gestire più di 65500 righe. \nCi sono %s forme.",
"ErrWord"       : u"Errore MS Word!\n(Le estensioni Python win32 per MS Word sono installate correttamente?)",
"ErrExpFreq"    : u"Errore salvataggio lista frequenze da esportare.",
"ErrExpKonk"    : u"Errore salvataggio lista concordanze da esportare.",
"ErrWeb"        : u"Errore recupero file HTML da internet.",
"ErrNews"       : u"Errore recupero messaggi dal newsgroup.",
"ErrQuery"      : u"Nessun termine di ricerca definito.",


##### Mitteilungen und Fragen #####
"AskSure"       : u"Sei sicuro?",
"AskDelete"     : u"Desideri cancellare davvero %s ?",
"StatusWeb"     : u"Recupero di %s file da internet...",
"StatusNews"    : u"Recupero di %s messaggi dal newsgroup...",
"DateiInfo"     : u"Informazioni file",
"DateiInfo2"    : u"File: %s\n\nPercorso: %s\n\nDimensioni: %s\n",
"InfoText"      : u"TextSTAT\
\nDopo aver creato (o aperto) un corpus, potrai aggiungervi dei file. \
Naturalmente potrai anche rimuoverne. Premi il tasto destro del mouse per avere il menù contestuale. \
Puoi salvare il corpus unitariamente. \
\nCi sono alcuni strumenti per l'analisi testuale: in 'Forme verbali' trovi \
i numeri delle frequenze occorrenze nei tuoi testi. 'Concordanza' mostra l'indice delle concordanze permutate \
(KWIC), 'Citazione' presenta il contesto ampliato.",

"StatusKorpImp" : u"Corpus importato con successo.",
"StatusKorpSave": u"Corpus salvato.",
"StatusFiles"   : u" %s file | %s byte ",
"StatusKorpDat" : u" Corpus: %s  (impostazione codifica attuale: %s)",
"KodierungInfo" : u"Ora puoi aggiungere dei file al corpus.\n\nFile word processor:\n- File MS Word ('.doc' o '.docx'; solo Windows)\n- File OpenOffice ('.odt o .sxw')\n\nFile testo:\n- File testo ASCII/ANSI (spesso '.txt')\n- File HTML (dal disco locale o direttamente da internet)\n- Messaggi newsgroup (direttamente da internet)\nQuando aggiungi file testo, assicurati che siano codificati correttamente.\nImpostazione attuale: %s",
"StatusFormen"  : u" %s forme verbali/varianti (%s parole/occorrenze nel corpus)",
"StatusNoKorp"  : u" nessun corpus ",
"StatusSuchKonk": u"Ricerca concordanze...",
"StatusTreffer" : u" %s volte ",
"StatusExpFreq" : u"Lista frequenze esportata",
"StatusExpKonk" : u"Lista concordanze esportata",
"ExportHinweis" : u"Meglio usare un carattere monospazio (come Courier New)",
"StatusClip"    : u"Selezione copiata negli appunti", 
"SpracheAendern": u"Cambia lingua",
"SpracheInfo"   : u"Riavvia TextSTAT per effettuare il cambio di lingua.",
"ProgBeenden"   : u"Esci da TextSTAT",
"AbfrageEnde"   : u"Corpus modificato. \nDesideri salvare il corpus \nprima di uscire da TextSTAT?",
"AbfrageSave"   : u"Corpus modificato. \nDesideri salvare il corpus \nprima di aprirne uno nuovo?",
}


##############################
########### Czech ##########
##############################
# Czech translation by Vlastimil Brom, <brom@phil.muni.cz>
#

czech  = {
"Titel"         : u"TextSTAT",
"Titel_lang"    : u"TextSTAT (jednoduchý nástroj pro textovou analýzu)",
"Version"       : Version,
"VersionDatum"  : u"Verze z %s" % VersionDatum,
"Copyright"     : Copyright,
"eMail"         : eMail,
"ProgURL"       : ProgURL,
"ProgInfo"      : u"TextSTAT je svobodný software.\nAutor nepřejímá záruky jakéhokoli druhu.",

###### Menu #####
"Korpus"        : u"Korpus",
"KorpusNew"     : u"Nový korpus",
"KorpusOpen"    : u"Otevřít korpus",
"KorpusHinzu"   : u"Přidat korpus",
"KorpusSave"    : u"Uložit korpus",
"KorpusSaveAs"  : u"Uložit jako",
"KorpusDel"     : u"Smazat korpus",
"LetzteKorpora" : u"Poslední korpusy",

"DateiHinzu"    : u"Přidat soubor z disku",
"WebHinzu"      : u"Přidat soubor z webu",
"NewsHinzu"     : u"Přidat texty z newsgroup",
"DateiWeg"      : u"Odstranit soubor(y)",

"OptSave"       : u"Uložit nastavení",
"Exit"          : u"Ukončit",

"ImpEx"         : u"Exportovat",
"Ex2csv"        : u"Frekvenční seznam > soubor CSV",
"Ex2txt"        : u"Konkordance > soubor TXT",
"Ex2excel"      : u"Frekvenční seznam > MS Excel",
"Ex2word"       : u"Konkordance > MS Word",
"ImpKorpus"     : u"Importovat korpus (TextSTAT 1.x)",

"Sprache"       : u"Jazyk",
"CodePage"      : u"Kódování souboru",
"Hilfe"         : u" ? ",
"RegExpHelp"    : u"Regular Expressions - Nápověda",
"History"       : u"Přehled změn",
"License"       : u"Licence",
"Willkommen"    : u" Vítejte v TextSTATu",


##### Toolbar #####
"KorpusNew2"    : u"Založit nový korpus",
"KorpusOpen2"   : u"Otevřít existující korpus",
"KorpusHinzu2"  : u"Přidat existující korpus k aktuálně otevřenému",
"KorpusSave2"   : u"Uložit aktuálně otevřený korpus",
"KorpusDel2"    : u"Definitivně smazat korpus",
"WebHinzu2"     : u"Přidat ke korpusu soubor(y) HTML z internetu",
"DateiHinzu2"   : u"Přidat ke korpusu soubor(y) z pevného disku",
"DateiWeg2"     : u"Odstranit soubor(y) z korpusu",
"FreqZeigen"    : u"Vypsat slovní frekvence",
"FreqZeigen2"   : u"Vypsat frekvence jednotlivých slovních tvarů v korpusu",
"Kopieren"      : u"Kopírovat (do schránky)",
"Kopieren2"     : u"Kopírovat výběr do schránky",
"Ex2excel2"     : u"Exportovat frekvenční seznam do MS Excel",
"Ex2word2"      : u"Exportovat konkordance do MS Word",
"Info"          : u"Informace k programu TextSTAT",
"Info2"         : u"Informace k programu",

##### Tabs #####
"KorpusTab"     : u"Korpus", 
"FormenTab"     : u"Tvary slov",
"ConcTab"       : u"Konkordance",
"ZitatTab"      : u"Doklad",
"ClustNGramsTab": u"Cluster/N-Grams",
"CollocatesTab" : u"Collocates",
"LConcTab" : u"KWIDC",
"TextGraphTab": u"Graph model",

"KTinfo"        : u"TextSTAT \n\nNaplňte korpus soubory nebo otevřete existující korpus TextSTAT.",
"KTkopieren"    : u"Kopírovat názvy souborů",
"KTopen"        : u"Otevřít soubor",
"KTdatinfo"     : u"Informace o souboru",
"KTdatweg"      : u"Odstranit soubor(y)",

"FTinfo"        : u"FREKVENCE \nslovních tvarů (Token)",
"FTsortFreq"    : u"třídit frekvenčně",
"FTsortAlpha"   : u"třídit abecedně",
"FTsortRetro"   : u"třídit retrográdně",
"FTminFreq"     : u"min. frekvence",
"FTmaxFreq"     : u"max. frekvence",
"FTignGross"    : u"Ignorovat velikost (A=a)",
"FTsuchFreq"    : u"NEBO vypsat frekvenci \nslov obsahujících:",
"FTfreqliste"   : u"Frekvenční seznam",
"FTwortform"    : u"Slovní tvar",
"FTfrequenz"    : u"Frekvence",
"FTkopieren"    : u"Kopírovat",
"FTsuchKonk"    : u"Vypsat konkordance",
"FTzeigInfo"    : u"Podrobnější informace",
"FTformInfo"    : u"Informace o korpusu\n\nVelikost korpusu: %s běžných slov (Tokens)\n\n%s různých tvarů (Types, s rozlišením velikosti písmen) resp. \n%s Types (s ignorováním velikosti písmen)\n\nTvar '%s' se vyskytuje %skrát (= %.2f %%)",
"FTOptionen"    : u"Frekvence / Možnosti",

"CTsuchen"      : u"Vyhledat",
"CTganzWort"    : u"jen celá slova",
"CTignGross"    : u"Ignorovat velikost písmen (A=a)",
"CTcontextL"    : u"levý kontext",
"CTcontextR"    : u"pravý kontext",
"CTmarkSuch"    : u"Vyznačit hledaný výraz",
"CTsortAlpha"   : u"třídit abecedně",
"CTsortR"       : u"třídit podle pravého kontextu",
"CTsortL"       : u"třídit podle levého kontextu",
"CTaktualisier" : u"Aktualizovat",
"CTmachQuery"   : u"Editor vyhledávání",
"CTkopieren"    : u"Kopírovat",
"CTzeigZitat"   : u"Zobrazit širší kontext",
"CTOptionen"    : u"Možnosti  vyhledávání",

"ZTinfo"        : u"Text dokladu",
"ZTkopieren"    : u"Kopírovat",
"ZToeffnen"     : u"Otevřít soubor",
"ZToeffnen2"    : u"\n(dvojklikem se soubor otevře)\n",
"ZTInit"        : u"\n Dvojklikem na řádku konkordance se zobrazí tentýž text s širším kontextem.","ClTFreqR"      :u"FreqR",
"ClTFreqL"      :u"FreqL",
"ClTKoef"       :u"Koef",
"ClTToken"      :u"Token",

"LCTSeparate"   :u"Separator",
"LCTSepBy"      :u"Separate by words",
"Source"        :u"Source",


##### Webdialog #####
"WDinfo"        : u"Přidejte stránky HTML přímo z internetu.\nZadejte adresu URL:",
"WDfrageSeiten" : u"Kolik stránek chcete zařadit do svého korpusu?",
"WDanzahl"      : u"Počet stránek ke stažení",
"WDinSubdir"    : u"hledat v zadaném podadresáři",
"WDaufServer"   : u"hledat na celém serveru",
"WDok"          : u"Hledat",
"WDcancel"      : u"Zavřít",

##### NewsDialog #####
"NDinfo"        : u"Přidat příspěvky z newsgroups", 
"NDserver"      : u"Server News",  
"NDgruppe"      : u"Newsgroup", 
"NDanzahl"      : u"Počet příspěvků", 
"NDzitWeg"      : u"Odstranit citáty", 
"NDok"          : u"Hledat",
"NDcancel"      : u"Zavřít",

##### QueryDialog #####
"QDinfo"        : u"Pomoc při vytváření komplexních vyhledávacích dotazů\nJe možné používat zástupné znaky (* a ?)",
"QDsuchFelder"  : u"hledané výrazy",
"QAusdruck1"    : u"první výraz",
"QAusdruck2"    : u"druhý výraz",
"QAbstand"      : u"počet slov mezi výrazy",
"QAbstandMin"   : u"alespoň a   ",
"QAbstandMax"   : u"nanejvýš",
"QmachAusdruck" : u"vytvořit vyhledávací dotaz",
"QDcancel"      : u"Zavřít",


##### Fehler #####
"Error"         : u"Chyba",
"ErrKorpNew"    : u"Soubor korpusu nemohl být založen!",
"ErrKorpOpen"   : u"Korpus nemohl být otevřen!\nJste si jisti, ze jde o soubor korpusu TextSTAT?",
"ErrKorpImp"    : u"Korpus nemohl být importován!",
"ErrNoKorp"     : u"Nejdříve je třeba založit nový korpus nebo otevřít existující.",
"ErrKorpSave"   : u"Soubor korpusu nemohl být uložen!",
"ErrFileOpen"   : u"Chyba při otvírání souboru!",
"ErrSelect"     : u"Nic nebylo vybráno!",
"ErrOptSave"    : u"Nastavení nemohla být uložena",
"ErrExport"     : u"Chyba exportu",
"ErrNoFreqList" : u"Žádný frekvenční seznam není k dispozici",
"ErrNoKonkList" : u"Žádný seznam konkordancí není k dispozici",
"ErrExcel"      : u"Chyba MS Excel!\nJak rozšíření Python win32 tak MS Excel musejí být řádně nainstalovány.",
"ErrExcel65K"   : u"Chyba! MS Excel může zpracovat nanejvýš 65500 řádků. \nK dispozici je ale %s řádků.",
"ErrWord"       : u"Chyba MS Word!\nJak rozšíření Python win32 tak MS Word musejí být řádně nainstalovány.",
"ErrExpFreq"    : u"Při ukládání frekvenčního seznamu došlo k chybě.",
"ErrExpKonk"    : u"Při ukládání seznamu konkordancí došlo k chybě.",
"ErrWeb"        : u"Při stahování souborů HTML z internetu došlo k chybě.",
"ErrNews"       : u"Při načítání zpráv z newsgroups došlo k chybě.",
"ErrQuery"      : u"Nebyl zadán žádný vyhledávací výraz.",


##### Mitteilungen und Fragen #####
"AskSure"       : u"Jste si jisti?",
"AskDelete"     : u"Opravdu chcete smazat %s ?",
"StatusWeb"     : u"Načítají se soubory z internetu (%s) ...",
"StatusNews"    : u"Načítají se soubory z newsgroups (%s) ... ",
"DateiInfo"     : u"Informace o souboru",
"DateiInfo2"    : u"Soubor: %s\n\nUmístění: %s\n\nVelikost: %s\n",
"InfoText"      : u"TextSTAT\
\nPo založení korpusu nebo otevření dříve vytvořeného lze nyní přidávat další soubory \
nebo některé odstranit. Po vybrání souboru a stisknutí pravého tlačítka myši \
se zobrazí další možnosti. \nKorpus může být i uložen jako celek.\
\nAnalýza textů je možná na více úrovních: \nPoložka 'Tvary slov' obsahuje údaje \
o frekvenci jednotlivých tvarů slov. 'Konkordance' představuje konkordanční řádky KWIC \
(KeyWord in Context), 'Doklad' pak širší textové okolí.",

"StatusKorpImp" : u"Korpus byl úspěšně importován.",
"StatusKorpSave": u"Korpus byl uložen.",
"StatusFiles"   : u" počet souborů: %s | velikost: %s B ",
"StatusKorpDat" : u" Korpus: %s  (Nastavené kódování souborů: %s)",
"KodierungInfo" : u"Nyní můžete přidat soubory.\n\nDokumentové soubory:\n- soubory MS Word ('.doc' nebo '.docx')\n- soubory OpenOffice ('.odt' nebo '.sxw')\n\ntextové soubory:\n- texty v ASCII/ANSI-formátu (většinou '.txt')\n- soubory HTML (z pevného disku nebo přímo z internetu)\n- příspěvky v newsgroups (přímo z internetu)\nU prostých souborů je třeba dodržet správné \nnastavení kódování.\nAktuálně nastavené kódování je: %s",
"StatusFormen"  : u" %s slovních tvarů/Types (%s běžných slov/Tokens v korpusu)",
"StatusNoKorp"  : u" žádný korpus ",
"StatusSuchKonk": u"Vyhledávání konkordancí ...",
"StatusTreffer" : u" %s nálezů ",
"StatusExpFreq" : u"Frekvenční seznam byl exportován.",
"StatusExpKonk" : u"Seznam Konkordancí byl exportován.",
"ExportHinweis" : u"K zobrazení použijte nejlépe neproporční písmo (např. Courier New)",
"StatusClip"    : u"Výběr byl zkopírován do schránky", 
"SpracheAendern": u"Změnit jazyk",
"SpracheInfo"   : u"Program je třeba restartovat pro uplatnění změny jazyka.\n\nYou have to restart TextSTAT to activate the language change.",
"ProgBeenden"   : u"Ukončit TextSTAT",
"AbfrageEnde"   : u"Aktuální korpus byl změněn.\nChcete jej uložit před ukončením programu TextSTAT?",
"AbfrageSave"   : u"Aktuální korpus byl změněn.\nChcete jej uložit před načtením nového korpusu?",
}

##############################
###########  Catalan   #######
##############################
# Catalan translation by "M. Amor Montané" <amor.montane@upf.edu>
# Thanks to Amor Montané & LATEL <iulalatel@upf.edu> for the translation. See http://latel.upf.edu

catalan  = {
"Titel"         : u"TextSTAT",
"Titel_lang"    : u"TextSTAT (Eina d'anàlisi textual)",
"Version"       : Version,
"VersionDatum"  : u"Data de la versió %s" % VersionDatum,
"Copyright"     : Copyright,
"eMail"         : eMail,
"ProgURL"       : ProgURL,
"ProgInfo"      : u"TextSTAT és programari lliure.\nL'ús d'aquest programa no té garanties.\nL'autor no assumeix cap tipus de responsabilitat.\n\nTraduït al català per LATEL <iulalatel@upf.edu>",

###### Menu #####
"Korpus"        : u"Corpus",
"KorpusNew"     : u"Nou corpus",
"KorpusOpen"    : u"Obre un corpus",
"KorpusHinzu"   : u"Afegeix un corpus",
"KorpusSave"    : u"Desa el corpus",
"KorpusSaveAs"  : u"Anomena i desa",
"KorpusDel"     : u"Elimina el corpus",
# has to be translated:
"LetzteKorpora" : u"Corpus(s) recent(s)",

"DateiHinzu"    : u"Afegeix un fitxer local",
"WebHinzu"      : u"Afegeix un fitxer del web",
"NewsHinzu"     : u"Afegeix una publicació d'un grup de discussió",
"DateiWeg"      : u"Elimina fitxer(s)",

"OptSave"       : u"Desa les opcions",
"Exit"          : u"Tanca",

"ImpEx"         : u"Exportació",
"Ex2csv"        : u"Llista de freqüències > Arxiu CSV",
"Ex2txt"        : u"Llista de concordances > Arxiu TXT",
"Ex2excel"      : u"Llista de freqüències > MS Excel",
"Ex2word"       : u"Llista de concordances > MS Word",
"ImpKorpus"     : u"Importa un corpus (TextSTAT 1.x)",

"Sprache"       : u"Llengua",
"CodePage"      : u"Codificació",
"Hilfe"         : u" ? ",
"RegExpHelp"    : u"Expressions regulars - Ajuda",
"History"       : u"Històric (en alemany)",
"License"       : u"Llicència",
"Willkommen"    : u"Informació sobre TextSTAT",


##### Toolbar #####
"KorpusNew2"    : u"Crea un nou corpus",
"KorpusOpen2"   : u"Obre un corpus existent",
"KorpusHinzu2"  : u"Afegeix un corpus existent al corpus actual",
"KorpusSave2"   : u"Desa el corpus",
"KorpusDel2"    : u"Elimina el corpus",
"WebHinzu2"     : u"Afegeix un fitxer del web",
"DateiHinzu2"   : u"Afegeix un fitxer local",
"DateiWeg2"     : u"Elimina fitxer(s)",
"FreqZeigen"    : u"Mostra la llista de freqüències de paraules",
"FreqZeigen2"   : u"Mostra la llista de freqüències de paraules",
"Kopieren"      : u"Copia al porta-retalls",
"Kopieren2"     : u"Copia la selecció al porta-retalls",
"Ex2excel2"     : u"Exporta la llista de freqüències a MS Excel",
"Ex2word2"      : u"Exporta les concordances a MS Word",
"Info"          : u"Informació",
"Info2"         : u"Informació sobre TextSTAT",

##### Tabs #####
"KorpusTab"     : u"Corpus",
"FormenTab"     : u"Formes",
"ConcTab"       : u"Concordances",
"ZitatTab"      : u"Context",
"ClustNGramsTab": u"Cluster/N-Grams",
"CollocatesTab" : u"Collocates",
"LConcTab" : u"KWIDC",
"TextGraphTab": u"Graph model",

"KTinfo"        : u"TextSTAT \n\nSisplau, crea un corpus i afegeix-hi alguns fitxers (o obre un corpus existent).",
"KTkopieren"    : u"Copia o reanomena el fitxer",
"KTopen"        : u"Obre el fitxer",
"KTdatinfo"     : u"Informació del fitxer",
"KTdatweg"      : u"Elimina el(s) fitxer(s)",

"FTinfo"        : u"FREQÜÈNCIA \nde formes (tokens)",
"FTsortFreq"    : u"Organitza per freqüència",
"FTsortAlpha"   : u"Organitza alfabèticament",
"FTsortRetro"   : u"Ordre invers",
"FTminFreq"     : u"Freqüència mínima",
"FTmaxFreq"     : u"Freqüència màxima",
"FTignGross"    : u"Organitza sense distingir entre\nmajúscules i minúscules",
"FTsuchFreq"    : u"Busca la freqüència de les\nparaules que contenen els caràcters següents:",
"FTfreqliste"   : u"Mostra la llista de freqüències",
"FTwortform"    : u"Formes",
"FTfrequenz"    : u"Freqüència",
"FTkopieren"    : u"Copia",
"FTsuchKonk"    : u"Busca concordances",
"FTzeigInfo"    : u"Més informació",
"FTformInfo"    : u"Informació del corpus\n\nEl corpus conté %s paraules (tokens)\n\n%s formes diferents (les formes i les lletres majúscules es diferencien) \n%s formes (les lletres minúscules s'ignoren)\n\nLa forma '%s' apareix %s vegades (= %.2f %%)",
"FTOptionen"    : u"Freqüència / Opcions",

"CTsuchen"      : u"Consulta",
"CTganzWort"    : u"Fes-ho coincindir amb una paraula sencera",
"CTignGross"    : u"No diferenciïs entre majúscules i minúscules",
"CTcontextL"    : u"Context a l'esquerra",
"CTcontextR"    : u"Context a la dreta",
"CTmarkSuch"    : u"Destaca la paraula consultada",
"CTsortAlpha"   : u"Organitza alfabèticament",
"CTsortR"       : u"Organitza a partir del context de la dreta",
"CTsortL"       : u"Organitza a partir del context de l'esquerra",
"CTaktualisier" : u"Actualitza",
"CTmachQuery"   : u"Editor de consultes",
"CTkopieren"    : u"Copia",
"CTzeigZitat"   : u"Mostra un context més gran",
"CTOptionen"    : u"Opcions",

"ZTinfo"        : u"Context",
"ZTkopieren"    : u"Copia",
"ZToeffnen"     : u"Obre el fitxer",
"ZToeffnen2"    : u"\n(Fes un doble clic per obrir el fitxer)\n",
# Has to be translated:
"ZTInit"        : u"\n Fes un doble clic en una de les concordances per obtenir més informació (és a dir, un context complet).",
"ClTFreqR"      :u"FreqR",
"ClTFreqL"      :u"FreqL",
"ClTKoef"       :u"Koef",
"ClTToken"      :u"Token",

"LCTSeparate"   :u"Separator",
"LCTSepBy"      :u"Separate by words",
"Source"        :u"Source",


##### Webdialog #####
"WDinfo"        : u"Afegeix fitxer(s) HTML directament des d'Internet.\nSisplau, introdueix l'adreça URL:",
"WDfrageSeiten" : u"Quantes pàgines vols afegir al corpus?",
"WDanzahl"      : u"Nombre de pàgines per recuperar",
"WDinSubdir"    : u"Domini: només el subdirectori",
"WDaufServer"   : u"Domini: servidor intern",
"WDok"          : u"D'acord",
"WDcancel"      : u"Cancel·la",

##### NewsDialog #####
"NDinfo"        : u"Afegeix publicacions d'un grup de discussió al corpus",
"NDserver"      : u"Servidor de missatges (del grup de discussió)", 
"NDgruppe"      : u"Grup de discussió",
"NDanzahl"      : u"Nombre de publicacions (missatges del grup)",
"NDzitWeg"      : u"Eliminar les citacions de les publicacions",
"NDok"          : u"D'acord",
"NDcancel"      : u"Cancel·la",

##### QueryDialog #####
"QDinfo"        : u"Ajuda per formular consultes complexes\nEs poden utilitzar caràcters comodí (wildcards), com ara * i ?",
"QDsuchFelder"  : u"Consulta",
"QAusdruck1"    : u"Primera paraula",
"QAusdruck2"    : u"Segona paraula",
"QAbstand"      : u"Nombre de paraules entre les paraules consultades",
"QAbstandMin"   : u"Mínim",
"QAbstandMax"   : u"Màxim",
"QmachAusdruck" : u"D'acord",
"QDcancel"      : u"Cancel·la",

##### Fehler #####
"Error"         : u"Error",
"ErrKorpNew"    : u"No es pot crear el fitxer del corpus",
"ErrKorpOpen"   : u"No es pot obrir el fitxer del corpus\nÉs realment un fitxer d'un corpus de TextSTAT?",
"ErrKorpImp"    : u"No es pot importar el fitxer del corpus",
"ErrNoKorp"     : u"Cal crear en primer lloc un corpus (o obrir-ne un d'existent).",
"ErrKorpSave"   : u"No es pot desar el fitxer del corpus",
"ErrFileOpen"   : u"S'ha produït un error en obrir el fitxer",
"ErrSelect"     : u"No s'ha seleccionat res",
"ErrOptSave"    : u"No s'han pogut desar les opcions",
"ErrExport"     : u"S'ha produït un error en l'exportació",
"ErrNoFreqList" : u"No hi ha cap llista de freqüències disponible",
"ErrNoKonkList" : u"No hi ha cap llista de concordances disponible",
"ErrExcel"      : u"Error de MS Excel\n(Comproveu que les extensions win32 de Python o MS Excel estiguin instal·lades correctament)",
"ErrExcel65K"   : u"S'ha produït un error. MS Excel no pot contenir més de 65500 línies. \nHi ha %s formes.",
"ErrWord"       : u"Error de MS Word.\n(Comproveu que les extensions win32 de Python o MS Word estiguin instal·lades correctament)",
"ErrExpFreq"    : u"S'ha produït un error en desar la llista de freqüències de paraules exportada.",
"ErrExpKonk"    : u"S'ha produït un error en desar la llista de concordances exportada.",
"ErrWeb"        : u"S'ha produït un error en buscar fitxers HTML des d'Internet.",
"ErrNews"       : u"S'ha produït un error en buscar publicacions de grups de discussió.",
"ErrQuery"      : u"No s'ha introduït cap paraula per a la cerca.",


##### Mitteilungen und Fragen #####
"AskSure"       : u"N'estàs segur/a?",
"AskDelete"     : u"Vols eliminar efectivament %s ?",
"StatusWeb"     : u"S'estan recuperant des d'Internet %s fitxers...",
"StatusNews"    : u"S'estan recuperant %s publicacions de grups de discussió...",
"DateiInfo"     : u"Informació del fitxer",
"DateiInfo2"    : u"Fitxer: %s\n\nDirectori: %s\n\nMida: %s\n",
"InfoText"      : u"TextSTAT\
\n\n\nEn crear o obrir un corpus, s'hi poden afegir fitxers. \
També es poden eliminar fitxers del corpus. En fer clic amb el botó dret del ratolí es desplega un menú d'opcions. \
El corpus es pot desar com un tot. \
\n\nS'ofereixen diverses funcionalitat per a l'anàlisi textual:\nA 'Formes' s'obtenen les freqüències de les paraules dels textos.\nA 'Concordances' s'obtenen els contextos d'aparició de les formes (KWIC).\nI a 'Context' es mostren contextos sencers.",

"StatusKorpImp" : u"El corpus s'ha importat correctament.",
"StatusKorpSave": u"El corpus s'ha desat correctament.",
"StatusFiles"   : u" %s fitxers | %s bytes ",
"StatusKorpDat" : u"Corpus: %s  (codificació actual: %s)",
"KodierungInfo" : u"Ara pots afegir alguns fitxers al corpus.\n\n Fitxers provinents de processadors de textos:\n- Fitxers de MS Word ('.doc', '.docx'; només en  Windows)\n- Fitxers d'OpenOffice ('.sxw', '.odt')\n\nFitxers de text:\n- Fitxers de text ASCII/ANSI (extensió '.txt')\n- Fitxers HTML (allotjats en el teu HD o directament d'Internet)\n- Publicacions de grups de discussió (directament d'Internet)\nEn afegir fitxers de text, cal verificar que s'utilitza una codificació correcta.\nLa codificació actual és: %s",
"StatusFormen"  : u" %s formes (%s paraules (tokens) al corpus)",
"StatusNoKorp"  : u"No existeix cap corpus",
"StatusSuchKonk": u"Busca concordances...",
"StatusTreffer" : u" %s trobades",
"StatusExpFreq" : u"S'ha exportat la llista de freqüències.",
"StatusExpKonk" : u"S'ha exportat la llista de concordances",
"ExportHinweis" : u"Cal utilitzar una font no proporcional (como ara Courier New)",
"StatusClip"    : u"S'ha copiat la selecció al porta-retalls",
"SpracheAendern": u"Canviar de llengua",
"SpracheInfo"   : u"Cal reiniciar TextSTAT per activar el canvi de llengua.",
"ProgBeenden"   : u"Surt de TextSTAT",
"AbfrageEnde"   : u"El corpus ha canviat. \nVols desar el corpus \nabans de sortir de TextSTAT?",
"AbfrageSave"   : u"El corpus ha canviat. \nVols desar el corpus \nabans d'obrir-ne un altre?",
}

#russian = english.copy()
#russian.update({
russian = {
"Titel"         : u"TextSTAT",
"Titel_lang"    : u"TextSTAT (Простой инструмент для анализа текста)",
"Version"       : Version,
"VersionDatum"  : u"Дата версии %s" % VersionDatum,
"Copyright"     : Copyright,
"eMail"         : eMail,
"ProgURL"       : ProgURL,
"ProgInfo"      : u"TextSTAT свободное ПО.\nИспользуйте на свой риск.\nАвтор не несет ответственности.",

###### Меню #####
"Korpus"        : u"Корпус",
"KorpusNew"     : u"Новый корпус",
"KorpusOpen"    : u"Открыть корпус",
"KorpusHinzu"   : u"Добавить корпус",
"KorpusSave"    : u"Сохранить корпус",
"KorpusSaveAs"  : u"Сохранить как",
"KorpusDel"     : u"Удалить корпус",
"LetzteKorpora" : u"Остальные корпусы",

"DateiHinzu"    : u"Добавить локальный файл",
"WebHinzu"      : u"Добавить файл из веб",
"NewsHinzu"     : u"Добавить новостные сообщения",
"DateiWeg"      : u"Удалить файл(ы)",

"OptSave"       : u"Сохранить настройки",
"Exit"          : u"Выход",

"ImpEx"         : u"Экспорт",
"Ex2csv"        : u"Частотный список > файл CSV",
"Ex2txt"        : u"Конкорданс > файл TXT",
"Ex2excel"      : u"Частотный список > MS Excel",
"Ex2word"       : u"Конкорданс > MS Word",
"ImpKorpus"     : u"Импортировать корпус (TextSTAT 1.x)",

"Sprache"       : u"Language",
"CodePage"      : u"Кодировка",
"Hilfe"         : u" Помощь ",
"RegExpHelp"    : u"Регулярные выраженения - Помощь",
"History"       : u"История (Немецкий)",
"License"       : u"Лицензия",
"Willkommen"    : u" Добро пожаловать в TextSTAT",

##### Toolbar #####
"KorpusNew2"    : u"Создать новый корпус",
"KorpusOpen2"   : u"Открыть существующий корпус",
"KorpusHinzu2"  : u"Добавить существующий корпус к текущему корпусу",
"KorpusSave2"   : u"Сохранить корпус",
"KorpusDel2"    : u"Удалить файл корпуса",
"WebHinzu2"     : u"Добавить HTML файл(ы) из Интернет в корпус",
"DateiHinzu2"   : u"Добавить локальны(е) файл(ы) к корпусу",
"DateiWeg2"     : u"Удалить файл(ы) из корпуса",
"FreqZeigen"    : u"Показать частоту слов",
"FreqZeigen2"   : u"Показать частоту словарных форм в корпусе",
"Kopieren"      : u"Скопировать в буфер обмена",
"Kopieren2"     : u"Копировать выделение в буфер обмена",
"Ex2excel2"     : u"Экспортировать список частот в MS Excel",
"Ex2word2"      : u"Экспортировать конкорданс в MS Word",
"Info"          : u"Информация",
"Info2"         : u"Информация о TextSTAT",

##### Tabs #####
"KorpusTab"     : u"Корпус", 
"FormenTab"     : u"Словарные формы",
"ConcTab"       : u"Конкорданс",
"ZitatTab"      : u"Цитаты",
"ClustNGramsTab": u"Cluster/N-Grams",
"CollocatesTab" : u"Коллокация",
"LConcTab"      : u"N-граммы",
"TextGraphTab": u"Графовая модель",


"KTinfo"        : u"TextSTAT \n\nПожалуйста, создайте корпус и добавьте файл(ы) (или откройте существующий корпус).",
"KTkopieren"    : u"Скопировать имя файла",
"KTopen"        : u"Открыть файл",
"KTdatinfo"     : u"Информация файла",
"KTdatweg"      : u"Удалить файл(ы)",

"FTinfo"        : u"ЧАСТОТА \nсловарных форм (токенов)",
"FTsortFreq"    : u"сортировать по частоте",
"FTsortAlpha"   : u"сортировать в алфавитном порядке",
"FTsortRetro"   : u"по последнему символу слова",
"FTminFreq"     : u"мин. частота",
"FTmaxFreq"     : u"макс. частота",
"FTignGross"    : u"сортировать без чувсвительности к регистру",
"FTsuchFreq"    : u"Задать фильтр (строка или\nрегулярное выражение):",
"FTfreqliste"   : u"Частотный список",
"FTwortform"    : u"Словарная форма",
"FTfrequenz"    : u"Частота",
"FTkopieren"    : u"Копировать",
"FTsuchKonk"    : u"Найти конкорданс",
"FTzeigInfo"    : u"Больше информации",
"FTformInfo"    : u"Информация по корпусу\n\nКорпус содержит %s слов (токенов)\n\n%s различных форм (types, заглавных буквы влияют) \n%s types (Заглавные буквы не влияют)\n\nФорма '%s' встречается %s раз (= %.2f %%)",
"FTOptionen"    : u"Частоты / настройки",

"CTsuchen"      : u"Поиск",
"CTganzWort"    : u"искать только целые слова",
"CTignGross"    : u"искать без учета регистра",
"CTcontextL"    : u"левый контекст",
"CTcontextR"    : u"правый контекст",
"CTmarkSuch"    : u"пометить найденую строку",
"CTsortAlpha"   : u"алфавитный порядок",
"CTsortR"       : u"соритровать по правому контексту",
"CTsortL"       : u"соритровать по левому контексту",
"CTaktualisier" : u"Обновить",
"CTmachQuery"   : u"Редактор запроса",
"CTkopieren"    : u"Копировать",
"CTzeigZitat"   : u"Показать больше контекста",
"CTOptionen"    : u"Настройки",

"ZTinfo"        : u"Текст цитаты",
"ZTkopieren"    : u"Копировать",
"ZToeffnen"     : u"Открыть файл",
"ZToeffnen2"    : u"\n(Дважды щелкните чтобы открыть файл)\n",
"ZTInit"        : u"\n Дважды щелкните на одном из результатов конкорданса, чтобы показать этот результат с более широким контекстом.",

"ClTFreqR"      :u"ЧастотаПр",
"ClTFreqL"      :u"ЧастотаЛв",
"ClTKoef"       :u"Коэф",
"ClTToken"      :u"Токен",

"LCTSeparate"   :u"Разделитель",
"LCTSepBy"      :u"Разделять по словам (\w+)",
"Source"        :u"Источник",

"Also"          :u"Другое",
"TGCompTextGraph"   :u"Вычислить графовую модель",
"TGLoadStatus"   :  u"Графовая модель загружается из файла...",
"TGSuccessLoadStatus":u"Грвфовая модель успешно загружена из файлв",
"tf-idf"        : u"TF-IDF",
"TGExport"      : u"Экспорт",
"TGGraphs"      : u"Графики частот",
"TGmaxWord"     : u"max слово",
"TGmaxValue"        :u"max значение",
"TGminWord"     :u"min слово",
"TGminValue"    :u"min значение",
"TGavgWord"     :u"сред. слово",
"TGavgValue"    :u"сред. значение",
"TGVertecesCount"  :u"Количество вершин:",
"TGEdgesCount"  :u"Количество дуг:",
"TGExportError" :u"Ошибка экспорта графовой модели...",
"TGExportNodeSuccess"   :u"выгрузка вершин графовой модели в .csv успешна",
"TGExportEdgeSuccess"   :u"выгрузка дуг графовой модели в .csv успешна",
"TGStopWords"       :u"Стоп-слова",
"TGdefaultStopWords"    :u",".join((u'в', u'но', u'и', u'на', u'из', u'то', u'к', u'а', u'что', u'-')),
"TGdefaultWordPattern"    :ur"[a-zA-ZА-ЯёЁ\-]+",
"TGSWordPattern"        :u"Шаблон слов",
"TGComputeStatus"       :u"Вычисление графовой модели..",
"TGStemming"            :u"Нормализовать",

##### Webdialog #####
"WDinfo"        : u"Добавьте HTML файлы напрямую из Интернета.\nВведите URL:",
"WDfrageSeiten" : u"Сколько страниц Вы хотите добавить к корпусу?",
"WDanzahl"      : u"Кол-во страниц для извлечения",
"WDinSubdir"    : u"домен: только поддиректории",
"WDaufServer"   : u"домен: весь сервер",
"WDok"          : u"Поиск",
"WDcancel"      : u"Закрыть",

##### NewsDialog #####
"NDinfo"        : u"Add newsgroup postings to corpus", 
"NDserver"      : u"news server",  
"NDgruppe"      : u"newsgroup", 
"NDanzahl"      : u"number of postings", 
"NDzitWeg"      : u"remove quotes from postings", 
"NDok"          : u"Search",
"NDcancel"      : u"Close",

##### QueryDialog #####
"QDinfo"        : u"Вспомогательная функция для формулирования сложных запросов.\n Работают шаблоны поиска (* и ?)",
"QDsuchFelder"  : u"Искать терм",
"QAusdruck1"    : u"Первый поисковый терм",
"QAusdruck2"    : u"Второй поисковый терм",
"QAbstand"      : u"Кол-во слов между двумя поиск. термами",
"QAbstandMin"   : u"min. и   ",
"QAbstandMax"   : u"max.",
"QmachAusdruck" : u"Начать поиск",
"QDcancel"      : u"Закрыть",

##### Fehler #####
"Error"         : u"Ошибка",
"ErrKorpNew"    : u"Файл корпуса не может быть создан!",
"ErrKorpOpen"   : u"Файл корпуса не может быть открыт!\nВы уверены, что это файл корпуса TextSTAT?",
"ErrKorpImp"    : u"Файл корпуса не может быть импортирован!",
"ErrNoKorp"     : u"Сначала нужно создать файл корпуса(или открыть существующий).",
"ErrKorpSave"   : u"Файл корпуса не может быть сохранен!",
"ErrFileOpen"   : u"Ошибка открытия файла!",
"ErrSelect"     : u"Ничего не выбрано!",
"ErrOptSave"    : u"Настройки могут не сохранится!",
"ErrExport"     : u"Ошбика экспорта",
"ErrNoFreqList" : u"No word frequency list available",
"ErrNoKonkList" : u"No word concordance list available",
"ErrExcel"      : u"Ошибка MS Excel!\n(Are the Python win32 extentions an MS Excel installed correctly?)",
"ErrExcel65K"   : u"Error! MS Excel cannot handle more than 65500 rows. \nWe have %s forms.",
"ErrWord"       : u"MS Word error!\n(Are the Python win32 extentions an MS Word installed correctly?)",
"ErrExpFreq"    : u"Error on saving the exported word frequency list.",
"ErrExpKonk"    : u"Error on saving the exported concordance list.",
"ErrWeb"        : u"Error while fetching HTML-files from the internet.",
"ErrNews"       : u"Error while fetching newsgroup postings.",
"ErrQuery"      : u"No search term defined.",


##### Mitteilungen und Fragen #####
"AskSure"       : u"Вы уверены?",
"AskDelete"     : u"Вы действительно хотите удалить %s ?",
"StatusWeb"     : u"%s файлы(ов) были получены из Интернета...",
"StatusNews"    : u"%s newsgroup postings are being retrieved...",
"DateiInfo"     : u"Информация о файле",
"DateiInfo2"    : u"Файл: %s\n\nПуть: %s\n\nРазмер: %s\n",
"InfoText"      : u"TextSTAT\
\nПосле создания (или открытия) корпуса, к нему можно добавить еще файлы. \
Файлы можно удалять из корпуса. Правая кнопка мыши откроет контекстное меню. \
Можно сохранить корпус целиком. \
\nРеализовано несколько инструментов для анализа текста: под 'Слоаврными формами' вы найдете \
частоты для токенов из ваших текстов. 'Конкорданс' покажет вам KWIC конкордансы \
(KeyWord in Context), 'Цитирование' отображает больше контекста.",

"StatusKorpImp" : u"Корпус успешно импортирован.",
"StatusKorpSave": u"Корпус сохранен.",
"StatusFiles"   : u" %s файлов | %s байт ",
"StatusKorpDat" : u" Корпус: %s  (установлена кодировка: %s)",
"KodierungInfo" : u"Сейчас Вы можете добавить файлы к корпусу.\n\nТекстовые документы:\n- файлы MS Word ('.doc' или '.docx'; только Windows)\n- файлы OpenOffice ('.odt или .sxw')\n\nТекстовые файлы:\n- ASCII/ANSI текстовые файлы (расширение '.txt')\n- HTML страницы (из вашего диска или напрямую из Интернета)\n- Новостные сообщения (по протоколу NNTP)\nДобавляя текстовые файлы проверяйте используему кодировку.\nСейчас установлена: %s",
"StatusFormen"  : u" %s словарных форм/типов (в корпусе %s слов/токенов)",
"StatusNoKorp"  : u"нет корпуса ",
"StatusSuchKonk": u"Ищем конкордансы...",
"StatusTreffer" : u" %s результатов ",
"StatusExpFreq" : u"Список частот экспортирован.",
"StatusExpKonk" : u"Список конкардансов экспортирован",
"ExportHinweis" : u"Используйте моноширный шрифт(например Courier New)",
"StatusClip"    : u"Выделеное скопировано в буфер обмена",
"SpracheAendern": u"Смена языка",
"SpracheInfo"   : u"Перезапустите TextSTAT, чтобы применить смену языка.",
"ProgBeenden"   : u"Закрыть TextSTAT",
"AbfrageEnde"   : u"Корпус изменен. \nХотите сохранить ващ корпус \nперед закрытием TextSTAT?",
"AbfrageSave"   : u"Корпус изменен. \nХотите сохранить ващ корпус \nперед открытием другого корпуса?",
}
#)



