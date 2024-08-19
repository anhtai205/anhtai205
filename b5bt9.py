# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:21:04 2024

@author:
"""

import math
a = float(input("nhap a:"))
b = float(input("nhap b:"))
A = (math.sqrt(a) - math.sqrt(b))/(math.pow(a, 0.25) - math.pow(b, 0.25))
B = (math.sqrt(a) + math.pow(a*b, 0.25))/(math.pow(a, 0.25) + math.pow(b, 0.25))
print("ket qua:", A - B)
