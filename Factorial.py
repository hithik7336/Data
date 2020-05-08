# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:13:58 2020

@author: hrith
"""


n = int(input("Enter The Number: "))

fact = 1

for i in range(1,n+1):
    fact = fact*i
    
print("The Factorial Of",n,"Is: ",fact)    


