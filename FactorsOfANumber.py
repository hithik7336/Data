# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:21:26 2020

@author: hrith
"""


n = int(input("Enter Any Number: "))

for i in range(1,n+1):
    if n%i == 0:
        print("Factor",i,"Is: ",i )
        
        
        