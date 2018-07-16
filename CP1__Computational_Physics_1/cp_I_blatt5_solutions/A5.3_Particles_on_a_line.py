import scipy as sci
import pylab as plt
import scipy.linalg as linalg

N=200                    # number of particles
def Vp(r):              # 1st derivative
    vp=-1./r**2         # repulsive 1/r potential
    #vp=-0.5/r**2       # wrong repulsive 1/r potential: forgotten factor of 2 from pairwise sum 
    return vp
    
def Vpp(r):             # 2nd derivative
    vp=2./r**3          # repulsive 1/r potential
    #vp=1/r**3          # wrong repulsive 1/r potential: forgotten factor of 2 from pairwise sum 
    return vp

def dV(x, n):
    # grad(V) for particle n
    # harmonic external potential
    res = sci.copy(x[n])
    # pairwise interaction, derivative V'
    for i in range(x.shape[0]):
        if i != n:
            v = x[n] - x[i]
            d = abs(v)
            res +=Vp(d)*v/d
    return res


def grad(x):
    #grad(V) for all particles x: [[x1],[x2],..]
    res = sci.zeros(x.shape)
    for i in range(x.shape[0]):
        res[i] = dV(x, i)
    return res

def J(x):
    # Jacobian (N)x(N) (Hessian of the potential)
    # x1,x2,x3,x4,...
    jac = sci.eye(N)
    jac = -jac
    for i in range(N):
        for j in range(i):
            r = x[i]-x[j]
            d = abs(r)
            ww=Vp(d)/d
            wwp=Vpp(d)-ww
            jxx = -ww - wwp*r[0]**2/d**2
            jac[i,i]   += jxx		# df_xi/dxi
            jac[i,j]	 -= jxx		# df_xi/dxj
            jac[j,j]   += jxx		# df_xi/dxi
            jac[j,i]	 -= jxx		# df_xi/dxj
    return jac


def newton(x,delta = 1.,eps =  1e-6):  
    # delta: maximal length of shift vector
    # eps: convergence criterion
    j = J(x)
    f = -grad(x)
    f = f.reshape(N)
    dx = sci.linalg.solve(j,f)
    shift=sci.sqrt(sci.dot(dx,dx))
    factor=delta/(delta+shift)
    dx = dx.reshape(N,1)
    x -= factor*dx
    if (shift>eps):
        return False
    return True

xpos=[]
if N==1:
    xpos[0]=0
elif N==2:
    x0=(1/4)**(1/3)  # analytically obtained equilibrium positions 
    xpos.append(-x0)
    xpos.append(x0)
#    xpos[1]= x0
elif N==3:
    x0=(5/4)**(1/3) # analytically obtained equilibrium positions
    xpos.append(-x0)
    xpos.append(  0)
    xpos.append(x0)
    

# Set initial positions, uniformly distributed:
wid=sci.sqrt(N)                 # range for initial conditions
x=sci.linspace(-wid,wid,N)      # linear spacing as a single vector
x=wid*(2*sci.rand(N)-1)             # random initial conditions
x=x.reshape(N,1)                # ... reshaped as array of arrays

print(" Initial positions\n",x)      # print initial condtion

plt.figure()
basevect=sci.ones(N)                 # time = number of iterates
plt.plot(0*basevect,x,'x')
plt.xlabel('Number of iterates')
plt.ylabel('Position')

# First part: Approximate equilibrium with a gradient method
l = 0.05                    # stepsize for gradient method
#l = 0.5                    # stepsize for gradient method set too large for test purposes
nmax = 1000                     # maximum number of iterations
converged = False
i = 0
while i < nmax and converged == False:
#    print(i,sci.transpose(x))   # old position
    i += 1                      # update counter
    d = grad(x)                 # compute gradient
    dl=d.reshape(N)
    dlf=sci.sqrt(sci.dot(dl,dl)) # length of gradient
    fac=l/(l+dlf)               # limit gradient step in length < l
    x -= fac*d                  # update position

    converged = True            # check convergence
    if sci.any(abs(d) > 1e-1):
        converged = False

    tcurrent=i*basevect         # nr of iterates
    plt.plot(tcurrent,x, '.r')  # add current positions

print ("\n Number of gradient-iterations: {0}".format(i))
print ("\n Value of gradients \n",grad(x))
print ("\n Positions after gradient iteration: \n",x)
print()

tNewton=(i+1)*basevect          # result from Newton= i(gradient)+1 for later
plt.xlim(-0.5,i+1.5)            # set xrange for plot
plt.ylim(-1.5*wid,1.5*wid)      # set yrange for plot   
plt.plot(tcurrent,x, 'v')       # change symbol of last position

# By applying a few Newton steps we improve positions
converged = False
i = 0
while (i < nmax and converged == False):
  i += 1
  converged = newton(x,delta=.1) # apply Newton steps up to nmax or convergence

print ("\n Number of Newton-iterations: {0}".format(i))
print("\n Positions after Newton iteration: \n",x)

# print analytical solution for N < 4:
if N<4:
    print("\n Exact positions:\n",xpos) 

print("\nGradients after Newton iteration:")
plt.title('Gradient method + Newton method')
print (grad(x))

plt.plot(tNewton,x,'sg')   # show position after Newton

# determine stability of equilibria:

j = J(x)
ew,ev = sci.linalg.eigh(j)              # determine eigenvalues of Jacobian 
                                        # linalg.eigh returns eigenvalues and eigenvectors of symmetric (applicable here) or Hermitian matrix 
 
print ("\nEigenvalues:")                # print eigenvalues
print (ew)                              

plt.figure()    # new figure for eigenmodes

for l in range(x.shape[0]):
    print(l,ew[l], ev[:,l])             # print eigenvalue and eigenvector
#    ypos=(l+1)*basevect                     # y-position for 
    ypos=-ew[l]*basevect                     # y-position for 
    plt.plot(x,ypos,'ob')               # .. particle positions
    plt.quiver(x,ypos,ev[:,l].reshape(N),0*ypos,scale=8) # & eigenvectors

plt.xlim(-3, 3)
plt.ylim(ymin=0)
plt.xlabel('Position')
plt.ticklabel_format(style='plain')
plt.ylabel('$\omega^2$')
plt.title('Eigenmodes')
plt.show()
