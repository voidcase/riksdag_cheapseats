import requests
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup, NavigableString, Tag

def anforande(doc, id):
    r = requests.get('http://data.riksdagen.se/anforande/' + doc + '-' + id)
    root = ET.fromstring(r.text)
    anf = {
        'datum': root.find('dok_datum').text,
        'avsnitt': root.find('avsnittsrubrik').text,
        'talare': root.find('talare').text,
        'parti': root.find('parti').text,
        'text': root.find('anforandetext').text
    }
    return anf
    
def debatt():
    r = requests.get('http://data.riksdagen.se/dokument/H50996.html')
    soup = BeautifulSoup(r.content, 'html.parser')
    sec2 = soup.find('div', ['Section2'])
    speeches = sec2.find_all('h2')
    anforanden = []
    for speech in speeches:
        anf = {}
        anf['nr'] = speech.findChildren()[5].string
        anf['talare'] = speech.findChildren()[8].string.title()
        p = speech.findChildren()[10].string
        try:
            anf['parti'] = list(filter(lambda c: c.isalpha(), list(p)))[0]
        except:
            print(p)
        text = ""
        next_text = speech.next_sibling
        while '<h2>' not in next_text:
            # if type(next_text) == NavigableString or type(next_text) == Tag:
            if type(next_text) == Tag:
                text += next_text.prettify()
            next_text = next_text.next_sibling
            if not next_text:
                break
        anf['data'] = text
        anforanden.append(anf)
    return anforanden
