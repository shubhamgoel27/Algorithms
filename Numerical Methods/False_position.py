# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 18:08:13 2015

@author: shubham
"""
from math import *
    
START = 0  # Interval starting point   
END = 6    #Interval ending point
TOLERANCE = 0.0001   #Tolerance level
ITER = 500    # Maximum number of iterations
i=0

def fn(value, function):
    ''' Returns the value of  input function for the given value
    '''
    x = value * 1.0
    return eval(function)
    
def false_position(a = START, b = END, function = "x**2 -1", tolerance = TOLERANCE, max_iter = ITER):
    """ Returns the root of the input function using the Regula-Falsi method
        INPUT: a(float/int) = start of the interval
               b(float/int) = end of the interval
               function(str) = function whose roots are needed
               tolerance(float) = deviation from the original answer allowed
               max_iter(int) = Maximum iterations allowed
    """
    i=0    
    while i<max_iter:
        i+=1
        fn_a = fn(a, function)
        fn_b = fn(b, function)
        c = ((b*fn_a) - (a*fn_b))/ (fn_a - fn_b)
        fn_c = fn(c, function)
        if abs(fn_c) < tolerance:
            return c
        elif (fn_a * fn_c) < 0:
            b = c
        else:
            a = c
    return "No root in given interval"
        
print false_position()        