# -*- coding: utf-8 -*-
"""
Created on Sun May 10 13:13:50 2020

@author: hrith
"""


a = int(input("Enter First Number: "))

b = int(input("Enter Scenond Number: "))

"""

Zero Division Error Exception

"""

try:
    
    print(a/b)
    
except ZeroDivisionError as e:
    
    print("You Cannot Divide A Number By Zero: ", e)
    
"""

Value Error Exception

"""
    
try:
    
    p = int(input("Enter A Number: "))
    
except ValueError as e:
    
    print("Enter An Integer Value: ", e)
    
"""
String Index Out Of Bound

"""
    
try:
    
    S = input("Enter String: ")
    
    print(S[20])
    
except IndexError as e:
    
    print("String Index Out Of Bound: ", e)  
    

finally:
    
    print("I'll Execute Whether There Is Exception Or Not ")

    
    
    
    

