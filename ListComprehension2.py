# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:11:47 2020

@author: hrith
"""


Names = ["Hrithik", "Kiran", "Shubham", "Ridhima", "Nina", "Paul", "Yashvardhan", "Ovi", "Inna", ]

name = []

for i in Names:
    if i.startswith("P"):
        name.append(i)
    
    
name2 = []

for j in Names:
    if len(j)>4:
        name2.append(j)
        
        
o = [l for l in Names if l.endswith("a")]



