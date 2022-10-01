#!/usr/bin/env python
# coding: utf-8

from datetime import datetime
from datetime import timedelta

def date_range(start_date, end_date):
    if None == start_date:
        return []
    if None == end_date:
        return []
    
    try:
        start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
        dates = []
        while start_date_dt <= end_date_dt:
            dates.append(start_date_dt.strftime('%Y-%m-%d'))
            start_date_dt += timedelta(days=1)
        return dates
        
    except ValueError as e:
        print (e)
        return []

    
assert ['2022-01-01', '2022-01-02', '2022-01-03'] == date_range('2022-01-01', '2022-01-03')
assert [] == date_range('2022-01-03', '2022-01-02')
assert [] == date_range('22-01-01', '2022-01-03')
assert [] == date_range('2022-01-01', '22-01-03')


print (date_range('2022-01-01', '2022-01-03'))

