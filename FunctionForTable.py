# -*- coding: utf-8 -*-
"""
Created on Fri May  8 13:24:39 2020

@author: hrith
"""


n = int(input("Enter The Number: "))

def table(a):
    
    for i in range(1,11):
        print(a,"X",i,"=",a*i)

table(n)    