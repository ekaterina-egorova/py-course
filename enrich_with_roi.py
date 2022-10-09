#!/usr/bin/env python
# coding: utf-8

def enrich_with_roi(campaigns: dict): # I decided to modify source data and do not copy memory
    if None == campaigns:
        raise ValueError('campaigns=None')
    
    for indicators in campaigns.values():
        revenue: float = indicators['revenue']
        cost: float = indicators['cost']
        roi = (revenue / cost - 1) * 100           
        indicators['ROI'] = roi
     
    l = list(campaigns.items())
    l.sort(key=lambda c: c[1]['ROI'], reverse=True)

    return dict(l)


campaigns = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}

print (f'Sample campaigns data:\n{campaigns}')
print (f'Enriched with ROI result:\n{enrich_with_roi(campaigns)}')
