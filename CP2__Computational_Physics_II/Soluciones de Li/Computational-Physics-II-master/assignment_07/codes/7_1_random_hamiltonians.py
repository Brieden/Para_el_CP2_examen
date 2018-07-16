import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

class RandomHamiltoniansType:

    def __init__(self, _n):
        self.data_ = np.random.normal(size=(_n, _n))
        self.data_ += np.transpose(self.data_)
        self.data_ /= np.sqrt(8.0)
        l = np.linalg.eigvals(self.data_)
        index = np.where(l<1.0)[0][0]
        self.n_ = _n
        self.x_ = l[index:]/np.sqrt(self.n_)
        self.z_ = np.empty(self.n_-index)
        self.s_ = np.empty(self.n_-1-index)

    @staticmethod
    def I_(_x):
        phi = np.arcsin(_x)
        return phi/np.pi+0.5+1/(2.0*np.pi)*np.sin(2.0*phi)

    def calZ(self):
        for i in range(len(self.z_)):
            self.z_[i] = self.n_*self.I_(self.x_[i])

    def calS(self):
        for i in range(len(self.s_)):
            self.s_[i] = self.z_[i+1]-self.z_[i]

    def plotFigure(self, _file_name):
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        plt.figure()
        plt.hist(self.s_, bins=np.arange(0.0, 5.1, 0.1), density=True, histtype='bar')
        p = lambda s : np.pi*0.5*s*np.exp(-np.pi*0.25*s*s)
        x = np.linspace(0.0, 5.0, 1001)
        plt.plot(x, p(x))
        plt.grid()
        plt.xlabel("\(s\)")
        plt.ylabel("probability density function")
        plt.savefig(_file_name)
        plt.close()

def main():
    HouchenLi = RandomHamiltoniansType(1500)
    HouchenLi.calZ()
    HouchenLi.calS()
    HouchenLi.plotFigure("figure_0.pdf")
    return 0

if __name__ == "__main__":
    main()
