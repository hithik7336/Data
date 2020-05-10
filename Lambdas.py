# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:28:57 2020

@author: hrith
"""

c = int(input("Enter First Number: "))
d = int(input("Enter Second Number: "))
N1 = input("Enter First Name: ")
N2 = input("Enter Last Name: ")


y = lambda x: x**2

z = lambda x: x**3

u = lambda a,b: a+b

Name = lambda fname, lname: fname.strip().title()+" "+lname.strip().title()

print("\n")

print(y(c))

print("\n")

print(z(d))

print("\n")

print(u(c,d))

print("\n")

print(Name(N1,N2))





