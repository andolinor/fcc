#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np

def calculate(lst: list):
    
    if len(lst) < 9:
        raise ValueError('List must contain nine numbers.')
        
    d = {'mean': None, 'variance': None, 'standard deviation': None,
        'max': None, 'min': None, 'sum': None}
    a = np.array(lst).reshape(3,3)
        
    d['mean'] = [list(a.mean(axis=0)), list(a.mean(axis=1)), a.mean()]
    d['variance'] = [list(a.var(axis=0)), list(a.var(axis=1)), a.var()]
    d['standard deviation'] = [list(a.std(axis=0)), list(a.std(axis=1)), 
                               a.std()]
    d['max'] = [list(a.max(axis=0)), list(a.max(axis=1)), a.max()]
    d['min'] = [list(a.min(axis=0)), list(a.min(axis=1)), a.min()]
    d['sum'] = [list(a.sum(axis=0)), list(a.sum(axis=1)), a.sum()]
    
    return d

