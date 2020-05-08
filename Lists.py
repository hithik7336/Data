# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:14:30 2020

@author: hrith
"""


Cities = ["Los Angeles", "San Jose", "San Francisco", "San Bruno", "San Diego", "San Antonio"]

print(type(Cities))

Num = ["Hrithik", 1, 7.6, [12,78,5], ["LA", "NY"], 4+2j]

Digits = [92,32,12,46,94,86,0,9,34,64,78,32]

print(type(Num))

print("The Reverse Of Cities List: ",Cities[::-1])

print("The Reverse Of Num List: ",Num[::-1])

print(Cities[2])

print(Cities[1:4])

print(Num[3][1])

for i in Cities:
    print(i)
    
for j in Num:
    print(j)
    
Cities.append("New York")
print(Cities)

Cities.insert(3,"Las Vegas")
print(Cities)

Cities.extend(["Washington DC"])
print(Cities)

Cities.extend(["Washington DC", "Cambridge"])
print(Cities)

Cities.remove("Washington DC")
print(Cities)

Cities.pop(9)
print(Cities)

Cities.reverse()
print(Cities)

print(Cities.index("Washington DC"))

Digits.sort()
print(Digits)

print(Cities.count("San Jose"))

Cities2 = Cities.copy()
print(Cities2)

Cities.clear()
print(Cities)






