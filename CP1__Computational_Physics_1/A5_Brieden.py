# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:10:34 2018

@author: briedens
"""
import numpy as np

A = np.array( [[10, -7, 0],
               [-3,  2, 6],
               [ 5, -1, 5]] )
b = np.array( [7.1, 3.9, 6] )
x = np.linalg.lstsq(A, b)[0]
r = abs(np.dot(A, x) - b)
con = np.linalg.cond(A)
print("x = ", x)
print("Residual r = ", r)
print("condition: ", con)