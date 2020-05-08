# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:44:39 2020

@author: hrith
"""


import numpy as np

X = np.random.randint(1,100,20)

np.random.seed(765
               )
Sig = []

for i in X:
    i=1/(1+np.exp(-i))
    if i<= 1:
        Sig.append(i)
        
