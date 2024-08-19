# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:51:55 2024

@author: AT
"""
a = int(input("nhap so a:"))
b = int(input("nhap so b:"))
tong = a + b
hieu = a - b
tich = a * b
thuong1 = round(a / b, 2)
thuong2 = round(a / b, 3)
print(f"tong cua {a} va {b} la: {tong}")
print(f" hieu cua {a} va {b} la: {hieu}")
print(f" tich cua {a} va {b} la: {tich}")
print(f" thuong cua {a} va {b} lam tron 2 chu so sau dau cham la: {thuong1} ")
print(f"thuong cua {a} va {b} lam tron 3 chu so sau dau cham la: {thuong2}")
