import numpy as np
import matplotlib.pyplot as plt
from time import time

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

class BuffonNeedleType:

    def __init__(self, _size, _rho):
        self.data_ = np.empty((_size, 3))
        self.data_[:,0] = np.random.uniform(0.0, 1.0, _size)
        self.data_[:,1] = np.random.uniform(0.0, np.pi/2.0, _size)
        self.size_ = _size
        self.rho = _rho
        self.probability = 0.0

    def calProbability(self):
        self.data_[:,2] = self.data_[:,0]+self.rho*np.sin(self.data_[:,1])
        self.probability = np.average(np.floor(self.data_[:,2]))

def main():
    size = 1000000
    num = 1000
    buffon_needle = BuffonNeedleType(size, 0.0)
    rho = np.logspace(-3, 0, num)
    probability = np.empty(num)

    for i in range(num):
        buffon_needle.rho = rho[i]
        buffon_needle.calProbability()
        probability[i] = buffon_needle.probability#/rho[i]

    plt.figure()
    plt.plot(rho, probability)
    plt.grid()
    plt.xlabel(r"\(\rho\)")
    plt.ylabel(r"probability density") #over \(\rho\)")
    plt.savefig("figure_0.pdf")
    return 0

if __name__ == "__main__":
    main()

