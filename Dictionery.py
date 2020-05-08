# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:04:02 2020

@author: hrith
"""


Rec1 = {"Name":"Hrithik Sharma", "ID":101, "Designation":"Data Scientist", "Salary":150000}
Rec2 = {"Name":"Shubham Sharma", "ID":102, "Designation":"Digital Marketer","Salary":120000}
Rec3 = {"Name":"Akhil Thakur", "ID":103, "Designation":"Data Scientist", "Salary":150000}
Rec4 = {"Name":"Ridhima Sharma", "ID":104, "Designation": "Food Engineer", "Salary":132000}
Rec5 = {"Name":"Kiran Thakur", "ID":105, "Designation":"Biotechnologist", "Salary":132000}
Rec6 = {"Name":"Khushbu Pathania","ID":106,"Designation":"PHP Developer", "Salary":132000}

print(Rec1)
print(Rec2)
print(Rec3)
print(Rec4)
print(Rec5)
print(Rec6)

print("\n")

Job = ["Data Scientist", "Digital Marketer", "App Developer", "Biotechnologist"]
Salary = [150000, 120000, 132000, 132000]

L = dict(zip(Job,Salary))

print(L)

print("\n")

for i in L.keys():
    print(i)

print("\n")
    
for j in L.values():
    print(j)

print("\n")

for k in L.items():
    print(k)
 
M = L.copy()   

print(M) 

print(L is M)

print(L.get('App Developer'))

L.pop('App Developer')

L.popitem()



    
