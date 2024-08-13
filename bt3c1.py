# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:00:37 2024

@author: anh 
"""

a = float(input("nhập số a:"))
b = float(input("nhập số b:"))
c = float(input("nhập số c:"))
if a + b > c and a + c > b and b + c > a:
     print ("a, b, c la 3 canh cua 1 tam giac")
else:
     print("a, b, c ko la 3 canh cuar tam giac")
 