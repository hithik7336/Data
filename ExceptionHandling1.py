# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:39:41 2020

@author: hrith
"""


a = int(input("Enter First Number: "))

b = int(input("Enter Second Number: "))

S = input("Enter A String: ")

try:
    print(a/b)
    
    k = int(input("Enter a Value: "))
    
    print(S[20])
    
except ValueError as e:
    
    print("Enter An Integer Value: ",e)
    
except ZeroDivisionError as e:
    
    print("You Cannot Divide A Number By Zero: ",e)   
    
except IndexError as e:

    print("String Index Out Of Bound: ",e)    

finally:
    
    print("It Will Execute Whether There Is Exception Or Not")
    
