# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:37:38 2020

@author: hrith
"""


N = ["Hrithik", "Kiran", "Shubham", "Ridhima", "Nina", "Paul", "Yashvardhan", "Ovi", "Inna", ]

for i in N:
    for j in i:
        print(j)
        
Z = [j for i in N for j in i]
