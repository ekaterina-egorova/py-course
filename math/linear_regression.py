#!/usr/bin/env python
# coding: utf-8

# In[71]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def linear_regression(x, y):
    meanx = np.mean(x)
    meany = np.mean(y)
    covxy = np.cov(x, y)[0][1]
    stdx = np.std(x)
    astar = covxy/stdx**2
    bstar = meany - covxy * meanx / stdx**2
    
    print (f"x = {x}")
    print (f"y = {y}")
    print (f"Mean of x = {meanx}")
    print (f"Mean of y = {meany}")
    print (f'Std of x = {stdx}')
    print (f'cov(x,y) = {covxy}')
    print (f'a* = {astar}')
    print (f'b* = {bstar}')
    
    ystar = []
    for i in x:
        ystar.append(astar * i + bstar)
        
    return ystar
    

plt.xlabel('x')
plt.ylabel('y')

sample_size = 10

x = []
for i in range(sample_size):
    x.append(i)
    
sample = norm(loc=0, scale=0.5).rvs(size=sample_size)
y0, y = [], []
for i in x:
    y0.append(0.5*i)
    y.append(0.5*i + sample[i])

plt.plot(x, y0, color= 'blue')
plt.plot(x, y, marker='o', color='green', ls='')
plt.plot(x, linear_regression(x, y), color="green")

plt.xlim(0, sample_size)
plt.ylim(0, sample_size)

print ("Blue -- original 0.5*x line, green -- built line:")

