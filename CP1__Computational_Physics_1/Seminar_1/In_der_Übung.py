import numpy as np
import matplotlib.pyplot as plt

def Reihe(Schritte, x_0, r):
#    r = np.linspace(0,4, 10)
    x = np.full(Schritte, np.nan)
    x[0] = x_0

    for n in np.arange(Schritte)[:-1]:
        x[n + 1] = r*x[n]*(1-x[n])
    return x

if __name__== "__main__":
    print(Reihe(10, 0.5, 2.1))

    #plt.plot(Reihe(300, 0.3, 2.9))
    plt.show()
