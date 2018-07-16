import numpy as np
import matplotlib.pyplot as plt
#from scipy.constants import Boltzmann
from matplotlib.animation import FuncAnimation
from time import time

class IsingModelsType:

    def __init__(self, _size, _steps, _temperature, _H, _J):
        self.data_ = np.empty([_steps, _size, _size])
        self.data_[0,:,:] = np.random.uniform(0.0, 1.0, (_size, _size))
        for i in range(_size):
            for j in range(_size):
                if self.data_[0,i,j] < 0.5:
                    self.data_[0,i,j] = -1
                else:
                    self.data_[0,i,j] = 1
        self.size_ = _size
        self.steps_ = _steps
        self.temperature_ = _temperature
        self.H_ = _H
        self.J_ = _J
        self.energys_ = np.empty(_steps)
        self.magnetizations_ = np.empty(_steps)

    def scanEnergys_(self):
        for k in range(self.steps_):
            for i in range(self.size_):
                for j in range(self.size_):
                    self.energys_[k] = self.H_*self.data_[k,i,j]
                    self.energys_[k] -= self.J_*self.data_[k,i,j]*self.data_[k,(i+1)%self.size_,j]
                    self.energys_[k] -= self.J_*self.data_[k,i,j]*self.data_[k,i,(j+1)%self.size_]
    
    def scanMagnetizations_(self):
        self.magnetizations_ = np.average(self.data_, axis=(1, 2))

    def genEnergyShift_(self, _k, _i, _j):
        delta_E = -2.0*self.H_*self.data_[_k,_i,_j]
        delta_E += 2.0*self.J_*self.data_[_k,_i,_j]*self.data_[_k,(_i-1)%self.size_,_j]
        delta_E += 2.0*self.J_*self.data_[_k,_i,_j]*self.data_[_k,_i,(_j-1)%self.size_]
        delta_E += 2.0*self.J_*self.data_[_k,_i,_j]*self.data_[_k,_i,(_j+1)%self.size_]
        delta_E += 2.0*self.J_*self.data_[_k,_i,_j]*self.data_[_k,(_i+1)%self.size_,_j]
        return delta_E

    @staticmethod
    def metropolis(_delta_E, _temperature):
        if (_delta_E <= 0.0) or (np.random.uniform(0, 1) < np.exp(_delta_E/(_temperature))):
            return -1
        else:
            return 1

    @staticmethod
    def glauber(_delta_E, _temperature):
        if (np.random.uniform(0, 1) < 1/(1+np.exp(_delta_E/_temperature))):
            return -1
        else:
            return 1

    def do_step_(self, _k):
        self.data_[_k,:,:] = self.data_[_k-1,:,:]
        for i in range(self.size_):
            for j in range(self.size_):
                delta_E = self.genEnergyShift_(_k, i, j)
                #self.data_[_k,i,j] *= IsingModelsType.metropolis(self.delta_E_, self.temperature_)
                self.data_[_k,i,j] *= IsingModelsType.glauber(delta_E, self.temperature_)

    def evaluate(self):
        for k in range(1, self.steps_):
            self.do_step_(k)
        self.scanEnergys_()
        self.scanMagnetizations_()

    def plotEnergyEvolution(self, _file_name):
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        plt.figure()
        plt.plot(np.arange(self.steps_), self.energys_, label="Energy Evoluton")
        plt.grid()
        plt.legend()
        plt.xlabel(r"time step \(n\)")
        #plt.xlabel("time step n")
        plt.ylabel(r"total energy \(E\)")
        #plt.ylabel("total energy E")
        plt.tight_layout()
        plt.savefig(_file_name)
        plt.close()

    def plotMagnetizationEvolution(self, _file_name):
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        plt.figure()
        plt.plot(np.arange(self.steps_), self.magnetizations_, label="Magnetization Evoluton")
        plt.grid()
        plt.legend()
        plt.xlabel(r"time step \(n\)")
        #plt.xlabel("time step n")
        plt.ylabel(r"average of magnetization \(M\)")
        #plt.ylabel("average of magnetization M")
        plt.tight_layout()
        plt.savefig(_file_name)
        plt.close()

    def plotLatticeEvolution(self):
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        latticeFig_, latticeAx_ = plt.subplots()
        latticePlot_ = plt.imshow(self.data_[0,:,:], cmap=plt.cm.gist_gray, animated=True)
        def initLattice_():
            latticeAx_.set_xlabel(r"\(x\)")
            #latticeAx_.set_xlabel("x")
            latticeAx_.set_ylabel(r"\(y\)")
            #latticeAx_.set_ylabel("y")
            return latticePlot_,
        def updateLattice_(_frame):
            latticePlot_.set_array(self.data_[_frame,:,:])
            return latticePlot_,
        ani = FuncAnimation(latticeFig_, updateLattice_, frames=range(self.steps_), init_func=initLattice_, blit=True)
        plt.show()

def main():
    size = 100
    steps = 1000
    temperature = 2.2
    H = 0.0
    J = 1.0
    np.random.seed(int(time()))
    s = IsingModelsType(size, steps, temperature, H, J)
    s.evaluate()
    s.plotEnergyEvolution("energy.pdf")
    s.plotMagnetizationEvolution("magnetization.pdf")
    s.plotLatticeEvolution()
    return 0

if __name__ == "__main__":
    main()
