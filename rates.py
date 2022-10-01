#!/usr/bin/env python
# coding: utf-8

import requests

class Rates:
    def __init__(self, format_='value'):
        self.format = format_
        
    def exchange_rates(self):
        self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return self.r.json()['Valute']
    
    def make_format(self, currency):
        response = self.exchange_rates()
        
        if currency in response:
            if self.format == 'full':
                return response[currency]
            if self.format == 'value':
                return response[currency]['Value']
        
        return 'Error'
        
    def usd(self):
        return self.make_format('USD')
    
    def max(self):
        response = self.exchange_rates()
        maxValue = -1.0
        leader = None
        for currency in response.values():
            value = float(currency['Value'])
            leader = currency['Name'] if value > maxValue else leader
            maxValue = value if value > maxValue else maxValue 
        return leader
        
    
class RatesDiff(Rates):
    def __init__(self):
        super().__init__(format_ = 'full')
        
    def usd(self):
        response = self.make_format('USD')
        return float(response['Value']) - float(response['Previous'])
    
r = Rates()
print(r.usd())
print(r.max())

d = RatesDiff()
print(f'{d.usd():.4}')
        

