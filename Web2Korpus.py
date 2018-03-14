#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Hilfsklassen und -funktionen für Korpus.py

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import urllib2, urlparse, re

# Klasse zum Entfernen von HTML und Formatieren der Textdatei
class HTMLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
        self.linkliste = []
    def handle_data(self, d):
        self.fed.append(d)
    def handle_entityref(self, name):
        self.handle_data(unichr(name2codepoint[name]))
    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               if name == "href":
                   # URLs dürfen nicht Unicode sein, da sie nachher noch 
                   # als 'key' für Dictionaries dienen sollen
                   self.linkliste.append(value.encode('utf-8'))
        
    def gettext(self):
        t = ''.join(self.fed)
        # die ganzen Leerzeilen usw. entfernen
        t = ' '.join(t.split())
        return t


#################

class Web2Korpus:
    def __init__(self, master=None, url='', anzahl=1, basis='', codepage='utf-8'):
        self.master = master
        self.url = url
        self.anzahl = anzahl
        self.basis = basis
        self.codepage = codepage
        
        if self.url[:7] not in ['http://', 'https:/']:
            self.url = 'http://' + self.url

        self.host = urlparse.urljoin(self.url, '/')
        self.subdir = urlparse.urljoin(self.url, ' ').strip()
        if basis == 'subdir':
            self.basis = self.subdir
        else:
            self.basis = self.host
        
        # Format: Dictionary mit key = url und value = [seite, [links]]
        self.data = {}
        self.links = []
        
        if self.anzahl == 1:
            self.getWebPage()
        else:
            self.getSomeWebPages()

           
    def checkLink(self, url):
        url_ok = 1
        # URL schon vorhanden
        if url in self.links:
            url_ok = 0
        # File nicht auf dem angegebenen Server
        elif not url.startswith(self.basis):
            url_ok = 0
        # falsches URL-Schema
        elif url[0:4] != 'http':
            url_ok = 0
        # falsches Dateiformat
        elif url.endswith(('.js', '.pdf', '.doc', '.docx', '.gif', '.bmp', '.png', '.jpg', '.jpeg', '.ico', '.wav', '.mp3', '.ogg')):
            url_ok = 0
        # Fragment: Sprungmarke innerhalb des Dokuments (also .../...#...)
        elif urlparse.urlparse(url)[5] != '':
            url_ok = 0
        return url_ok

           
    def getWebPage(self):
        try:
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1)'
            headers = { 'User-Agent' : user_agent }
            req = urllib2.Request(self.url, None, headers)
            verbindung = urllib2.urlopen(req)

            seite = verbindung.read()
            
            # Kodierung aus Seite auslesen
            cod = re.search("text/html; charset=([ A-Za-z0-9-]+)", seite)
            if cod != None:
                cod = cod.group(1).strip()
            # ansonsten nehmen wir die Einstellung aus TextSTAT
            else:
                cod = self.codepage
            
            # Jetzt machen wir aus der Seite Unicode; ist etwas riskant, da man nicht 
            # weiß, ob das Characterset richtig angegeben ist...
            # Alternativ müsste man einfach die Angabe in self.codepage nehmen (= else)
            seite = unicode(seite, cod, 'replace')

            # Script- und Style-Angaben raus (die werden vom HTMLParser ignoriert bzw.
            # als normale Daten behandelt, daher vorher raus:
            seite = re.sub(r"(?is)<(script|style).*?>.*?(</\1>)", "", seite)
            
            st = HTMLStripper()
            st.feed(seite)
            st.close()

            # Unicode-Text machen
            self.data[self.url] = st.gettext()
            
            # Links überprüfen und in Liste
            for x in st.linkliste:
                if x.find('/') == -1:
                    x = urlparse.urljoin(self.url, x)
                if x.find('/') == 0:
                    x = urlparse.urljoin(self.host, x)
                
                url_ok = self.checkLink(x)   
                if url_ok == 1:
                    self.links.append(x)
        except:
            self.data[self.url] = 'Fehler'
        
   
    def getSomeWebPages(self):
        self.getWebPage()
        i = 1
        while len(self.links) > 0:
            if i >= self.anzahl:
                break
            else:
                self.url = self.links[0]
                self.links.pop(0)
                if self.data.has_key(self.url) == 0:
                    self.getWebPage()
                    i = i+1
                    
                    # Fortschritt in Statusbar anzeigen
                    self.master.status.progress.updateProgress(newValue=i, newMax=self.anzahl)
                    
        # Progressbar zurücksetzen                
        self.master.status.progress.updateProgress(0)

        
    def getData(self):
        return self.data


    
if __name__ == '__main__':
    url = 'www.stern.de'
    k = Web2Korpus(url, anzahl=3, basis='server')
    x = k.getData()
    for i in x.keys():
        print i
        print x[i]
