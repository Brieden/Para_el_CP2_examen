import numpy as np
from time import time
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

class BrownianMotorType:

    def __init__(self, _x0, _t0, _a, _b, _omega, _D, _h, _size):
        self.x_ = np.empty(_size)
        self.x_[0] = _x0
        self.t_ = np.empty(_size)
        self.t_[0] = _t0
        self.a_ = _a
        self.b_ = _b
        self.omega_ = _omega
        self.D_ = _D
        self.h_ = _h
        self.size_ = _size

    def evolution(self):
        for i in range(1, self.size_):
            self.t_[i] = self.t_[i-1] + self.h_
            self.x_[i] = self.x_[i-1] + (1-np.cos(2.0*self.omega_*self.t_[i-1]))*(self.a_*np.sin(self.x_[i-1])+2.0*self.b_*np.sin(2.0*self.x_[i-1]))*self.h_ + np.random.normal(0.0, np.sqrt(self.D_*self.h_))*self.h_
        del i

    def plotFigure(self, _file_name):
        plt.figure()
        plt.plot(self.t_, self.x_)
        plt.grid()
        plt.xlabel(r"\(t\)")
        plt.ylabel(r"\(x\)")
        plt.tight_layout()
        plt.savefig(_file_name)
        plt.close()

def main():
    np.random.seed(int(time()))
    bacteria = BrownianMotorType(0.0, 0.0, 1.0, 2.0, 10, 10000.0, 0.1, 10000)
    bacteria.evolution()
    bacteria.plotFigure("figure_3_0.pdf")
    return 0
if __name__ == "__main__":
    main()
    
