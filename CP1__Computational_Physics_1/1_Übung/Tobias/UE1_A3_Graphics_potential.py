#import scipy  
import numpy as np
import math 
import matplotlib.pyplot as plt

x = np.linspace(-3,3,60) #array mit datenpunkten

v = x*x*math.e**(-x) # Potential, übergabe der datenpunkte lässt v auch zu array werden

vx = (2*x-x**2)*math.e**(-x) # erste Ableitung, Kraft

vxx = (x**2-4*x+2)*math.e**(-x) # zweite Ableitung

plt.plot(x,v,"x",label='potential') 
plt.plot(x,vx,"x",label='force') 
plt.plot(x,vxx,"x",label='2nd derivate') 

plt.xlabel('x')
plt.ylabel('V(x), F(x), dF(x)/dx') 
plt.legend(loc='upper right')                      # position legende
plt.title('Graphics')
plt.grid(True)           
                          # Gitterlinien
plt.show()  # stell alle bisher erwähnten datensätze dar

# Nullstellensuche der Kraft ergibt analytisch x=0 und x=2

# =============================================================================
# for z in vx:
#     print(z)
# =============================================================================
