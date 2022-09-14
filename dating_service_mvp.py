#!/usr/bin/env python
# coding: utf-8

def match_pairs(boys, girls):
    if len(boys) != len(girls):
        raise ValueError("Attention! Someone may be left without a pair!")
        
    sorted_boys = sorted(boys)
    sorted_girls = sorted(girls)
    return [[boy, sorted_girls[i]] for i, boy in enumerate(sorted_boys)]


assert match_pairs(['Peter', 'Alex', 'John', 'Arthur', 'Richard'],                    ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']) == [['Alex', 'Emma'], ['Arthur', 'Kate'], ['John', 'Kira'], ['Peter', 'Liza'], ['Richard', 'Trisha']]

boys = input("Please enter boys list:").strip().split()
girls = input("Please enter girls list:").strip().split()

if(len(boys) != len(girls)) :
    print('Attention! Someone may be left without a pair!')
else:
    print ("Result:")
    for pair in match_pairs(boys, girls):
        print (f'{pair[0]} and {pair[1]}')

