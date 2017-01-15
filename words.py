#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from requests import get

CARDS_FOLDER = 'cards'
SOUNDS_FOLDER = 'sounds'
TRANSLATE_TO = 'uk'
URL_WORD = 'http://www.wordreference.com/es/translation.asp?tranword='
URL_SOUND = ('http://www.wordreference.com'
             '/audio/en/{}/general/'.format(TRANSLATE_TO))
WORDS_FILE = 'words.txt'


def get_words():
    """Lee del fichero ./vocabulario/words.txt de las palabras a traducir"""
    words = []
    f = open(WORDS_FILE, 'r')
    for l in f:
        words.append(l.replace('\n', ''))
    return words


def get_pronountiation():
    """Devuelve el mp3 solicitado: /audio/en/uk/general/"""
    # Se puede hacer con una regex: /audio/en/uk/general/numero.mp3
    return None


def get_sound_name(html):
    return False


def get_html(word):
    html = get(URL_WORD + '{}'.format(word))
    return html


def get_translation(html):
    """Devuelve la traduccion solicitada"""
    soup = BeautifulSoup(html.text, 'html.parser')
    trans = soup.find_all("td", "ToWrd")
    return [t.next for t in trans[1:6]]


def create_card(translation, sound):
    """Devuelve el html de la tarjeta a crear en Anki"""
    return None


def create_massive_import(cards):
    """Recibe una lista de cards y crea el fichero cards_words.txt
    preparado para cargar en Anki
    """
    pass


def main():
    html = get_html('word')
    print get_translation(html)
    print get_sound_name(html)
    # get_pronountiation(url)


if __name__ == '__main__':
    main()
