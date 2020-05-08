# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:35:58 2020

@author: hrith
"""


import sys

Fruits = ("Apple", "Banana", "Mango", "Kiwi", "Pineapple","Apple")

for i in Fruits:
    print(i)
    
print("\n")

print("The Type This Data Is: ",type(Fruits))

print("The Size Of Above Tuple Is: ",sys.getsizeof(Fruits))

print("The Length Of Above Tuple Is: ",len(Fruits))

print("The Number Of Apple In The Fruits: ",Fruits.count("Apple"))

print("The Index Of Banana Is: ",Fruits.index("Banana"))

print("\n")

print(Fruits[1:5])

print("The Reverse Of Above Tuple Is: ",Fruits[::-1])

a,b,c = 1,2,3

Z = 1,2,3,4,5

print(Z)

print("The Type Of z Is: ",type(Z))

