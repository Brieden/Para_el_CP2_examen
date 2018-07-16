import numpy as np
from scipy import fftpack
from scipy.signal import windows
import matplotlib.pyplot as plt

class SunSpotActivtiesType:

    def __init__(self, _data_file_name, _window_func=windows.boxcar):
        data = np.genfromtxt(_data_file_name, usecols=(2, 3))
        self.window_func_ = _window_func
        self.t_ = data[:, 0]
        self.y_ = data[:, 1]
        self.num_ = len(self.t_)
        self.f_ = np.empty(shape=self.num_)
        self.I_ = np.empty(shape=self.num_)
    
    def plotTimeDominFigure(self, _file_name):
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        fig, ax = plt.subplots()
        ax.plot(self.t_, self.y_)
        ax.set_title(r"Time Domin of Sun Spots activities")
        ax.set_xlabel(r"\(t\)")
        ax.set_ylabel(r"intensity")
        ax.grid()
        fig.tight_layout()
        fig.savefig(_file_name)
        

    def plotRealPartsOfFrequencyDominFigure(self, _file_name):
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        fig, ax = plt.subplots()
        ax.plot(self.f_, np.real(self.I_))
        ax.set_title(r"Real Part of Frequency Domin")
        ax.set_xlabel(r"\(\omega\)")
        ax.set_ylabel(r"intensity")
        ax.set_xlim((-0.3, 0.3))
        ax.grid()
        fig.tight_layout()
        fig.savefig(_file_name)

    def plotImaginaryPartsOfFrequencyDominFigure(self, _file_name):
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        fig, ax = plt.subplots()
        ax.plot(self.f_, np.imag(self.I_))
        ax.set_title(r"Imaginary Part of Frequency Domin")
        ax.set_xlabel(r"\(\omega\)")
        ax.set_ylabel(r"intensity")
        ax.set_xlim((-0.3, 0.3))
        ax.grid()
        fig.tight_layout()
        fig.savefig(_file_name)

    def plotAbsoluteValuesOfFrequencyDominFigure(self, _file_name):
        plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        fig, ax = plt.subplots()
        ax.plot(self.f_, np.absolute(self.I_))
        ax.set_title(r"Absolute Values of Frequency Domin")
        ax.set_xlabel(r"\(\omega\)")
        ax.set_ylabel(r"intensity")
        ax.set_xlim((-0.3, 0.3))
        ax.grid()
        fig.tight_layout()
        fig.savefig(_file_name)

    def do_fft(self):
        w = self.window_func_(self.num_)
        self.f_ = fftpack.fftshift(fftpack.fftfreq(self.num_, d=self.t_[1]-self.t_[0]))
        self.I_ = fftpack.fftshift(fftpack.fft(w*(self.y_-np.average(self.y_))))

def main():
    sun_spots = SunSpotActivtiesType("SN_m_tot_V2.0.dat", windows.triang)
    sun_spots.do_fft()
    #sun_spots.plotTimeDominFigure("time_domin.pdf")
    sun_spots.plotRealPartsOfFrequencyDominFigure("real_parts_of_frequency_domin_triang.pdf")
    sun_spots.plotImaginaryPartsOfFrequencyDominFigure("imaginary_parts_of_frequency_domin_triang.pdf")
    sun_spots.plotAbsoluteValuesOfFrequencyDominFigure("absolute_values_of_frequency_domin_triang.pdf")
    return 0

if __name__ == "__main__":
    main()
