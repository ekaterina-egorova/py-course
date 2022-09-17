#!/usr/bin/env python
# coding: utf-8


queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]
m = {}
for q in queries:
    if q: 
        words_count = len(q.split())
        queries_count = m.setdefault(words_count, 0)
        m[words_count] = queries_count + 1
        
for k in sorted(m.keys()):
    print (f'Поисковых запросов, содержащих {k} слов(а): {m[k]/len(queries):.2%}')
    

