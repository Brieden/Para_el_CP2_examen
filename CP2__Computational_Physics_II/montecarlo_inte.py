import numpy as np
import matplotlib.pyplot as plt

N = int(1e6)
f = lambda x: x**2/( 1 + x**2) 
x_min, x_max = 0,1

y_max = max(f(np.linspace(x_min,x_max,int(1e5))))
y_min = min(f(np.linspace(x_min,x_max,int(1e5))))
x = np.random.uniform(x_min,x_max,N)
y = np.random.uniform(y_min,y_max,N)

hits = 0
for n in range(N):
    if abs(y[n]) <= abs(f(x[n])) and np.sign(y[n]) == np.sign(f(x[n])):
        hits += np.sign(y[n])
   
print("Fläche = ",(x_max - x_min)*(y_max - y_min)*hits/N)

if 0:
    plt.xkcd(), plt.ylabel("f(x)"), plt.xlabel("x")
    x = np.linspace(x_min,x_max, 1e3) 
    plt.plot(x,f(x))

