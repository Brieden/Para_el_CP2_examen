# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:06:46 2018

@author: briedens
"""
import numpy as np

S = lambda n_min, n_max: np.sum([ (-1)**n / abs( x + n * l)  for n in range(n_min, n_max)])
x = 0.2
l = 1
genauigkeit = 1e-5
ergebnis = 3.53834
terme = 0

while abs( ergebnis - S(-terme, terme)) > genauigkeit:
    terme += 1
    
print("Es werden %i Terme benötigt." %terme)