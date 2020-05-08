# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:05:38 2020

@author: hrith
"""


Names = ["Hrithik","Hrithik", "Kiran", "Akhil", "Akhil", "Kiran", "Mallu", "Mallu", "Mallu", "Hrithik"]

Uni = []

def Unique():
    
    for i in Names:
        if i not in Uni:
            Uni.append(i)
            
    print(Uni)
    
Unique()