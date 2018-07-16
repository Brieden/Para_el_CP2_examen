import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class MoleculesType:

    def __init__(self, _steps, _n , _d, _delta_t, _damping):
        self.data_ = np.empty(shape=(_steps, _n, _d))
        #self.data_[0,:,:] = np.load("ic_01.npy")
        self.data_[0, :, :] = np.random.normal(size=(_n, _d))
        self.steps_ = _steps
        self.n_ = _n
        self.d_ = _d
        self.delta_t_ = _delta_t
        self.damping_ = _damping
        self.total_energy_ = np.empty(_steps)
        self.kinetic_energy_ = np.zeros(_steps)
        self.potential_energy_ = np.zeros(_steps)
        self.interacting_energy_ = np.zeros(_steps)

    @staticmethod
    def K_(_r1, _r2, _delta_t, _damping):
        return (1-_damping)**2*0.5*(_r2-_r1).dot(_r2-_r1)/(_delta_t*_delta_t)

    @staticmethod
    def V_int_(_r1, _r2):
        return 1/(_r2-_r1).dot(_r2-_r1)

    @staticmethod
    def V_ext_(_r):
        return 0.5*_r.dot(_r)

    @staticmethod
    def F_int_(_r1, _r2):
        return 2.0*(_r1-_r2)/(np.linalg.norm(_r2-_r1)**4)

    @staticmethod
    def F_ext_(_r):
        return -_r

    def do_step_(self, _step):
        for i in range(self.n_):
            F = self.F_ext_(self.data_[_step-1, i, :])
            for j in range(self.n_):
                if j != i:
                    F += self.F_int_(self.data_[_step-1, i, :], self.data_[_step-1, j, :])
            self.data_[_step, i, :] = (2-self.damping_)*self.data_[_step-1, i, :]-(1-self.damping_)*self.data_[_step-2, i, :]+F*self.delta_t_*self.delta_t_

    def calKineticEnergy_(self, _step):
        for i in range(self.n_):
            self.kinetic_energy_[_step] += self.K_(self.data_[_step-1, i, :], self.data_[_step, i, :], self.delta_t_, self.damping_)

    def calPotentialEnergy_(self, _step):
        for i in range(self.n_):
            self.potential_energy_[_step] += self.V_ext_(self.data_[_step, i, :])

    def calInteractingEnergy_(self, _step):
        for i in range(self.n_): 
            for j in range(i+1, self.n_):
                self.interacting_energy_[_step] += self.V_int_(self.data_[_step, i, :], self.data_[_step, j, :])

    def calTotalEnergy_(self, _step):
        self.total_energy_[_step] = self.kinetic_energy_[_step] + self.potential_energy_[_step] + self.interacting_energy_[_step]

    def evaluate(self):
        self.data_[0, :, :] = np.random.normal(size=(self.n_, self.d_))
        self.calPotentialEnergy_(0)
        self.calInteractingEnergy_(0)
        self.calTotalEnergy_(0)

        self.data_[1, :, :] = np.copy(self.data_[0, :, :])
        for i in range(self.n_):
            F = self.F_ext_(self.data_[0, i, :])
            for j in range(self.n_):
                if j != i:
                    F += self.F_int_(self.data_[0, i, :], self.data_[0, j, :])
            self.data_[1, i, :] += F*self.delta_t_*self.delta_t_
        self.calKineticEnergy_(1)
        self.calPotentialEnergy_(1)
        self.calInteractingEnergy_(1)
        self.calTotalEnergy_(1)

        for i in range(2, self.steps_):
            self.do_step_(i)
            self.calKineticEnergy_(i)
            self.calPotentialEnergy_(i)
            self.calInteractingEnergy_(i)
            self.calTotalEnergy_(i)

    def saveAnimation(self, _file_name):
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=15, bitrate=1800)
        fig, ax = plt.subplots()
        samples = plt.scatter(self.data_[0, :, 0], self.data_[0, :, 1] , animated=True)
        def init():
            ax.set_xlim((-8, 8))
            ax.set_ylim((-8, 8))
            ax.set_xlabel(r"\(x\)")
            ax.set_ylabel(r"\(y\)")
            fig.set_tight_layout(True)
            return samples,
        def update(_step):
            samples.set_offsets(self.data_[_step, :, :])
            return samples,
        ani = animation.FuncAnimation(fig, update, frames=range(self.steps_), interval=0, init_func=init, blit=True)
        #ani.save(_file_name, writer=writer)
        plt.show()

    def plotFigure(self, _file_name):
        t = self.delta_t_*np.arange(0, self.steps_)
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        plt.figure()
        plt.plot(t, self.total_energy_, label="total")
        plt.plot(t, self.kinetic_energy_, label="kinetic")
        plt.plot(t, self.potential_energy_, label="potential")
        plt.plot(t, self.interacting_energy_, label="interacting")
        plt.xlabel("time units")
        plt.ylabel("energy")
        plt.grid()
        plt.legend()
        plt.tight_layout()
        plt.savefig(_file_name)
        plt.close()

def main():
    HouchenLi = MoleculesType(int(120/0.01+1), 20, 2, 0.01, 0.001)
    HouchenLi.evaluate()
    HouchenLi.plotFigure("figure_1.pdf")
    HouchenLi.saveAnimation("animation.mp4")
    return 0

if __name__ == "__main__":
    main()
