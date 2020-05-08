# -*- coding: utf-8 -*-
"""
Created on Thu May  7 15:34:05 2020

@author: hrith
"""


x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

print("\n")

def Add(a,b):
    A = a+b
    print("The Sum Is: ",A)
    
def Sub(a,b):
    S = a-b
    print("The Difference Is: ",S)
    
def Pro(a,b):
    P = a*b
    print("The Product Is: ",P)
    
def Div(a,b):
    D = a/b
    print("The Quotient Is: ",D)
    
def FloDiv(a,b):
    FD = a//b
    print("The Floor Division Is: ",FD)
    
def Rem(a,b):
    R = a%b
    print("The Remainder Is: ",R)
    
def Exp(a,b):
    E = a**b
    print("Raised To Power: ",E)
    
Add(x,y)
Sub(x,y)
Pro(x,y)
Div(x,y)
FloDiv(x,y)
Rem(x,y)
Exp(x,y)
