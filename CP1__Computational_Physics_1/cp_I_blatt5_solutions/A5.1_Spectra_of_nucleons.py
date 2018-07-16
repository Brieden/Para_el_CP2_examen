from scipy import zeros,pi,sqrt
import scipy.optimize as opt
import scipy.special as scs
import scipy as sci

import pylab as plt

# Spherical Bessel functions
def Jn(x, n):
    return scs.jv(n+.5, x) * sqrt(pi/2/x) # workaround for scipy versions < 0.18.0
    #return scs.spherical_jn(n,x)         # for scipy versions >= 0.18.0 
                                          # you can check your version with print(scipy.__version__) 

# or with lambda keyword:
# Jn = lambda x,n: scs.jv(n+.5, x) * sqrt(pi/2/x)
    
# Create an array of wavenumbers for all n and l
nmax = 10
lmax = 10
knl = zeros([nmax*lmax, 3]) # 1 col: n, 2 col: l, 3 col: k_nl
i = 0
for l in range(lmax): # loop over angular momentum quantum number
    # Find sign changes in Jn and use that for bisections
    xstep = 0.5
    x0 = xstep
    Jn0 = Jn(x0, l)
    n = 0
    while n < nmax:
        Jn1 = Jn0
        x0 += xstep
        Jn0 = Jn(x0, l)
        if Jn0*Jn1 < 0: # sign change
            # Found sign change: compute root and store it in knl
            #root = opt.bisection(Jn, x0-xstep, x0, args=(l,))
            root = opt.bisect(Jn, x0-xstep, x0, args=(l,))
            n += 1
            knl[i,0] = n
            knl[i,1] = l
            knl[i,2] = root
            i += 1

# Sort array by wavenumber knl[:,2] (E \propto knl**2) 
knl = knl[knl[:,2].argsort()]

# Print 10 lowest wavenumbers
l2s = ["S", "P", "D", "F", "G", "H", "I", "J", "K"] # map l to letter
for i in range(10):
    l = int(knl[i,1])
    print(str(int(knl[i,0])) + l2s[l] +  ": " + str(knl[i,2]))


# plot bessel functions:
scale = 1
fig = plt.figure()
fig.subplots_adjust(bottom = 0.15/scale, left = 0.1/scale, right = 1-(1-0.97)/scale,top = 1-(1-0.97)/scale, wspace = .4*scale,hspace = 0.3*scale)


i = 0
x = sci.linspace(1e-6,1,100)

for i in range(9):
  plt.subplot(3,3,i+1)
  plt.plot(x,Jn(knl[i,2]*x,knl[i,1]))
  plt.axhline(0.0,c='0.5')
  plt.xlabel(r'$x/R$')
  plt.ylabel(r'$j_{{{0}{1}}}$'.format(int(knl[i,0]),l2s[int(knl[i,1])]))
  plt.ylim(-0.4,1.0)


fig.set_size_inches((8*scale,8*scale))
plt.savefig("A5.1_Spectra.pdf")
