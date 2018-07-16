import numpy as np
import matplotlib.pyplot as plt
from time import time

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

class MonteCarloExponentialIntegrationType:
    
    def __init__(self, _f, _size):
        self.f_ = _f
        self.size_ = _size
        self.data_ = np.random.
        self.result = 0.0

    def 

    def plotFigure(self, _file_name):
        x = np.logspace(3, int(np.log10(self.size_)), 1001)
        y = np.empty_like(x)
        for i in range(len(x)):
            x[i] = int(x[i])
            #y[i] = np.abs(np.average(self.data_[0:int(x[i])])-np.pi/(1.0+np.pi**2))
            y[i] = np.abs(np.average(self.data_[0:int(x[i])])-1.0)
        plt.figure()
        plt.loglog(x, y, '-')
        plt.grid()
        plt.xlabel(r"the amount \(n\) of the random numbers")
        plt.ylabel(r"the error from the exact integration")
        plt.tight_layout()
        plt.savefig(_file_name)
        plt.close()

def main():
    np.random.seed(int(time()))
    f1 = lambda x : x
    f2 = lambda x : np.sin(np.pi*x)
    a = MonteCarloExponentialIntegrationType(f1, 1000000)
    a.plotFigure("figure_1_0.pdf")
    return 0

if __name__ == "__main__":
    main()
    
