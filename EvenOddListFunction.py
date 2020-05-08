# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:19:43 2020

@author: hrith
"""


Num = list(range(1,21))

E = []
O = []

def Even():
    
    for i in Num:
        if i%2 == 0 not in E:
            E.append(i)
            
    print(E)
    
def Odd():
    
    for j in Num:
        if j%2 != 0 not in O:
            O.append(j)
            
    print(O)
    
Even()
print("\n")
Odd()