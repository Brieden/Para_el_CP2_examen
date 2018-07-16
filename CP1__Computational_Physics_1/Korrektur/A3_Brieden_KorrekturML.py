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
    df = [x1, -(4 * x0**2 - 2) * x1 - x0**5 + 2 * x0**3 - 2*x0] # ML: hier könnte man optimaler arbeiten, um die hohen Potenzen zu vermeiden
    return df
steps = 500
t = np.linspace(0, 4, steps)
y_0 = [1,0]
l = odeint(fun, y_0, t) 
# ML: mit full_output = True kann man auf die Anzahl der Zeitschritte und den Integrator zugreifen:
# ML: mit info['nst'] kann man die Anzahl der Zeitschritte auslesen und mit info['mused'] auf den Integrator zugreifen. info['nqu'] gibt die Ordnung des Interators
t_4 = (abs(t-4)).argmin()

print("Bei t = %.0f ergibt sich eine Position von x = %.3f und eine Geschwindigkeit von x' = v = %.3f" %( t[t_4], l[t_4,0], l[t_4,1]))
print("Bei t = %.0f ergibt sich eine Position von x = %.3f und eine Geschwindigkeit von x' = v = %.3f" %( t[-1], l[-1,0], l[-1,1])) # ML: geht auch
print("Ich habe odeint von scipy.integrate benutzt es benutzt lsoda von der FORTRAN library odepack.  \
      \n Dabei habe ich %i Zeitschritte benutzt."%steps)
# ML: odeint benutzt hier ein Adams Verfahren bis zu 8. Ordnung, d.h. der Zeitschritt wird weiter angepaßt. 
plt.plot(t, l)
plt.show()
