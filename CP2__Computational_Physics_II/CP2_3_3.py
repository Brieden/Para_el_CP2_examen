import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


V = lambda x, t:(1 - np.cos(2*ω*t))*(a*np.cos(x) + b*np.cos(2*x))

V_punkt = lambda x,t:(
        (-1 + np.cos(2*t*ω))*(a*np.sin(x) + 2*b*np.sin(2*x))+
        2*ω*(a*np.cos(x) + b*np.cos(2*x))*np.sin(2*t*ω))

tBegin=0
tEnd=2*np.pi*2
dt= (tEnd-tBegin)/300
#dt= 
x_0 = 0
a,b,sigma,ω = .1,1,.1,1

t = np.arange(tBegin, tEnd, dt)
N = t.size
sqrtdt = np.sqrt(dt)
x = np.zeros(N)
x[0] = x_0

for i in range(1,N):
    x[i] = (x[i-1] 
            + dt*V_punkt(x[i-1],t[i]) 
            + sigma*np.random.normal(loc=0.0,scale=sqrtdt))

plt.plot(t,x)
plt.show()