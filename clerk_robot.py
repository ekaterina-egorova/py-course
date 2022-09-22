#!/usr/bin/env python
# coding: utf-8


# In[258]:


documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}

document_by_number = { document['number']: document for document in documents }
directory_by_doc_number = {}
for directory_id, documents in directories.items():
    for document_number in documents:
        directory_by_doc_number[document_number] = directory_id

def lookup_owner(number):
    if number:
        document = document_by_number.get(number)
        if document: 
            return document['name']
        
    return None

def lookup_directory(number):
    if number:
        return directory_by_doc_number.get(number)
    return None
        
    
assert None == lookup_owner(None)
assert None == lookup_owner(226234)
assert 'Василий Гупкин' == lookup_owner('2207 876234')
assert 'Геннадий Покемонов' == lookup_owner('11-2')
assert 'Аристарх Павлов' == lookup_owner('10006')

assert None == lookup_directory(None)
assert None == lookup_directory(226234)
assert '1' == lookup_directory('2207 876234')
assert '1' == lookup_directory('11-2')
assert '2' == lookup_directory('10006')

answer = ''
lookup_owner_cmd = 'p'
lookup_directory_cmd = 's'
break_cmd = 'r'

while break_cmd != answer:
    answer = input('Введите команду: ')
    if lookup_owner_cmd != answer and lookup_directory_cmd != answer:
        continue
    
    document_number = input('Введите номер документа: ')
    
    if lookup_owner_cmd == answer:
        owner = lookup_owner(document_number)
        if owner:
            print(f'Результат:\nВладелец документа: {owner}')
        else:
            print('Документ не найден')
    
    if lookup_directory_cmd == answer:
        directory = lookup_directory(document_number)
        if directory:
            print(f'Результат:\nДокумент хранится на полке: {directory}')
        else:
            print('Документ не найден')

