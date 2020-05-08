# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:51:31 2020

@author: hrith
"""


String = input("Enter A String: ")

String_Rev = String[::-1]

if String == String_Rev:
    print("The String Is Palinderome")
    
else:
    print("The String Is Not Palinderome")
    
