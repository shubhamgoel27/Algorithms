# -*- coding: utf-8 -*-
"""
Created on Tue Feb  3 00:58:22 2015

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

def second_derivative(y):
    '''Returns derivative of the function
    '''
    first = y.diff(x)
    return first.diff(x)
    
def chebychev(x0 = 2, function = x**2 -1):
    ''' Returns the root of the input function
        x0 is the initial guess
    '''
    #print 'Starting Chebychev'
    while abs(fn(x0, function)) > TOLERANCE:
        fx_n = fn(x0, function)
        fprime_n = derivative(function).subs(x,x0)
        
        f2prime_n = second_derivative(function).subs(x, x0)
        x0 = x0 - (fx_n/fprime_n) #Left part
        x0 = x0 - (1/2)* ((fx_n/fprime_n)**2)* (f2prime_n/fx_n)       
    return x0    
    
    
print N(chebychev())