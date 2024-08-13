# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:47:22 2024

@author: anh tai
"""
km = float(input("Số km quãng đường đi được:"))
if km <= 3:
    if km > 1:
        x = km * 13
        print(f" số tiền phải trả là {x}K")
    else:
        print(" sóo tiền phải trả là ")
else:
    if km <= 8:
        x = 39 + (km - 3) * 12
        print(f" só tiền phải trả là {x}")
    else:
        x = 39 + 5 * 12 + (km - 8) * 10
        if x > 100:
            a = x * 0.92
            print(f" số tiền phải trả là {a}K")
        else:
            a = x
            print(f" số tiền phải trả là {a}")
            
