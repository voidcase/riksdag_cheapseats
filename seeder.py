import requests
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup, Tag
import peewee as pw
from playhouse.db_url import connect
from os import environ

from backend.models import Document, Debate, Speech

def main():
    db = connect(environ.get('DATABASE_URL') or 'sqlite:///test.db')
    meta, data = debatt()
    db.create_tables([Debate, Speech])
    debate = Debate.create(id=meta['id'], title=meta['title'], summary=meta['summary'])
    debate.save()
    for anf in data:
        try:
            speech = Speech.create(
                person=anf['talare'],
                debate_id=meta['id'],
                nr=anf['nr'],
                party=anf['parti'],
                body=anf['data']
                )
            speech.save()
        except:
            pass

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
    debate_id = 'H50996'
    r = requests.get('http://data.riksdagen.se/dokument/' + debate_id + '.html')
    soup = BeautifulSoup(r.content, 'html.parser')
    sec2 = soup.find('div', ['Section2'])
    speeches = sec2.find_all('h2')
    anforanden = []

    first = speeches[0]
    prev_text = first.previous_sibling
    summary = ""
    while '<h1>' not in prev_text:
        if type(prev_text) == Tag:
            summary += prev_text.prettify()
        prev_text = prev_text.previous_sibling
        if not prev_text:
            break
    title = ''
    if prev_text:
        title = prev_text.findChildren()[7].string

    debatt = { 'id': debate_id, 'title': title, 'summary': summary }

    for speech in speeches:
        anf = {}
        anf['nr'] = speech.findChildren()[5].string
        anf['talare'] = speech.findChildren()[8].string.title()
        p = speech.findChildren()[10].string
        anf['parti'] = ''
        try:
            anf['parti'] = list(filter(lambda c: c.isalpha(), list(p)))[0]
        except:
            print(p)
        text = ""
        next_text = speech.next_sibling
        while '<h2>' not in next_text:
            if type(next_text) == Tag:
                text += next_text.prettify()
            next_text = next_text.next_sibling
            if not next_text:
                break
        anf['data'] = text
        anforanden.append(anf)
    return debatt, anforanden

if __name__ == "__main__":
    main()