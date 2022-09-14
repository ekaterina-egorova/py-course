#!/usr/bin/env python
# coding: utf-8


def middle_letters(text):
    str_text = str(text)
    length = len(str_text)
    start = (length - 1)//2
    end = (length + 2)//2
    return str_text[start:end]

assert middle_letters('test') == 'es'
assert middle_letters('testing') == 't'
assert middle_letters('') == ''

text = input("Please enter a word:")
result = middle_letters(text)
print (f'Middle letter{" is" if len(result) == 1 else "s are"}: {result}')


