import numpy as np
import matplotlib.pyplot as plt
from time import time

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

class MarkovChainType:

    def __init__(self, _alpha, _beta, _size):
        self.alpha_ = _alpha
        self.beta_ = _beta
        self.size_ = _size
        self.data_ = -0.5*np.ones(_size)
        self.step_ = .0
        self.p1_ = []
        self.p2_ = []

    def do_step_(self):
        for i in range(self.size_):
            if self.data_[i] < 0:
                if np.random.uniform() < self.alpha_:
                    self.data_[i] += 1
            else:
                if np.random.uniform() < self.beta_:
                    self.data_[i] -= 1

    def walk(self, _steps):
        while self.step_ < _steps:
            self.do_step_()
            temp, opt = np.histogram(self.data_, bins=[-1,0,1])
            self.p1_.append(temp[0]/self.size_)
            self.p2_.append(temp[1]/self.size_)
            self.step_ += 1
            del opt
            del temp

    def plotFigure(self, _file_name, _a,_b):
        plt.figure()
        plt.semilogx(np.arange(1.0, self.step_+1.0, 1.0), self.p1_, label= "State 1")
        plt.semilogx(np.arange(1.0, self.step_+1.0, 1.0), self.p2_, label= "State 2")
        plt.legend()
        plt.grid()
        plt.ylim(0.0,1.0)
        plt.title(r"$\alpha$ = {0: .2f}, $\beta$ = {1:.2f}".format(_a, _b))
        plt.xlabel(r"numbers of steps \(n\)")
        plt.ylabel(r"probability \(P\)")
        plt.tight_layout()
        plt.savefig(_file_name)
        plt.close()

def main():
    np.random.seed(int(time()))
    alpha_list = np.append(np.linspace(0.2, 0.8, 1),[0.01])
    beta_list = np.append(np.linspace(0.2, 0.8, 1),[0.01])
    a, b = np.meshgrid(alpha_list, beta_list)
    for i in range(len(alpha_list)):
        for j in range(len(beta_list)):
            s = MarkovChainType(a[i][j], b[i][j], 1000)
            s.walk(1000)
            alpha_label= int(a[i][j]*10)
            beta_label= int(b[i][j]*10)
            s.plotFigure("fig2_a_{0:d}_b_{1:d}.png".format(alpha_label,beta_label), a[i][j], b[i][j] )
            del s
    return 0

if __name__ == "__main__":
    main()

