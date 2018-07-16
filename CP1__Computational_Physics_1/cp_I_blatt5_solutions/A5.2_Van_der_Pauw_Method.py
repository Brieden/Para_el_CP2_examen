import matplotlib.pyplot as plt
import scipy as sci
import numpy as np
from scipy import exp


def func(x,r):
    return  exp(-x) + exp(-x*r) - 1
   
# bisection algorithm:
def bisection(f,xa,xb,arg):
  n = 0
  low = f(xa,arg)
  high = f(xb,arg)
  if ((low*high) > 0):
    print ("Apparently no sign change")
    return 0
  else:
    while (n < 52):
      n += 1
      xTrial = (xa+xb)/2.
      fTrial = f(xTrial,arg)
      if (fTrial*low < 0):
        high = fTrial
        xb = xTrial
      else:
        low = fTrial
        xa = xTrial
    return [xa,xb]


rvalues = sci.linspace(0.01, 10, 1000)
x_r = []  #store values for x(rho)
y_r = []  #store values for x(1/rho)

# for each r carry out a bisection for x(r) and x(1/r). 
for r in rvalues:
  # we can use same the initial interval for different r in the bisection because
  # of the type of function. You can plot it for different r to see that. 
  # It depends on the minimal and maximal r in the chosen range.
  [xa,xb] = bisection(func,0.0001,5,r)         
  x_r.append(xa)
  
  [ya,yb] = bisection(func,0.0001,5,1/r)         
  y_r.append(ya)
  

fig = plt.figure()
plt.plot(rvalues,x_r-y_r/rvalues, color='black',linewidth=2,label=r'$x(\rho)-x(1/\rho)/\rho$')
plt.plot(rvalues,rvalues*x_r-y_r, color='red',linewidth=2,label=r'$\rho x(\rho)-x(1/\rho)$')
plt.xlabel(r'$\rho$',fontsize=20)
plt.ylabel(r'$f(x,\rho)$',fontsize=20)
plt.xlim(0,10)
plt.legend(fontsize=20)
  
fig = plt.figure()
plt.plot(rvalues,x_r, color='black',linewidth=4,label=r'$x(\rho)$')
plt.plot(rvalues,y_r/rvalues, color='red',linewidth=2,label=r'$x(1/\rho)/\rho$ from separate bisection')
plt.plot(1/rvalues,x_r*rvalues, color='blue',linewidth=0.5,label=r'$x(1/\rho)/\rho$ from setting $\rho \to 1/\rho$')
plt.xlabel(r'$\rho$',fontsize=20)
plt.ylabel(r'$x(\rho), \ x(1/\rho)/\rho$',fontsize=20)
plt.xlim(0,10)
plt.ylim(0,4)
plt.legend(fontsize=20)


plt.show()


