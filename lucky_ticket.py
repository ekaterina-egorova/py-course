#!/usr/bin/env python
# coding: utf-8

def is_lucky(ticket):
    ticket_arr = [int(char) for char in str(ticket)]
    
    if len(ticket_arr) % 2 > 0:
        raise ValueError('ticket is not valid for the calculating method')

    total = 0
    end = len(ticket_arr)//2
    
    for i in range(end):
        total = total + ticket_arr[i] - ticket_arr[len(ticket_arr)-i-1]

    if total == 0: # total is int therefore could be compared to 0
        return True
    
    return False

assert is_lucky(123456) == False
assert is_lucky(123321) == True
assert is_lucky(1234) == False
assert is_lucky(1221) == True
assert is_lucky(781448) == True

ticket = input("Введите 6-значный номер билета:")
if len(ticket) != 6:
    raise ValueError('ticket length is not valid')
print ('Счастливый билет') if is_lucky(ticket) else print('Несчастливый билет')

