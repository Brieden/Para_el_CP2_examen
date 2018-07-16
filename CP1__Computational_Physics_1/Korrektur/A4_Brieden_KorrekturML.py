# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:10:34 2018

@author: briedens
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

def dif2_matrix(x,dx):
    dif_now = np.diag(np.ones(len(x))) * -2
    dif_pre_ones = np.ones(len(x)-1)
    dif_pre = np.diag(dif_pre_ones, k=-1)
    dif_post_ones = np.ones(len(x)-1)
    dif_post = np.diag(dif_post_ones, k=1)     
    dif  =  dif_now + dif_pre + dif_post
    dif /= dx**2
    return dif

def potential_matrix(x):
    V_matrix = np.eye(len(x))
    for i in range(len(x)):
        V_matrix[i,i] *=  V(x[i])
    return V_matrix
    
def plot():
    for i in range(N_evs):
        plt.plot(x, ev[:,i] * 10 + ew[i])  
    plt.plot(x, V(x))
    plt.ylim(-1, 15)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$V(x)$')
    plt.title("Dopplemuldenpotential")
    plt.show()
    
V = lambda x: x**4 - 2 * x**2
x = np.linspace(-2.5,2.5, 100) #ML: zu kleiner Bereich. 
dx = x[1] - x[0]
N_evs = 5

H = -dif2_matrix(x, dx) + potential_matrix(x)
ew, ev = linalg.eigh(H)

plot() # ML: Die Eigenwerte bitte auch auflisten
print("Ich habe als Methode die Diskretisierung des Raumes benutzt (Finite-Differenzen-Methoden). \
       \n Die Diskretisierung der zweiten Ableitung erfolgt mit den zentralen Differenzenquotienten der zweiten Ableitung \
       \n Die Genauigkeit dieser Methode habe ich mit dem Potential der harmonischen Oszillators verifiziert. \
       \n Dessen analytische Lösung bekannt ist.")
# ML: letzteres gibt nur eine Verfikation der Methode, es können weiterhin Fehler durch mangelnde Auflösung (dx zu groß) und zu kleine Intervalle auftreten. Was für ein Potential reicht, kann für ein anderes falsch sein. 

