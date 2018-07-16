# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:09:02 2018

@author: briedens
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def fun(y, t):
    x0, x1 = y
    df = [x1, -(4 * x0**2 - 2) * x1 - x0**5 + 2 * x0**3 - 2*x0]
    return df
steps = 500
t = np.linspace(0, 4, steps)
y_0 = [1,0]
l = odeint(fun, y_0, t)
t_4 = (abs(t-4)).argmin()

print("Bei t = %.0f ergibt sich eine Position von x = %.3f und eine Geschwindigkeit von x' = v = %.3f" %( t[t_4], l[t_4,0], l[t_4,1]))
print("Ich habe odeint von scipy.integrate benutzt es benutzt lsoda von der FORTRAN library odepack.  \
      \n Dabei habe ich %i Zeitschritte benutzt."%steps)
plt.plot(t, l)
plt.show()