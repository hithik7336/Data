# -*- coding: utf-8 -*-
"""
Created on Sun May  3 12:50:14 2020

@author: hrith
"""


n =int(input("Enter The Number: ")) 
rev = 0
  
while(n > 0): 
    a = n % 10
    rev = rev * 10 + a 
    n = n // 10
      
print(rev) 