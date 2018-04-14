import requests
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup, Tag
import peewee as pw
from playhouse.db_url import connect
from os import environ
import re

from backend.models import Debate, Speech

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
    while True:
        if type(prev_text) == Tag:
            if '<h1>' in prev_text.prettify():
                break
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
        while True:
            if type(next_text) == Tag:
                if '<h2>' in next_text.prettify():
                    break
                text += next_text.prettify()
            next_text = next_text.next_sibling
            if not next_text:
                break
        anf['data'] = parse_text(text)
        anforanden.append(anf)
    return debatt, anforanden

def parse_text(text):
    s = BeautifulSoup(text, 'html.parser')
    childs = s.findChildren()
    paragraphs = [str(childs[i].prettify()) for i in range(len(childs)) if i % 2 == 1]
    result = ''.join(paragraphs)
    result = result.replace('<span>', '<p>')
    result = result.replace('</span>', '</p>')
    result = re.sub('<span[^<]+>', '', result)
    # return list(map(lambda s: str(s)[6:-7], paragraphs)) # remove <span>...</span>
    return result


if __name__ == "__main__":
    main()
