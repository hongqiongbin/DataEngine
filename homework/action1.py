
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:36:57 2021

@author: HongQiongbin
"""
total=0
for number in range(1,100):
    if number%2==1:
        continue
    total=total+number
print(total)