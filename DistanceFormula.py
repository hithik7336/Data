# -*- coding: utf-8 -*-
"""
Created on Fri May  1 14:50:38 2020

@author: hrith
"""
import math

x1 = int(input("Enter First X Coordinate: "))
y1 = int(input("Enter First Y Coordinate: "))

x2 = int(input("Enter Second X Coordinate: "))
y2 = int(input("Enter Second Y Coordinate: "))

Dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("The Distance Between Two Points Is: ",Dist)