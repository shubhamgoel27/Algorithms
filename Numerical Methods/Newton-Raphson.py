# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 15:51:41 2015

@author: shubham
"""

import numpy
from sympy import *

START = 0  # Interval starting point   
END = 6    #Interval ending point
TOLERANCE = 0.0001   #Tolerance level
ITER = 500    # Maximum number of iterations
i=0
x = Symbol('x')

def fn(value, function):
    ''' Returns the value of  input function for the given value
    '''
    return function.subs(x,value)
    
def derivative(y):
    '''Returns derivative of the function
    '''
    return y.diff(x)

def newton_raphson(x0 = 2, function = x**2 -1):
    ''' Returns the root of the input function
        x0 is the initial guess
        
    '''
    print 'Starting Newton Raphson'
    while abs(fn(x0, function)) > TOLERANCE:
        fx_n = fn(x0, function)
        fprime_n = derivative(function).subs(x,x0)
        x0 = x0 - (fx_n/fprime_n)
        print x0
        
    return x0    
    
print newton_raphson()  
    