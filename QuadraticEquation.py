# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:41:06 2020

@author: hrith
"""
import math

a = int(input("Enter The Value Of a: "))
b = int(input("Enter The Value Of b: "))
c = int(input("Enter The Value Of c: "))
D = b**2 - 4*a*c


R1 = (-b + math.sqrt(D))/2*a
R2 = (-b - math.sqrt(D))/2*a

print("The First Root Of Equation Is: ",R1)
print("The Second Root Of Equation Is: ",R2)