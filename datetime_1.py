#!/usr/bin/env python
# coding: utf-8

from datetime import datetime

print(datetime.strptime('Wednesday, October 2, 2002', '%A, %B %d, %Y'))
print(datetime.strptime('Friday, 11.10.13', '%A, %d.%m.%y'))
print(datetime.strptime('Thursday, 18 August 1977', '%A, %d %B %Y'))
