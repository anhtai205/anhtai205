# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:22:20 2024

@author: AT
"""
str_input = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
sub_strings = str_input.split(", ")
print("Các sub-string (Yêu cầu 1):")
for sub in sub_strings:
    print(sub)