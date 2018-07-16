import numpy as np
import scipy.integrate as integrate

def main():
    f = lambda y,k : np.power(y, k)*np.exp(-y*y/2.0)/np.sqrt(2.0*np.pi)
    c = np.empty(5)
    c_err = np.empty_like(c)
    for i in range(5):
        c[i], c_err[i] = integrate.quad(f, -np.inf, np.inf, args=(2*(i+1),))
    print(c)
    print(c_err)
    return 0

if __name__ == "__main__":
    main()
