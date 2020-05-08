# -*- coding: utf-8 -*-
"""
Created on Mon May  4 20:19:40 2020

@author: hrith
"""


String1 = "Hrithik Sharma"
String2 = "Los Angeles"
String3 = "Data Scientist"
String4 = "Apple"
String5 = 'python is very great language'
String6 = 'JAVA IS BORING LANGUAGE'

print("The Length Of String 1 Is: ",len(String1))
print("The Length Of String 2 Is: ",len(String2))
print("The Length Of String 3 Is: ",len(String3))
print("The Length Of String 4 Is: ",len(String4))

print('\n')

print("The Reverse Of String 1 Is: ",String1[::-1])
print("The Reverse Of String 2 Is: ",String2[::-1])
print("The Reverse Of String 3 Is: ",String3[::-1])
print("The Reverse Of String 4 Is: ",String4[::-1])

print('\n')

print("My Name is {} I Live In {} I am a {} & I Work For {}".format(String1, String2, String3, String4))

print('\n')

print("My Name Is {}".format(String1))
print("I Live In {}".format(String2))
print("I Am A {}".format(String3))
print("I Work For {}".format(String4))
print("My Salary Is {}".format("$500K"))

print('\n')

print(String1[0])
print(String1[1:6])
print(String3[-5])
print(String2[4:])

print('\n')

print(String5.capitalize())
print(String6.casefold())
print(String4.count('p'))
print(String4.replace("p","z"))
print(String6.split(" "))
print(String2.index('A'))
print(String6.endswith('E'))
print(String5.startswith('p'))
print(String6.lower())
print(String5.upper())
print(String4.find('l'))
print(String3.title(), String4.title())


for i in String1:
    print(i)
    
    