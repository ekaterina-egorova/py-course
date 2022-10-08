#!/usr/bin/env python
# coding: utf-8

# In[9]:


from datetime import datetime

SUPPORTED_DATE_FORMAT = '%Y-%m-%d'

def check_date(date, required_format):
    try:
        datetime.strptime(date, required_format)
        return True
    except ValueError:
        return False

def dates_check(stream):
    return [check_date(date, SUPPORTED_DATE_FORMAT) for date in stream]

assert [True, False, False] == dates_check(['2018-04-02', '2018-02-29', '2018-19-02'])

