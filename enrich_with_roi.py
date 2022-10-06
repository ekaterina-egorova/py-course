#!/usr/bin/env python
# coding: utf-8

# In[80]:


def enrich_with_roi(campaigns: dict): # ~ requires ~ 5 campaigns memory size 
    if None == campaigns:
        raise ValueError('campaigns=None')
    
    enriched_campaigns = {} # since sorting is required then I'm going to copy all the data into a new structure 
    
    for source, indicators in campaigns.items():
        revenue: float = indicators['revenue']
        cost: float = indicators['cost']
            
        enriched_indicators = {'ROI': (revenue / cost - 1) * 100, 'cost': cost, 'revenue': revenue}            
        enriched_campaigns[source] = enriched_indicators
    
    return dict(sorted(enriched_campaigns.items(), key=lambda k: k[1]['ROI'], reverse=True))


campaigns = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}

print (f'Sample campaigns data:\n{campaigns}')
print (f'Enriched with ROI result:\n{enrich_with_roi(campaigns)}')

