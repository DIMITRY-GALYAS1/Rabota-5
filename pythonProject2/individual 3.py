#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    d = str(input('Введите число:'))
    if d.isdigit():
        print(len(str(d)))
        exit(0)
    else:
        print('Ошибка')
        exit(1)
