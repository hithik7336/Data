# -*- coding: utf-8 -*-
"""
Created on Wed May  6 22:59:40 2020

@author: hrith
"""


Words = ("MALAYALAM","PYTHON","NITIN","JAVA","RADAR","CIVIC","MADAM","ROVER","HELLO","FOREVER","BMW","LOVE")

P = []

for i in Words:
    if i == i[::-1]:
        P.append(i)
        
NP = []

for j in Words:
    if j != j[::-1]:
        NP.append(j)
        
