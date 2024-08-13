# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:16:59 2024

@author: anh tai
"""
import random
luachon = [ "keo", "bua", "bao"]
ngchoi = input (" lua chon (keo - bua - bao):")
may = random.choice(luachon)
print(f"ban chon:  {ngchoi}")
print(f"may chon:  {may}")
if ngchoi == may:
    print ("hoa")
elif may == " bua" and ngchoi == "keo" or\
    may == "keo" and ngchoi == "bao" or\
        may == "bao" and ngchoi =="bua":
    print("may thang")
else:
    print("may thua")