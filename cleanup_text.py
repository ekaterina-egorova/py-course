#!/usr/bin/env python
# coding: utf-8

import re

some_string = 'Напишите функцию функцию, которая будет будет будет будет удалять все все все все последовательные повторы слов из из из из заданной строки строки при помощи регулярных выражений'

def cleanup_text(text):
    return re.sub(r'\b([^\W\d_]+)(\s+\1)+\b', r'\1', text)

print( cleanup_text(some_string) )





