# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 21:31:00 2024

@author: anh Tai
"""
from math import sqrt

print(" giai phuong rinh bac 2: ax^2+bx+c=0")
a = float(input("nhap a:"))
b = float(input("nhap b:"))
c = float(input("nhap c:"))

if a==0:
    if b==0:
        if c==0:
            print("phuong trinh co vo so nghiem")
        else:
            print("phuong trinh vo nghiem")
    else:
        if c==0:
            print("phuong trinh co 1 nghiem x = 0")
        else:
            print("phuong trinh co nghiem x =" -b / a)
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("phuong trinh vo nghiem")
    elif delta == 0:
        print("phuong trinh co 1 nghiem x =" -b / (2*a))
    else:
        print("phuong trinh co hai nghiem phan biet")
        print("x1 = ", float((-b - sqrt(delta) / (2*a))))
        print("x2 = ", float((-b + sqrt(delta) / (2*a))))