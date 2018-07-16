import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from numba import jit

class RankomWalkerType:

    def __init__(self, _steps, _num, *_arg):
        self.steps_ = _steps
        self.num_ = _num
        self.arg_ = _arg
        self.data_ = np.empty(shape=(self.steps_, self.num_))
        self.l_ = np.empty(shape=self.num_)
        self.fitting_parameters_ = np.empty(shape=(self.steps_, 2))

    @jit
    def initialize_(self):
        self.data_[0, :] = np.zeros(shape=self.num_)

    @jit
    def do_step_(self, _i):
        self.l_ = np.round(self.arg_[0]*np.random.uniform(size=self.num_)+self.arg_[1])
        #def option(_r):
        #    if _r < 0.5-self.arg_[0]:
        #        result=-1
        #    else
        #        result=1
        #options = np.vectorize(option)
        #self.l_ *= options(np.random.uniform(size=self.num_))
        self.data_[_i] = self.data_[_i-1]+self.l_

    @jit
    def fit_curve_(self, _i):
        self.fitting_parameters_[_i, :] = norm.fit_loc_scale(self.data_[_i, :])

    @jit
    def evaluate(self):
        self.initialize_()
        self.fit_curve_(0)
        for i in range(1, self.steps_):
            self.do_step_(i)
            self.fit_curve_(i)

    def plotFigureOfTheStep(self, _i, _file_name):
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        fig, ax = plt.subplots()
        n, bins, patches = ax.hist(self.data_[_i, :], bins=np.linspace(-200+0, 200+0, 401), density=True, histtype='bar')
        x = np.linspace(bins[0], bins[-1], 1000)
        y = norm.pdf(x, *self.fitting_parameters_[_i])
        ax.plot(x, y, label=r"\(\mu={0:.2f},\quad\sigma={1:.2f}\)".format(*self.fitting_parameters_[_i]))
        ax.legend()
        ax.grid()
        ax.set_title(r"The PDF after {0:d} steps".format(_i))
        ax.set_xlabel(r"location")
        ax.set_ylabel(r"probability density")
        fig.tight_layout()
        fig.savefig(_file_name)

def main():
    a = 2
    b = -1
    steps = 1001
    num = 1000000

    solver = RankomWalkerType(steps, num, a, b)
    solver.evaluate()
    solver.plotFigureOfTheStep(steps-1, "figure_0.pdf")

if __name__ == "__main__":
    main()
        
