# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 21:26:55 2014

@author: shubhamgoel
"""

def gray_code(n):
        gray_code = []
        
        for number in xrange(1<<n):
            new = number ^ (number>>1)
            gray_code.append([new,bin(new)[2:]])
        
        return gray_code
        
n = raw_input('Enter the no. of bits: ')
print gray_code(int(n))        