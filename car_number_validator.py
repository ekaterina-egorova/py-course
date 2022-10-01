#!/usr/bin/env python
# coding: utf-8

import re
auto_number_regex = r'^(([АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2})(\d{2,3}))$'

def validate_auto_number(request):
    result = re.findall(auto_number_regex, request)
    if result == []:
        return None, None
    return result[0][1], result[0][2]


assert ('А222ВС', '96') == validate_auto_number('А222ВС96')
assert (None, None) == validate_auto_number('АБ22ВВ193')

def print_validation_result(request):
    number, region = validate_auto_number(request) 
    if None == number or None == region:
        print('Результат: Номер не валиден')
    else:
        print(f'Результат: Номер {number} валиден. Регион: {region}')

car_id = 'А222ВС96'
print_validation_result(car_id)
car_id = 'АБ22ВВ193'
print_validation_result(car_id)

