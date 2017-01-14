#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup


OUTPUT_DIRECTORY = 'output'
TRANSLATE_TO = 'uk'
URL_WORD = 'http://www.wordreference.com/es/translation.asp?tranword='
URL_SOUND = ('http://www.wordreference.com'
             '/audio/en/{}/general/'.format(TRANSLATE_TO))


def get_words():
    """Lee del fichero ./vocabulario/words.txt de las palabras a traducir"""
    return None


def get_pronountiation():
    """Devuelve el mp3 solicitado"""
    return None


def get_translation():
    """Devuelve la traduccion solicitada"""
    return None


def create_card(translation, sound):
    """Devuelve el html de la tarjeta a crear en Anki"""
    return None


def create_massive_import(cards):
    """Recibe una lista de cards y crea el fichero cards_words.txt
    preparado para cargar en Anki
    """


def main():
    return None


if __name__ == '__main__':
    main()
