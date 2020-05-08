# -*- coding: utf-8 -*-
"""
Created on Fri May  8 13:31:31 2020

@author: hrith
"""


def Pnp():
    
    Palinderome = []
    
    Not_Palinderome = []
    
    Words = ("NITIN","HRITHIK", "MALAYALAM", "APPLE", "MADAM", "SCIENTIST", "RADAR", "LUKES", "CIVIC", "LOS ANGELES")
    
    for i in Words:
        if i == i[::-1]:
            Palinderome.append(i)
            
    print("The Palinderome List Is: ","\n",Palinderome)

    print("\n")
    
    for j in Words:
        if j != j[::-1]:
            Not_Palinderome.append(j)
            
    print("The Non Palinderome Is: ","\n",Not_Palinderome)
    
    
Pnp()