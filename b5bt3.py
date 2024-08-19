# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:40:21 2024

@author: PC
"""
N = int(input("nhập số nguyên dương N co 2 chu  :"))
hang_chuc = N // 10
hang_don_vi = N % 10
tong_chu_so = hang_chuc + hang_don_vi
print(f"tong 2 chu so cua N là: {hang_chuc} + {hang_don_vi} = {tong_chu_so}")
