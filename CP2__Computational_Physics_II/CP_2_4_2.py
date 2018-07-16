import numpy as np
import matplotlib.pyplot as plt

α, β = .13, .16
N = 10
zustand = [1]
#if 0:
#    for t in range(N):
#        Zufall = np.random.rand()
#        if zustand[-1] == 1:
#            if Zufall < α:
#                zustand.append(1)
#            else: 
#                zustand.append(2)
#        else:
#            if Zufall < β:
#                zustand.append(2)
#            else: 
#                zustand.append(1)
#    plt.hist(zustand)
#    plt.show()

p1, p2 = np.ones(N), np.zeros(N)

for i in range(N-1):
    p1[i+1] = (1-α) * p1[i] + β*p2[i]
    p2[i+1] = α*p1[i] + (1-β) * p2[i]
    
    
plt.plot(p1)
plt.plot(p2)
plt.show()
