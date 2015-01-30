# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 21:18:26 2015

@author: shubham
"""

def count_split(A,B):
    ''' Returns the number of inversions of the original array split into two sorted arrays
        A is the right part of that array and B the left one. '''
        
    n = len(A) + len(B)
    C = []
    i=0
    j=0
    invs = 0
    for k in range(n):
        if A[i] < B[j]:
            C.append(A[i])
            i+=1
        elif A[i] > B[j]:
            C.append(B[j])
            j+=1
            invs += (len(A)-i)
        if i==len(A):
            C = C + B[j:]
            return invs, C
        if j==len(B):            
            C = C + A[i:]
            return invs, C            
    return invs, C


def inversion(A):
    """ Returns the total number of inversions and the sorted array
        Takes an array as an input
        Uses a modified merge sort thus having O(nlogn) running time
    """
    n = len(A)
    if n==1:
        return 0, A
    else:
        left_inv, left = inversion(A[:n/2])
        right_inv, right = inversion(A[n/2:])
        split, merged = count_split( left, right)
    return left_inv + right_inv + split, merged    
    
def read_array(path):
    ''' Reads data of the following format into an integer array:
        Each line of the input should have single integer element 
        '''
    f = open(path)
    long_array = f.readlines()
    long_array = [int(x) for x in long_array]
    return long_array
        
inversions, sorted_array = inversion(read_array('Data/IntegerArray.txt'))
print inversions
