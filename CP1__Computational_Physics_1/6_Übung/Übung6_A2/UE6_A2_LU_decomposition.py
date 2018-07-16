import numpy as np
import scipy

#A=(a c 0 0) = L * U
#   b a c 0
#   0 b a c
#   0 0 b a

size = 10#Size of tridiagonal quare matrix mxm

A= scipy.zeros((size,size)) #Matrix mit Nullen
L= scipy.zeros((size,size))
U= scipy.zeros((size,size))

b= np.zeros(10)
b[0]=1

#Erstellen der Ausgangsmatrix A
for z in range(size):   # Zeilen
   for i in range(size): # Spalten
       if z==i:
           A[z][i]=2   # Hauptdiagonale ai
       if z==i-1:
           A[z][i]=-1  # obere Diagonale ci
       if z==i+1:
           A[z][i]=-1  # untere Diagonale bi

da = np.zeros(size)
dc = np.zeros(size)
db = np.zeros(size)

# indizes der diagonalenelemente
ai=0
bi=1
ci=1

#Speichern der relevanten diagonalen von A
for z in range(size):   # Zeilen
   for i in range(size): # Spalten
       if z==i:
           da[ai] = A[z][i]   # Hauptdiagonale ai
           ai=ai+1           
       if z==i-1:
           dc[ci] = A[z][i]  # obere Diagonale ci
           ci=ci+1
       if z==i+1:
           db[bi] = A[z][i]  # untere Diagonale bi
           bi=bi+1

# diagonalen von L und U die keine Nullen enthalten
L_u = np.zeros(size)

U_m = np.zeros(size)
U_o = np.zeros(size)


# Berechnung der Elemente der L-und U-Diagonalen
U_m[0]=da[0]

for i in range(1,size):
    L_u[i] = db[i]/U_m[i-1]
    
    U_m[i] = da[i]-L_u[i]*dc[i-1]

# indizes der diagonalenelemente
li=1
ui=0
ci=1

#Füllen der L und U Matrizen
for z in range(size):   
   for i in range(size): 
       if z==i:
           L[z][i]=1   # Hauptdiagonale      
           U[z][i]=U_m[ui]
           ui=ui+1
       if z==i-1:
           U[z][i] = dc[ci]    # obere Diagonale 
           ci=ci+1
       if z==i+1:
           L[z][i]= L_u[li]  # untere Diagonale 
           li=li+1

#Berechnung mit L U
y = scipy.zeros(size)
x = scipy.zeros(size)

for i in range(size):
    y[i] = b[i]
    for k in range(i):
        y[i] -= L[i,k]*y[k]     

for i in range(size-1,-1,-1):
    x[i] = y[i]
    for k in range(i+1,size):
        x[i] -= U[i,k]*x[k]
        
    x[i] *= 1./U[i,i]
    
print("Lösung mit L-U-Zerlegung:")
print(x)
print("\n Benutzung von Solve mit A und b:")
print(scipy.linalg.solve(A,b))

A_dec=np.dot(L,U)
print("\n Fehler bei Zerlegung, da Element A[1,1]falsch:")
print(A_dec)

print("L")
print(L)

print("\n U")
print(U)

