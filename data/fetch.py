import requests
from xml.etree import ElementTree as ET 

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
    
    