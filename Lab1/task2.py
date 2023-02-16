#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:24:07 2023

@author: elinejorgensen
"""

def jainsall(values):
    sum1 = 0
    sum2 = 0
    N = len(values)
    
    for i in values:
        sum1 += i
        sum2 += i**2
        
    JFI = (sum1**2) / (N * sum2)
    
    return JFI

liste = {7, 12, 15, 32}

print("JFI = ", jainsall(liste))

