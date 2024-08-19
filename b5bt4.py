# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:21:20 2024

@author: AT
"""
def time_to_seconds(time_str):
    h,m, s = map(int, time_str.split(':'))
    total_seconds = h * 3600 + m * 60 + s
    return total_seconds
time_input = input("nhap thoi gian theo dinh dang hh:mm:ss:")
seconds = time_to_seconds(time_input)
print(f"tong so day la: {seconds}")   
