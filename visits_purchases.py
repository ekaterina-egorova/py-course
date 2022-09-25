#!/usr/bin/env python
# coding: utf-8

import json

purchases_file_name = 'purchase_log.txt'
visits_file_name = 'visit_log.csv'
funnel_file_name = 'funnel.csv'

purchases = {}

with open(purchases_file_name) as purchases_file:
    for i, line in enumerate(purchases_file): 
        parsed = json.loads(line)
        purchases[parsed['user_id']] = parsed['category']
        
print (f'Loaded {len(purchases)} rows from {purchases_file_name}')

funnel_rows = 0

with open(visits_file_name) as visit_file, open(funnel_file_name, 'w') as funnel_file:
    for i, line in enumerate(visit_file): # using first title line matches purchases_log.txt title line
        user_id, source = line.strip().split(',')
        category = purchases.get(user_id)
        if category:
            funnel_file.write(f'{user_id},{source},{category}\n') # also writing title line
            funnel_rows += 1
    print (f'Walking through {i} rows from {visits_file_name}')
    
print (f'Matched {funnel_rows} visits to purchases. Matched rows has been written to {funnel_file_name}')

