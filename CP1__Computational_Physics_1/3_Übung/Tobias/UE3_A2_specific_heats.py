from scipy.constants import*
import numpy as np
import math 
import matplotlib.pyplot as plt
import matplotlib as mpl # für Farben
import time

def number_rot(T,I):
    sigma = 0
    J = 0
    summand =1
    thet = ((h/math.pi)**2)/(2*I*k)
    while(summand>10**(-9)):
        summand = (2*J+1)*math.e**((-J*(J+1)*thet)/T)
        sigma = sigma + summand
        J = J+1 
    return sigma,(T/thet)

def in_energy(T):
    u_ana = 2*k*T
    return u_ana

def spec_heat(T):
    c_ana = 2*k
    return c_ana

T0 = 0 # in K
Tend = 300 # in K
schritt = 10
I_N2 = 13.9*10**(-47) # Für N2 in kg*m²

#thet = ((h/math.pi)**2)/(2*I_N2*k)

dt =np.arange(T0,Tend+schritt,schritt) # Vektor mit Temperaturwerten

zt = np.array([number_rot(T,I_N2)[0]for T in dt]) #Z(T) numerisch

zt_theta = np.array([number_rot(T,I_N2)[1]for T in dt]) #z(T) analytisch

ut = np.array([in_energy(T)for T in dt])   # Inntere Energie U analytisch

ct = np.array([spec_heat(T)for T in dt])  # Wärmekapazität konstant????

plt.plot(dt,zt,"x",label='number') 
plt.plot(dt,zt_theta,"x",label='T_thet') 
plt.plot(dt,ut,"x",label='Ut') 
plt.plot(dt,ct,"x",label='ct') 
plt.ylabel('Anzahl Zustände')
plt.xlabel('Temperatur in K')
plt.legend(loc='upper left') 

print("Temperatur   Z(T)(numerisch)    Z(T)(analytisch)")
dig =7 # Nachkommastellen

for t in dt:             # repr() erstellt String # [:dig] anzahl Ziffern
    print(repr(t).rjust(3),repr(number_rot(t,I_N2)[0])[:dig].rjust(20),repr(number_rot(t,I_N2)[1])[:dig].rjust(20))
    

