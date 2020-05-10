# -*- coding: utf-8 -*-
"""
Created on Sat May  9 12:53:15 2020

@author: hrith
"""

import Calc

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("\n")

print("The Sum Is: ",Calc.Sum(a,b))
print("The Difference Is: ",Calc.Sub(a,b))
print("The Product Is: ",Calc.Mul(a,b))
print("The Divisor Is: ",Calc.Def(a,b))

print("\n")

from Calc import *

print("The Sum Is: ",Sum(a,b))
print("The Difference Is: ",Sub(a,b))
print("The Product Is: ",Mul(a,b))
print("The Divisor Is: ",Def(a,b))

print("\n")

from Calc import Sum
print(Sum(a,b))

from Calc import Sub
print(Sub(a,b))

from Calc import Mul
print(Mul(a,b))

from Calc import Def
print(Def(a,b))

