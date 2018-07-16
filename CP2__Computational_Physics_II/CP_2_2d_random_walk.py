import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#plt.style.use('bmh')
#plt.xkcd()
plt.rcParams['figure.figsize'] = (3.0, 5.0)
plt.rcParams['font.size'] = 16
#np.random.seed(1)
N  = 100
starts = 4000
if 0:
    endpunkte = np.zeros((starts,2))
    for r in range(starts):
        p_l, p_r, p_u, p_d = 2/8, 2/8, 2/8, 2/8
        if sum([p_l,p_r,p_u,p_d])!=1: print("nop")
        rand = np.random.rand(N)
        steps = np.zeros((N+1,2))
        for t in range(N):
            steps[t+1] = steps[t]    
            if 0 < rand[t] < p_l:
                steps[t+1,0] = steps[t,0] - 1
            elif p_l < rand[t] < p_l+p_r:
                steps[t+1,0] = steps[t,0] + 1
            elif p_l+p_r < rand[t] < p_l+p_r+p_u:
                steps[t+1,1] = steps[t,1] + 1
            elif p_l+p_r+p_u < rand[t] < p_l+p_r+p_u+p_d:
                steps[t+1,1] = steps[t,1] - 1
            else:
                print("noooo")
        endpunkte[r] = steps[-1]
    #print(steps)
    liste =[]
    for t in range(len(endpunkte)):
        liste.append(endpunkte[t,0]**2+endpunkte[t,1]**2)
#plt.hist(liste, bins=100)

histo , bins= np.histogram(liste, normed=True)
d_bin = bins[1]- bins[0]

x = np.linspace(min(bins), max(bins),200)
#x = np.linspace(-10,10,200)
funktion = lambda x, a, mu, sigma: a/(2*np.pi*sigma**2)*np.exp(-.5*(x-mu)**2/sigma**2)
#plt.plot(x, funktion(x,1,1))
p = [200000,0,120000]
popt, pcov = curve_fit(funktion, bins[:-1]+d_bin, histo, p0=p)
plt.ylabel("Probabilidad ρ")
plt.xlabel("camino retrocedido [1e6]")
plt.plot((bins[:-1]+d_bin)/1e6, histo, label="random walk")
plt.plot(x/1e6, funktion(x, *popt), label="fitted Gauß")
plt.legend(loc=4)
print(popt)















