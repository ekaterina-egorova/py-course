#!/usr/bin/env python
# coding: utf-8

def is_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

assert is_leap(2024) == True
assert is_leap(2022) == False
assert is_leap(2100) == False
assert is_leap(2400) == True
assert is_leap(2020) == True
assert is_leap(2019) == False
 
year = int(input('Введите год:'))
print('Високосный год') if is_leap(year) else print('Обычный год')
