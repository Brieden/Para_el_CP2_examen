import numpy as np
import matplotlib.pyplot as plt
from time import time
from scipy.optimize import curve_fit

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

class RandomWalks3DType:

    def __init__(self, _size):
        self.data_ = np.zeros([_size, 3])
        self.l_ = np.empty([_size, 3])
        self.steps_ = 0
        self.norm_ = np.empty(_size)

    def genNorm_(self):
        for i in range(len(self.norm_)):
            self.norm_[i] = np.linalg.norm(self.data_[i,:])
        del i

    def plotFigure(self, _file_name):
        p = lambda x,sigma : np.sqrt(2.0/np.pi)/(sigma**3)*x**2*np.exp(-(x/sigma)**2/2.0)
        plt.figure()
        ydata, bins, *opt = plt.hist(self.norm_, bins=np.linspace(0.0, 80.0, 81), density=True, histtype='bar')
        xdata = np.empty(len(ydata))
        for i in range(len(ydata)):
            xdata[i] = (bins[i]+bins[i+1])/2.0
        popt, pcov = curve_fit(p, xdata, ydata)
        x = np.linspace(0.0, 80.0, 1001)
        y = p(x, *popt)
        ydata_prime = p(xdata, *popt)
        R2 = (np.average(ydata*ydata_prime)-np.average(ydata)*np.average(ydata_prime))/(np.std(ydata)*np.std(ydata_prime))
        plt.plot(x, y, '--', label=r"\(\sigma={0:.4f}\)".format(*popt))
        plt.xlim([0.0, 80.0])
        plt.ylim([0.0, 0.036])
        plt.grid()
        plt.legend()
        plt.xlabel(r"the radius \(R\)")
        plt.ylabel(r"probability density function")
        plt.text(60.0, 0.03, r"\(R^2={0:.4f}\)".format(R2))
        plt.tight_layout()
        plt.savefig(_file_name)
        plt.close()

class SphericalRandomWalksType(RandomWalks3DType):

    def __init__(self, _size):
        RandomWalks3DType.__init__(self, _size)

    def do_step_(self):
        self.l_[:,2] = -np.random.uniform(-1.0, 1.0, len(self.norm_))
        temp1 = np.random.uniform(0.0, 2.0*np.pi, len(self.norm_))
        temp2 = np.sqrt(1-self.l_[:,2]**2)
        self.l_[:,0] = temp2*np.cos(temp1)
        self.l_[:,1] = temp2*np.sin(temp1)
        self.data_ += self.l_
        self.steps_ += 1
        del temp1
        del temp2

    def walk(self, _steps):
        while self.steps_ < _steps:
            self.do_step_()
            if self.steps_ % int(_steps/100) == 0:
                print("SphericalRandomWalks: process has been finished for {0:d}%".format(int(self.steps_/_steps*100)))
        self.genNorm_()

class CubicRandomWalksType(RandomWalks3DType):

    def __init__(self, _size):
        RandomWalks3DType.__init__(self, _size)

    def do_step_(self):
        i = 0
        while i < len(self.norm_):
            self.l_[i,:] = np.random.uniform(-1.0, 1.0, 3)
            temp = np.linalg.norm(self.l_[i,:])
            if temp <= 1.0:
                self.l_[i,:] /= temp
                i += 1
        self.data_ += self.l_
        self.steps_ += 1
        del i
        del temp

    def walk(self, _steps):
        while self.steps_ < _steps:
            self.do_step_()
            if self.steps_ % int(_steps/100) == 0:
                print("CubicRandomWalks: process has been finished for {0:d}%".format(int(self.steps_/_steps*100)))
        self.genNorm_()

class GaussianRandomWalksType(RandomWalks3DType):

    def __init__(self, _size):
        RandomWalks3DType.__init__(self, _size)

    def do_step_(self):
        self.l_ = np.random.normal(0.0, 1.0, (len(self.norm_), 3))
        for i in range(len(self.norm_)):
            self.l_[i,:] /= np.linalg.norm(self.l_[i,:])
        self.data_ += self.l_
        self.steps_ += 1
        del i

    def walk(self, _steps):
        while self.steps_ < _steps:
            self.do_step_()
            if self.steps_ % int(_steps/100) == 0:
                print("GaussianRandomWalks: process has been finished for {0:d}%".format(int(self.steps_/_steps*100)))
        self.genNorm_()

def main():
    np.random.seed(int(time()))
    size = 100000
    steps = 1000
    walkers = []
    walkers.append(SphericalRandomWalksType(size))
    walkers.append(CubicRandomWalksType(size))
    walkers.append(GaussianRandomWalksType(size))
    for i in range(3):
        walkers[i].walk(steps)
        walkers[i].plotFigure("figure_2_{0:d}.pdf".format(i))

if __name__ == "__main__":
    main()
