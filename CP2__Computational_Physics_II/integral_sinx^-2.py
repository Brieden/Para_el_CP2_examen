import numpy as np
import matplotlib.pyplot as plt

N = int(1e6)
x = np.linspace(-1,1, 1e5) 
y = lambda x: np.sin(x**-2)
#h = max(y(x))
#x_max = 100
#x_rand = np.random.uniform(0,x_max,N)
#y_rand = np.random.uniform(0,h,N)
#hits = 0
#
#for n in range(N):
#    if y_rand[n] <= y(x_rand[n]):
#        hits += 1
#print(h*x_max*hits/N)



plt.xkcd(), plt.ylabel("f(x)"), plt.xlabel(x), plt.title("$f(x)=sin(x^2)$")

plt.plot(x,y(x))

