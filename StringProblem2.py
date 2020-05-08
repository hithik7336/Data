# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:52:46 2020

@author: hrith
"""


Names = ["Hrithik", "Kiran", "Ojasvi", "Sebastian", "Danielle"]
Size = []

for i in Names:
    Size.append(len(i))
    Size.sort()
    
print("The Length Of Longest String Is: ",Size[4])