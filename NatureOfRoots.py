# -*- coding: utf-8 -*-
"""
Created on Fri May  1 17:13:38 2020

@author: hrith
"""


a = int(input("Enter The Value Of a: "))
b = int(input("Enter The Value Of b: "))
c = int(input("Enter The Value Of c: "))
D = b**2 - 4*a*c
print('\n')
print("The Discrinent Is: ",D)

if D>0:
    print("Real And Distinct Roots")
    
elif D==0:
        print("Equal Roots")
        
else:
    print("Imaginery Roots")
            
            