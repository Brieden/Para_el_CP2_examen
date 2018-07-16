import numpy as np
import matplotlib.pyplot as plt

class DirectedPercolationType:

    def __init__(self, _size, _r, _p):
        self.size_ = _size
        self.lattice_ = np.empty(shape=(self.size_, self.size_))
        self.lattice_[0] = np.ones(self.size_)
        self.transit_probabilities_ = np.empty(self.size_)
        self.transit_ratios = np.empty(self.size_)
        self.r = _r
        self.p = _p
        self.changeStates_ = np.vectorize(DirectedPercolationType.changeAState_)

    @staticmethod
    def changeAState_(_random, _q):
        if _random < _q:
            return 0
        else:
            return 1

    def calTransitRatios_(self, _i):
        self.transit_ratios[_i] = np.average(self.lattice_[_i, :])

    def calTransitProbabilities_(self, _i):
        self.transit_probabilities_[0] = (1-self.r*self.lattice_[_i-1, self.size_-1])*(1-self.p*self.lattice_[_i-1, 0])*(1-self.r*self.lattice_[_i-1, 1])
        for j in range(1, self.size_-1):
            self.transit_probabilities_[j] = (1-self.r*self.lattice_[_i-1, j-1])*(1-self.p*self.lattice_[_i-1, j])*(1-self.r*self.lattice_[_i-1, j+1])
        self.transit_probabilities_[self.size_-1] = (1-self.r*self.lattice_[_i-1, self.size_-2])*(1-self.p*self.lattice_[_i-1, self.size_-1])*(1-self.r*self.lattice_[_i-1, 0])

    def do_step_(self, _i):
        self.lattice_[_i,:] = self.changeStates_(np.random.uniform(size=self.size_), self.transit_probabilities_)*self.lattice_[_i-1,:]

    def evaluate(self):
        self.calTransitRatios_(0)
        for i in range(1, self.size_):
            self.calTransitProbabilities_(i)
            self.do_step_(i)
            self.calTransitRatios_(i)

    def plotFigure(self, _file_name):
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        plt.figure()
        plt.plot(np.arange(self.size_), self.transit_ratios, '.')
        plt.title(r"The Evolution of Transit Ratios for \(r={0:4}\) and \(p={1:4}\)".format(self.r, self.p))
        plt.xlabel(r"Transit Ratio \(R\)")
        plt.ylabel(r"Time")
        plt.grid()
        plt.tight_layout()
        plt.savefig(_file_name)
        plt.close()

def main():
    size = 100
    r = np.linspace(0.1, 1.0, 9)
    p = 0.7
    transit_ratios = np.empty(shape=(9, 100))
    t = np.arange(100)
    DPSolver = DirectedPercolationType(size, 0.1, p)
    colors = plt.cm.jet(np.linspace(0.0, 1.0, 9))
    for i in range(9):
        DPSolver.r = r[i]
        DPSolver.evaluate()
        transit_ratios[i, :] = DPSolver.transit_ratios
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.figure()
    for i in range(9):
        plt.plot(t, transit_ratios[i, :], color=colors[i])
    plt.title(r"The Evolution of Transit Ratios with \(p=0.7\)")
    plt.xlabel(r"\(t\)")
    plt.ylabel(r"Transit Ratio")
    plt.grid()
    #plt.colorbar()
    plt.tight_layout()
    plt.savefig("figure_2.pdf")
    plt.close()
    return 0

if __name__ == "__main__":
    main()

