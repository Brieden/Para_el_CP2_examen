import scipy  
import numpy as np
import math 
import matplotlib.pyplot as plt

x=1
n=0 #laufindex
end=50 #anzahl der h-schritte

#initialisieren von feldern
hl = np.zeros(end)
m1 = np.zeros(end)
m2 = np.zeros(end)
m3 = np.zeros(end)

mx = - math.sin(x) # analytische ableitung von cos(x)

while n<end:
    
    h=2**(-n)

    hl[n]=h # vektor für x-achse
    
    m1[n]=abs(((math.cos(x+h)-math.cos(x))/(h))-mx) #delta ausdruck 1
    
    m2[n]=abs(((math.cos(x)-math.cos(x-h))/(h))-mx) #delta ausdruck 3
    
    m3[n]=abs(((math.cos(x+h)-math.cos(x-h))/(2*h))-mx) #delta ausdruck 3
    
    n=n+1 # zähler laufindex

plt.loglog(hl,m1,"x",label='expression 1') 
plt.loglog(hl,m2,"x",label='expression 2')
plt.loglog(hl,m3,"x",label='expression 3')
plt.xlabel('Step size of h [log]')
plt.ylabel('deviation of approximation and analytica solution [log]') 
plt.legend(loc='lower right')                      # position legende
plt.title(('Numerical derivatives for n =',end))
plt.grid(True)                                     # Gitterlinien

plt.show()  # stell alle bisher erwähnten datensätze dar

print(hl)
#der Ausdruck 3 (grün) weist die geringsten Abweichungen (bis zu 10^-11) zur analytischen lösung auf.
#Die genauigkeit ist wegen der doppelten intervallgröße besser als in den Ausdrücken 1 und 2, 


    



    

