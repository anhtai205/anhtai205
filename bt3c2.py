# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:27:22 2024

@author: anh tai
"""

a = float(input("nhập số a:"))
b = float(input("nhập số b:"))
c = float(input("nhập số c:"))
if a ** 2 + b ** 2 == c ** 2:
    print("a, b, c la 3 canh cua 1 tam giac vuong")
elif a == b == c:
    print("a, b, c la 3 canh cua 1 tam giac deu")
elif a == b or a == c or c == b:
    print("a, b, c la 3 canh cua 1 tam giac can")
elif (a ** 2 + b ** 2 == c ** 2 and a == b) or  (a ** 2 + c ** 2 == b ** 2 and a == c) or (c ** 2 + b ** 2 == a ** 2 and b == c):
  print("a, b, c la 3 canh cua 1 tam giac vuong can")  
  
