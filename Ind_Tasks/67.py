#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sort_list(func):
    """
    Сортировка списка
    """
    def wrapper(not_s_l):
        print(not_s_l)
        sort_line = sorted(func(not_s_l))
        return sort_line
    return wrapper


@sort_list
def get_list(line):
    """
    Создание списка из строки цифр разделенных пробелами
    """
    new_line = [int(i) for i in line.split()]
    return new_line


if __name__ == '__main__':
    s = input("Enter line: ")
    print(get_list(s))
