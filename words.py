#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from bs4.element import Tag
from requests import get
from re import search
from datetime import datetime
from os.path import join, exists
from os import makedirs
from time import sleep

NOW = datetime.now()
DATE = str(NOW.year) + str(NOW.strftime('%m')) + str(NOW.strftime('%d'))
OUTPUT_PATH = 'cards'
CARDS_PATH = join(OUTPUT_PATH, 'UK' + DATE)
SOUNDS_PATH = join(CARDS_PATH, 'sounds')
TRANSLATE_TO = 'uk'
URL_WORD = 'http://www.wordreference.com/es/translation.asp?tranword='
URL_SOUND = ('http://www.wordreference.com'
             '/audio/en/{}/general/'.format(TRANSLATE_TO))
WORDS_FILE = 'words.txt'
DECK_NAME = 'UK' + DATE


def get_words():
    """Lee del fichero ./vocabulario/words.txt de las palabras a traducir"""
    words = []
    f = open(WORDS_FILE, 'r')
    for l in f:
        words.append(l.replace('\n', ''))
    return words


def get_pronountiation(word, name):
    """Devuelve el mp3 solicitado"""
    url = URL_SOUND + '{}'.format(name)
    print url
    mp3 = get(url)
    print mp3.status_code
    f = open(join(SOUNDS_PATH, 'UK-' + DATE + '-' + word + '.mp3'), 'w')
    f.write(mp3.content)


def get_sound_name(html):
    """regex: en/numero4-6 digitos.mp3"""
    s = search(r"en(\d+)\.mp3", html)
    if s:
        groups = s.groups()
    return 'en' + groups[0] if s else ''


def get_html(word):
    url = URL_WORD + '{}'.format(word)
    print url
    html = get(url)
    print html.status_code
    return html.text


def get_translation(html):
    """Devuelve la traduccion solicitada"""
    soup = BeautifulSoup(html, 'html.parser')
    trans = soup.find_all("td", "ToWrd")
    return [t.next for t in trans[1:6] if not isinstance(t.next, Tag)]


def create_card(word, translation):
    """Devuelve el html de la tarjeta a crear en Anki"""
    anverse = word + '<br>'
    means = ', '.join(translation)
    sound = ' [sound:UK-' + DATE + '-' + word + '.mp3]'
    reverse = ("""<div style='font-family: Arial; """
               """font-size: 12px;'>""" + means + """</div>""")
    return anverse, reverse, sound


def create_massive_import(cards):
    """Recibe una lista de cards (tuplas: (anverse, reverse, sound))
    y crea el fichero cards_words.txt preparado para cargar en Anki
    """
    fa = open(join(CARDS_PATH, DECK_NAME + '-anverse.txt'), 'w+')
    fr = open(join(CARDS_PATH, DECK_NAME + '-reverse.txt'), 'w+')
    for card in cards:
        ca = card[0] + '#' + card[1] + ' ' + card[2]
        cr = card[1] + '#' + card[2] + ' ' + card[0]
        fa.write(ca.encode('utf-8'))
        fa.write('\n')
        fa.write('\n')
        fr.write(cr.encode('utf-8'))
        fr.write('\n')
        fr.write('\n')


def main():
    print OUTPUT_PATH
    print CARDS_PATH
    print SOUNDS_PATH
    print DECK_NAME
    if not exists(CARDS_PATH):
        makedirs(CARDS_PATH)
    if not exists(SOUNDS_PATH):
        makedirs(SOUNDS_PATH)
    cards = []
    words = get_words()
    for w in words:
        html = get_html(w)
        trans = get_translation(html)
        cards.append(create_card(w, trans))
        sound_name = get_sound_name(html)
        if sound_name:
            get_pronountiation(w, sound_name + '.mp3')
        sleep(2)
    create_massive_import(cards)


if __name__ == '__main__':
    main()
