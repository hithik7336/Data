# -*- coding: utf-8 -*-
"""
Created on Wed May  6 22:14:38 2020

@author: hrith
"""


Names = ("Hrithik", "Hitesh", "Himanshu", "Kiran", "Kinsey", "Kiara", "Kyra")

fr1 = []
fr2 = []

for i in Names:
    if i.startswith("K"):
        fr1.append(i)
        
for j in Names:
    if j.startswith("H"):
        fr2.append(j)
        
print(fr1)
print('\n')
print(fr2)
