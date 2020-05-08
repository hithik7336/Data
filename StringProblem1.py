# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:32:14 2020

@author: hrith
"""


S = input("Enter The string: ")

if len(S)>3:
    print(S)

if S.endswith("ing") == False:
        S+="ing"
        print(S)
    
if S.endswith("ing") == True:
    S = S.replace("ing","ly")
    print(S)
    
    