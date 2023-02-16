#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:45:12 2023

@author: elinejorgensen
"""

values = []

with open('throughputs.txt', 'r') as file:
    for line in file:
        words = line.split()
        values.append(int(words[0]))
        

def jainsall(values):
    sum1 = 0
    sum2 = 0
    N = len(values)
    
    for i in values:
        sum1 += i
        sum2 += i**2
        
    JFI = (sum1**2) / (N * sum2)
    
    return JFI


print ("JFI = ", jainsall(values))