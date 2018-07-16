import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt

class DerivativesType:

    def __init__(self, _x, _dt, _order=1):
        self.x = _x
        self.dt = _dt
        self.order_ = _order
        self.f_ = np.empty_like(self.x)
        self.s_ = np.empty_like(self.x, dtype=np.complex64)
        self.derivatives = np.empty_like(self.x, dtype=np.float64)

    def do_fft_(self):
        self.f_ = fftpack.fftfreq(len(self.x), self.dt)
        self.s_ = fftpack.fft(self.x)

    def multiplyFactors_(self):
        self.s_ *= np.power(self.f_, self.order_)*1J

    def do_ifft_(self):
        self.derivatives = fftpack.ifft(self.s_)

    def evaluate(self):
        self.do_fft_()
        self.multiplyFactors_()
        self.do_ifft_()

def main():
    t = np.linspace(-0.5, 0.5, 10001)
    y = np.cos(2.0*np.pi*t)
    sol = DerivativesType(y, t[1]-t[0])
    sol.evaluate()
    der_y = sol.derivatives
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    fig, ax = plt.subplots()
    ax.plot(t, y, label=r"\(y=\sin\left(t\right)\)")
    ax.plot(t, np.real(der_y), label=r"\(y'=\cos\left(t\right)\)")
    #ax.set_title()
    ax.set_xlabel(r"\(t\)")
    ax.set_ylabel(r"\(y\)")
    ax.legend()
    ax.grid()
    fig.tight_layout()
    fig.savefig("figure_0.pdf")
    return 0

if __name__ == "__main__":
    main()