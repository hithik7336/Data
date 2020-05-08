# -*- coding: utf-8 -*-
"""
Created on Fri May  8 16:50:18 2020

@author: hrith
"""


n = int(input("Enter A Number: "))

def Factorial(a):
    
    fact = 1
    
    for i in range(1,n+1):
        fact = fact * i
        
    print("The Factorial Of Above Number Is: ",fact)
    
Factorial(n)