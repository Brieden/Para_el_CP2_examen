# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:06:46 2018

@author: briedens
"""
import numpy as np

#S = lambda n_min, n_max: np.sum([ (-1)**n / abs( x + n * l)  for n in range(n_min, n_max)])
S = lambda n_min, n_max: np.sum([ (-1)**n / abs( x + n * l)  for n in range(n_min, n_max+1)]) #ML: Hier fehlt der letzte Term
x = 0.2
l = 1
genauigkeit = 1e-5
ergebnis = 3.53834  # ML: Wo kommt das Ergebnis her?
terme = 0

#while abs( ergebnis - S(-terme, terme)) > genauigkeit:
    terme +=1 # ML: sehr ineffizient, die Summe muß 2e5 mal neu berechnet werden 

#ML edit:
print(S(-200000,200000))
print(S(-200001,200001))
print(S(-200002,200002))

print("Es werden %i Terme benötigt." %terme) 
