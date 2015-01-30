# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 23:38:31 2014

@author: shubhamgoel
"""

import numpy as np

# Vertices represent Madhya_Pradesh,Gujarat,Rajasthan,Maharashtra,UP and Delhi in the same order
Ques3 = np.matrix(((0, 1, 1, 1, 1),(1, 0, 1, 1, 0),(1, 1, 0, 0, 1),(1, 1, 0, 0, 1),(1, 0, 1, 1, 0)))

Ques4 = np.matrix(((0, 1, 1, 1, 1, 0),(1, 0, 1, 1, 0, 0),(1, 1, 0, 0, 1, 0),(1, 1, 0, 0, 1, 0),(1, 0, 1, 1, 0, 1),(0, 0, 0, 0, 1, 0)))

def connected(adj_mat):
    convert = adj_mat**len(adj_mat)
    for i in range(0,len(adj_mat)):
        for j in range(0,len(adj_mat)):
            if not i==j:
                if convert.item(i+j) ==0:
                    return 'Graph is disconnected'
    return 'Graph is connected'                
    