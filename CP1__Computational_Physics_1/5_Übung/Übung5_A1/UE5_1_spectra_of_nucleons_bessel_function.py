import numpy as np
import scipy
import matplotlib.pyplot as plt

                      #(Ordnung der Besselfunktion, Anzahl Nullstellen)
#scipy.special.jn_zeros() # Bestimmt Nullstellen für besselfunktion der n-ten Ordnung
#scipy.special.spherical_jn()

p_end=12
p_step=0.01
dat_p=np.arange(0,p_end+p_step,p_step)

acc=0.00000001#Genauigkeit NS


#print(dat_p)

l= 3
#ns=[]
#werte=[[],[]]
for l_ in range(l+1): # erzeuge l+1 Plots
    werte =np.array([scipy.special.spherical_jn(l_,p) for p in dat_p])
    plt.plot(dat_p,werte,label='l=%i'%l_)
    
    #for j in werte:
    #    if j<acc and j>0:
    #        ns.append(j)
            
    
#print(ns)

plt.ylabel('J_l(x)')
plt.xlabel('p')
plt.title('Spherical Bessel functions')
plt.xlim(0,p_end)
plt.legend(loc='upper right') 
plt.grid(True)

plt.show() # zeige alle Plots an

# =============================================================================
# pns=1
# 
# while(pns>acc): 
#     
#     pnsp=pns-(scipy.special.spherical_jn(0,pns)/scipy.special.spherical_jn(0,pns,derivative=True))
#     
#     pns=pnsp
#     
# print(pns)
# =============================================================================

