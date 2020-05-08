# -*- coding: utf-8 -*-
"""
Created on Sat May  2 21:54:41 2020

@author: hrith
"""


n = int(input("Enter The Number Upto Sum Is Required: "))
sum = 0

for i in range(1,n+1):
    sum = sum+i

print("The Sum Of First",n,"Numbers Is: ",sum)
    