#!/usr/bin/env python
# coding: utf-8


ids = {'user1': [213, 213, 213, 15, 213], 
       'user2': [54, 54, 119, 119, 119], 
       'user3': [213, 98, 98, 35]}
 
geo_tags = set()

for v in ids.values():
    for i in v:
        geo_tags.add(i)
        
print(f'Результат: {geo_tags}')
    

