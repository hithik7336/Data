# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:47:37 2020

@author: hrith
"""


import numpy as np

np.random.seed(210)

X = np.random.randint(1,10,6)

X = list(X)

print("The List Is: ",X)

def ProductOfElements():
    
    product = 1
    
    for i in X:
         product = product*i
         
    print("The Product Of Elements Of List Is: ",product)
    
ProductOfElements()
        