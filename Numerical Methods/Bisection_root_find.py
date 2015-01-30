# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 13:51:14 2015

@author: shubham
"""
    
START = -10   # Interval starting point   
END = 6    #Interval ending point
TOLERANCE = 0.001   #Tolerance level
ITER = 500    # Maximum number of iterations
i=0

def calculate(value, function):
    ''' Returns the value of  input function for the given value
    '''
    x = value * 1.0
    return eval(function)
    
def bisection(start = START, end = END ,function = "x**3 + 1",tolerance = TOLERANCE, max_iter = ITER):
    global i
    i +=1
    while i<max_iter:        
        mid = (start + end)/2.0
        if abs(calculate(mid, function)) < tolerance:
            return "The approximate root is " + str(mid)
        elif func(start)*func(mid)<=0.0:
            return bisection(start, mid)   # Search in the left half part of interval now
        else:
            return bisection(mid, end)     # Search in the right half part of interval now
    return "No root found in the given interval"            

print bisection(function="x**2 - 1")