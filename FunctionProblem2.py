# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:09:20 2020

@author: hrith
"""


Names = ("Hrithik", "Hitesh", "Himanshu", "Akhil", "Anaa", "Ankit", "Kinsey", "Kiana", "Karen")

H = []

K = []

A =[]

def HF():
    
    for i in Names:
        if i.startswith("H"):
            H.append(i)
    print(H)
            
def KF():
    
    for j in Names:
        if j.startswith("K"):
            K.append(j)
    print(K)
            
def AF():
    
    for k in Names:
        if k.startswith("A"):
            A.append(k)
    print(A)
 
HF()
print("\n")
KF()
print("\n")
AF()      
    
    
    
            