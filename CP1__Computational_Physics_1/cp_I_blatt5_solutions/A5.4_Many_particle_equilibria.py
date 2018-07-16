import pylab as plt
import scipy as sci
import scipy.linalg as linalg
import numpy as np
import math

from cmath import rect
from scipy import sqrt,cos,sin

#***************fct definitions******************************#

# effective potential for n particles, each of which is located at a different vertex of a 
# regular polygon, with or without particle in the middle
# not used directly in the calculation, may be used for plotting
def Veff(r,n,pmiddle):
    coeff = 0
    for i in range(n):
       for j in range(i):
          # Note that there is no factor of 1/2, because we sum over j > i and not over all j!=i
          coeff += 1/sqrt((cos(2* math.pi/n *i)-cos(2* math.pi/n *j))**2 + (sin(2* math.pi/n *i)-sin(2* math.pi/n *j))**2)
    if pmiddle == True: 
       # for particle in the middle (i.e. at the origin) add only the repulsive part -> n/r
       V = 0.5*n*r**2 + (coeff+n)/r
    else :   
       V = 0.5*n*r**2 + coeff/r
    return V 

# first derivative of the effective potential
def dVdr(r, n, pmiddle):
    coeff = 0
    for i in range(n):
       for j in range(i):
          coeff += 1/sqrt((cos(2* math.pi/n *i)-cos(2* math.pi/n *j))**2 + (sin(2* math.pi/n *i)-sin(2* math.pi/n *j))**2)

    if pmiddle == True:
       # for particle in the middle (i.e. at the origin) add only the repulsive part -> n/r**2
       dVdr = n*r - (coeff+n)/r**2
    else :   
       dVdr = n*r - coeff/r**2
    return dVdr 

     
# second derivative of the effective potential
def d2Vdr2(r, n, pmiddle):
    coeff = 0
    for i in range(n):
       for j in range(i):
          coeff += 1/sqrt((cos(2* math.pi/n *i)-cos(2* math.pi/n *j))**2 + (sin(2* math.pi/n *i)-sin(2* math.pi/n *j))**2)

    if pmiddle == True:
       # for particle in the middle (i.e. at the origin) add only the repulsive part -> 2n/r**3
       dVdr = n + 2*(coeff+n)/r**3
    else :   
       dVdr = n + 2*coeff/r**3
    return dVdr 
    

def Newton(guess, n,pmiddle, tol =  1e-11, maxiter = 100000):
  r0 = guess
  diff = 1
  count = 0
  while (count < maxiter and diff > tol): 
    r = r0 - 1/d2Vdr2(r0,n,pmiddle) * dVdr(r0,n,pmiddle) 
    diff = abs(r-r0)
    count+=1
    r0 = r
  return r
#***************End of fct definitions******************************#

# number of particles
n = 6

# decide if there is a particle in the middle
pmiddle = False
#pmiddle = True

if pmiddle == True:
   print('\nNumber of particles in polygon formation: {0}, plus one located at the origin'.format(n)) 
else:
   print('\nNumber of particles in polygon formation: {0}.'.format(n)) 


# guess for the Newton search
r0 = 1
  
r = Newton(r0,n,pmiddle)
#print("\nNumber of Newton-iterations: {0}".format(i))

print('\nDistance of each particle from the origin: r = ',  r) 

# Get particle configuration
x = np.arange(n,dtype=complex)

for i in range(n):
   # return complex number corresponding to polar coordinates 
   x[i] = rect(r,2*math.pi*i/n) 

# include particle in the middle, if present
if pmiddle == True:
   x0 = 0+0j
   y = np.append(x,x0)
else:
   y = x

print('\nParticles in the complex plane\n')
print(y)


plt.figure()

#plot particle configurations:
plt.plot(y.real,y.imag, 'o')
plt.gca().set_aspect(1)
plt.title(r'Particle equilibrium positions',fontsize=20)
plt.xlabel(r'$Re(x_i)$',fontsize=20)
plt.ylabel(r'$Im(x_i)$',fontsize=20)
plt.xlim(-2.5,2.5)
plt.ylim(-2.5,2.5)


plt.show()
