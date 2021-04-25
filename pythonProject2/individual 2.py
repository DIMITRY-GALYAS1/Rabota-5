#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = str(input('Введите предложение:'))
    q = s.rfind(' ')
    if len(s) == 12 and q == -1:
        z = s[2:9]
        print('Слово:', s[0:2] + z[::-1] + s[9:12])
        exit(0)
    else:
        print('Ошибка')
        exit(1)
