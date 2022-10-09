#!/usr/bin/env python
# coding: utf-8

import re

#I decided to use relaxed validation do not push user to guess validator rules
phone_number_pattern = r'^(\+?[78])?([\(\)\s-]{0,2}(\d)){10}$'
digit_pattern = r'(\d)'
phone_number_regex = re.compile(phone_number_pattern)
digit_regex = re.compile(digit_pattern)

def format_russian_phone_number(request):
    if phone_number_regex.match(request): 
        d = re.findall(r'(\d)', request[::-1])
        return f'+7-{d[9]}{d[8]}{d[7]}-{d[6]}{d[5]}{d[4]}-{d[3]}{d[2]}-{d[1]}{d[0]}'
    return 'Номер не валиден'
  
assert '+7-950-555-55-55' == format_russian_phone_number('+7 950 555-55-55')  
assert '+7-950-555-55-55' == format_russian_phone_number('8(950)555-55-55')  
assert '+7-950-555-55-55' == format_russian_phone_number('+7 950 555 55 55')  
assert '+7-950-555-55-55' == format_russian_phone_number('7(950) 555-55-55')  
assert 'Номер не валиден' == format_russian_phone_number('423-555-55-5555')
assert 'Номер не валиден' == format_russian_phone_number('123-456-789')
assert '+7-950-555-55-55' == format_russian_phone_number('+8 950 555-55-55')
assert '+7-950-555-55-55' == format_russian_phone_number('+7 (950 555-55-55')
assert '+7-950-555-55-55' == format_russian_phone_number('+7 (950) 5-55-55-55')
assert '+7-950-555-55-55' == format_russian_phone_number('+7 (950) 5 555 555')
assert 'Номер не валиден' == format_russian_phone_number('+7 (950) 5555 5555')
    
phone = input('Введите номер телефона: ')
print (f'Результат: {format_russian_phone_number(phone)}')

