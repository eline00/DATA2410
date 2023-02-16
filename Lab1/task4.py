#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 12:07:19 2023

@author: elinejorgensen
"""

values = []

with open('throughputs2.txt', 'r') as file:
    for line in file:
        words = line.split()
        
        if words[1] == "Kbps":
            words[0] = int(words[0]) / 1000
            
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

print(values)
print ("JFI = ", jainsall(values))