import numpy as np
import matplotlib.pyplot as plt
###############
#      a)     #
###############
if 0:
    N = int(1e6)
    x = np.linspace(0,10) 
    y = lambda x: x*np.exp(-x)
    h = max(y(x))
    x_max = 100
    x_rand = np.random.uniform(0,x_max,N)
    y_rand = np.random.uniform(0,h,N)
    hits = 0
    
    for n in range(N):
        if y_rand[n] <= y(x_rand[n]):
            hits += 1
    print(h*x_max*hits/N)
    
    
###############
#      b)     #
###############
if 1:
    N = int(1e6)
    x = np.linspace(0,10) 
    y = lambda x: np.sin(np.pi*x)*np.exp(-x)
    h = max(y(x))
    x_max = 8
    x_rand = np.random.uniform(0,x_max,N)
    y_rand = np.random.uniform(0,h,N)
    hits = 0
    
    for n in range(N):
        if y_rand[n] <= y(x_rand[n]):
            hits += 1
    print(h*x_max*hits/N)
    print(np.pi/(1+np.pi**2))
    plt.xkcd()
    plt.plot(x,y(x))