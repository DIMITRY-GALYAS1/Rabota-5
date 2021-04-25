#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input('Введите предложение:')
    z = s.rfind(' ')
    if z == -1:
        print('Вы ввели одно слово')
        exit(1)
    else:
        print('Последние слово:', s[z:])
        exit(0)
