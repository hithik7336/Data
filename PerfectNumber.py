# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:26:30 2020

@author: hrith
"""


n = int(input("Enter The Number: "))
sum = 0

for i in range(1,n+1):
    if n%i == 0:
         print("Factor",i,"Is: ",i)
         sum = sum+i
    
print("The Sum Of Factors Is: ",sum)

if(sum == n*2):
    print(n,"Is A Perfect Number")
else:
    print(n,"Is Not A Perfect Number")
    
    