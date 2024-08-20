# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:46:57 2024

@author: AT
"""

a = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
b = a.replace("P.","").replace("Q.","").replace("Tp.","").split(",")
print("a, b (Yêu cầu 2):")
for sub in b:
    print(sub)
