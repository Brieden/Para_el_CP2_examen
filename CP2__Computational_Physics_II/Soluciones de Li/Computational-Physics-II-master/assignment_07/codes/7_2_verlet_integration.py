import numpy as np
import matplotlib.pyplot as plt
from time import time

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

class VerletIntegration:

    def __init__(self, _num, _dim, _delta_t):
        self.data_ = np.empty((_num, _dim))
        self.t_ = np.empty((_num, 1))
        self.num_ = _num
        self.dim_ = _dim
        self.delta_t_ = _delta_t
        self.data_[0,:] = np.zeros((_dim))
        self.data_[0,0] = np.random.uniform(0, 2)
        #self.data_[0,0] = 1.0
        self.t_[0] = 0.0
        self.data_[1,:] = np.copy(self.data_[0,:])
        self.data_[1,1] += np.sqrt((2-self.data_[0,0])/self.data_[0,0])*self.delta_t_
        self.t_[1] = self.delta_t_
    
    def a_(self, _x):
        result = np.empty(self.dim_)
        result[0] = -_x[0]/(np.linalg.norm(_x)**3)
        result[1] = -_x[1]/(np.linalg.norm(_x)**3)
        return result

    def do_step_(self, _i):
        self.data_[_i] = 2.0*self.data_[_i-1]-self.data_[_i-2]+self.a_(self.data_[_i-1])*np.square(self.delta_t_)
        self.t_[_i] = self.t_[_i-1]+self.delta_t_

    def evaluate(self):
        for i in range(2, self.num_):
            self.do_step_(i)

    def plotFigure(self):
        plt.figure()
        plt.plot(self.t_, self.data_[:,0])
        plt.grid()
        plt.xlabel(r"\(t\)")
        plt.ylabel(r"\(x\)")
        plt.savefig("figure_2_1.pdf")
        plt.close()
        plt.figure()
        plt.plot(self.t_, self.data_[:,1])
        plt.grid()
        plt.xlabel(r"\(t\)")
        plt.ylabel(r"\(y\)")
        plt.savefig("figure_2_2.pdf")
        plt.close()
        plt.figure()
        plt.plot(self.data_[:,0], self.data_[:,1])
        plt.grid()
        plt.xlabel(r"\(x\)")
        plt.ylabel(r"\(y\)")
        plt.savefig("figure_2_3.pdf")
        plt.close()

def main():
    np.random.seed(int(time()))
    s = VerletIntegration(4001, 2, np.pi/250)
    print(s.data_[0,:])
    s.evaluate()
    s.plotFigure()
    return 0
    
if __name__ == "__main__":
    main()
