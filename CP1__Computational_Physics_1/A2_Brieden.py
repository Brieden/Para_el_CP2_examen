# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:07:58 2018

@author: briedens
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fmin


f = lambda x: np.cos(x) * np.sinh(x) - 1
grobe_schätzung = [4, 8, 11, 14, 17]

nullstellen = [] 
for x_0 in grobe_schätzung:
    nullstellen.append(fmin(lambda x: abs(f(x)), x_0, disp=0))
print("Die Nullstellen liegen bei:")
for i in nullstellen:
    print("%.5f"%i[0])
    
x = np.linspace(0,20,300)
plt.plot(x, f(x))
plt.vlines(nullstellen, -.5, .5, linestyles = "--", lw = 3, colors = "C1")
plt.hlines(0,0,20, linestyles="--", colors = "C1")
plt.ylim(-1,1)
plt.show()