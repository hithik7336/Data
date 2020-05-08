# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:26:37 2020

@author: hrith
"""


import numpy as np

np.random.seed(101)

X = np.random.randint(1,100,10)

Y =list(X)

print("The List Is: ",Y)

def SumOfListElements():
    
    Sum = 0
    
    for i in Y:
        Sum+=i
    print("Them Sum Of Elements Of List: ",Sum)
    

SumOfListElements()
        
    
    

