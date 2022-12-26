#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def decorator(func):
    morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е':
             '.', 'ё': '.', 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-',
             'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с':
             '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.',
             'ч': '---.', 'ш': '----', 'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-',
             'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-...-'}

    # Функция возвращает ключ словаря по значению
    def get_key(val, dct):
        for key, value in dct.items():
            if val == key:
                return value

    def text_morze(*args):
        a = ''
        value = func(*args)
        for i in value:
            if i in morze.keys():
                a += get_key(i, morze)
        print(a)
        return a

    return text_morze


@decorator
def in_str(strk):
    strk = strk.lower()
    strk = ' '.join(strk.split())
    return strk


if __name__ == '__main__':
    print(in_str("ытаолфт"))
