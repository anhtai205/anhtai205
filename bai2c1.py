# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:12:17 2024

@author: anh tai
"""
a = float(input("nhap so a:"))
b = float(input("nhap so b:"))
if a == 0 :
    if b == 0:
        print("phuong trinh co vo so nghiem")
    else:
        print("phuong trinh vo nghiem")
else:
    print("phuong trinh co nghiem x=", -b / a)        