#!/usr/bin/env python
# coding: utf-8


year = 2400
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print('Високосный год')
else:
    print('Обычный год')

