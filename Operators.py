# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 22:09:07 2020

@author: hrith
"""

a = 10

b = 2

c = [1,2,3,4,5,6]

d = "Hrithik Sharma"

# ARITHMATIC OPERATORS

print("The Sum Of Is: ",a+b)
print("The Difference Is: ",a-b)
print("The Product Is: ",a*b)
print("The Quotient Is: ",a/b)
print("The Remainder Is: ",a%b)
print("The Floor Division Is: ",a//b)
print("Power: ",a**b)

# BITWISE OPEARATORS

print("&: ",a&b)
print("|: ",a|b)
print("~: ",~a," ",~b)
print("^: ",a^b)
print("<<: ",a<<b)
print(">> ",a>>b)

# LOGICAL OPERATORS

print("and: ",a>20 and b<5)
print("or: ",a>20 or b<3)
print(not(a>20 and b<5))

# IDENTITY OPERATORS

print("IS ",c is d)
print("IS NOT: ",c is c)

# MEMEBERSHIP OPERATORS

print("IN: ","Z" in d)
print("NOT IN: ","H" not in d)
print("IN: ","M" in c)
print("NOT IN: ",5 not in c)

# COMPARISON OPERATORS

print("=: ",a==b)
print("<=: ",a<=b)
print(">= ",a>=b)
print(">: ",b>a)
print("<: ",b<a)
print("!=: ",a!=b)


a+=10
a-=10
a*=10
a/=10
a**=2
b**=10