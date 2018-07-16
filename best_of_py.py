import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
#import scipy as sp
import scipy.integrate as integrate
import scipy.constants as constants
from scipy.integrate import odeint
from scipy import linalg
import sympy as sym
from scipy.optimize import fmin
import time
%matplotlib inline
plt.style.use('bmh')
plt.rcParams['figure.figsize'] = (15.0, 6.0)
plt.rcParams['font.size'] = 16
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

for i in range(6):
    print("Starte mit Aufgabe %i nach spätestens %i Minuten!"% (i+1, 120/6*i))
    
"""
# schönes Histogramm
rand = np.random.rand(int(1e7))
plt.hist(rand,density=True,histtype='step',bins=50)

# Ableitung + Nullstelle mit x-Array
V = lambda x: x**2 * np.exp(-x)
dV = lambda x: np.gradient(V(x),x)
minimuselement = (abs(0-V(x))).argmin()
x_0_Stelle = x[minimumselement]

# Ableitung symbolisch
x = sym.symbols("x")
V = x**2 * sym.exp(-x)
dV = sym.diff(V)
x_0_Stelle = fmin(lambda i: float(dV.subs({x:i})), 1)

# was sagt die Zeit
def meantime(f, x, N):
    t = 0
    for i in range(1, N):
        tstart = time.clock()
        f(x)
        tend = time.clock()
        t += (tend - tstart)
    return t/N     

# Newton-Verfahren
def newtons_method(f, df, x0, e):
    delta = dx(f, x0)
    while delta > e:
        x0 = x0 - f(x0)/df(x0)
        delta = dx(f, x0)
    print 'Root is at: ', x0
    print 'f(x) at root is: ', f(x0)
    
# 2D Skalarfeld
N_x, N_y = 500, 500
x_min, x_max = -1, 1
y_min, y_max = -1, 1
x, y = np.linspace(x_min, x_max, N_x), np.linspace(y_min, y_max, N_y)
X, Y = np.meshgrid(x, y, indexing='ij')
H_grid = H(X,Y)
plt.imshow(H_grid, origin=low, extent=(x_min, x_max, y_min, y_max))
plt.colorbar()

# find min über 2 parameter
def fmin_2d(fun, x1, x2, n_max, plotten):
    x1_x2_liste = np.zeros([n_max + 1,2])
    x1_x2_liste[0]= ([x1,x2])
    
    for n in range(n_max):
        x1 = fmin(lambda x1: fun(x1, x2), x1, disp=0)[0]
        x2 = fmin(lambda x2: fun(x1, x2), x2, disp=0)[0]
        x1_x2_liste[n+1]= ([x1,x2])
    
    if plotten:
        fig, ax1 = plt.subplots()
        ax1.plot(x1_x2_liste[:,0], "x", c="C0")
        ax1.set_xlabel('Schritte')
        ax1.set_ylabel('Parameter 1', color="C0")
        ax1.tick_params('y', colors="C0")
        ax2 = ax1.twinx()
        ax2.plot(x1_x2_liste[:,1], "x", c="C1")
        ax2.set_ylabel('Parameter 2', color="C1")
        ax2.tick_params('y', colors="C1")
        fig.tight_layout()
        plt.show()
    return x1, x2

# Differenzialmatrix für d2x: Central Differenz
def dif2_matrix(x, dx):
    dif_now = np.diag(np.ones(len(x))) * -2
    dif_pre_ones =  np.ones(len(x)-1)
    dif_pre = np.diag(dif_pre_ones, k=-1)
    dif_post_ones = np.ones(len(x)-1)
    dif_post = np.diag(dif_post_ones, k=1)     
    dif  =  dif_now + dif_pre + dif_post
    dif /= dx**2
    return dif

x = np.linspace(0,2*np.pi, 300)
dx = x[1] - x[0]
d2_m = dif2_matrix(x, dx)

# für die V(x) Matrix
def potential(x):
    V_matrix = np.eye(len(x))
    for i in range(len(x)):
        V_matrix[i,i] *=  V(x[i])
    return V_matrix
V = lambda x: 2 * np.exp(x)

# Multithreading allgemein
from multiprocessing.dummy import Pool as ThreadPool 
from multiprocessing import Pool
pool = Pool() #pool = ThreadPool()
ergebnis_vektor = pool.map(funktion, input_vektor)

# Multithreading für 2d Matix nxn
ergebnis_vektor = np.reshape(ergebnis_matrix, n*n)
input_vektor = np.reshape(input_matrix, n*n)
pool = ThreadPool() #pool = Pool()
ergebnis_vektor = pool.map(funktion,input_vektor)
ergebnis_matrix = np.reshape(ergebnis_vektor, (n, n))

