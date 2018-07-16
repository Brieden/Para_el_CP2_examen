import scipy  
import numpy as np
import math 
import matplotlib.pyplot as plt
import matplotlib as mpl # für Farben
import time
from scipy.linalg import solve

#                         LGS der Form: Ax=b
#     (Exponent,Basis)
def vektor_b(k,N): # gibt die einzelnen akkumulierten Teilsummen aus, für LGS als Vektor b
    n=1
    erg_sigma=[[0 for el in range(1) ]for zeilen in range(0,N,1)]
    sigma=0
    while n<=N:
        summand = n**k
        sigma=sigma+summand
        erg_sigma[n-1][0]=sigma
        n=n+1
    return erg_sigma    # Elemente von der Liste erg_sigma über erg_sigma[0,1,2...] ansprechen


#print(sum(2,3))

def matrix_A(k,N):
    
    mat_a=[[0 for zeilen in range(0,N,1)]for spalten in range(0,k+1,1)]
    
    for n in range(1,N+1,1):
        for l in range(1,k+2,1):
            pot= n**l
            mat_a[l-1][n-1]=pot
            
    return mat_a       
  

# Für jedes k eine zeile von koeffizienten


k=2
N=k+1

print(vektor_b(k,N))

print(matrix_A(k,N))

print(solve(matrix_A(k,N),vektor_b(k,N)))
  
    
            
            
            
            
        

