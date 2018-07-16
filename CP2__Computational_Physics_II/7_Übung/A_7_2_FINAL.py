import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

def force_oszi(x):
  result = np.empty(1)
  result = -x
  return result 
   
def force_columb(x):
  result = np.empty(2)
  result[0] = -x[0]/(x[0]**2 + x[1]**2)**(3/2)
  result[1] = -x[1]/(x[0]**2 + x[1]**2)**(3/2)
  return result

def do_step_columb(data,i,dt):
   pos = 2*data[i-1] - data[i-2] + force_columb(data[i-1])*np.square(dt)
   return pos

def do_step_oszi(data,i,dt):
   pos = 2*data[i-1] - data[i-2] + force_oszi(data[i-1])*np.square(dt)
   return pos

def main_columb(dt,r0):
   t_end = int(2*np.pi/dt)  
   trac = np.zeros((t_end+2,2))  
   trac[0] = np.array([r0,-np.sqrt((2-r0)/r0)*dt]) # acceleration ingored to get the cirlce motion
   trac[1] = np.array([r0,0])  
   for i in range(2,t_end+2):
      trac[i] = do_step_columb(trac,i,dt) 
   return trac

def main_oszi(dt):
   t_end = int(4*np.pi/dt)
   trac = np.zeros(t_end+2)
   trac[0] = 1
   trac[1] = 1 # acceleration automaticlly includet in the third step
   for i in range(2,t_end+2):
      trac[i] = do_step_oszi(trac,i,dt)
   return trac
       


if __name__ == "__main__":
   
#==============================================================================
#    Osszilator 
#==============================================================================
   
   X = np.linspace(0,np.pi*4,2000)
   analytical_oszi = np.cos(X)   
   
   for dt in [.1,.05,0.01,0.005,.001]:
      trac = main_oszi(dt)
      trac_interpolated = np.interp(X,np.linspace(0,4*np.pi,len(trac)),trac)
      plt.plot(X,trac_interpolated-analytical_oszi,label='dt='+str(dt))

   plt.legend()
   plt.show()
   
   
#==============================================================================
#    Coulomb
#==============================================================================
   
   trac = main_columb(.01,1)
   plt.plot(trac[:,0],trac[:,1])
   plt.show()
   
   
   cmap = plt.get_cmap('PiYG')
   
   num=30
   for i,r0 in enumerate(np.linspace(1,1.97,num)):
      trac = main_columb(.01,r0)
      plt.plot(trac[:,0],trac[:,1],color = cmap(i/num))
      plt.scatter(trac[-1,0],trac[-1,1],color = cmap(i/num))
   plt.show()
   
   num=30
   for i,r0 in enumerate(np.linspace(1,1.97,num)):
      trac = main_columb(.001,r0)
      plt.plot(trac[:,0],trac[:,1],color = cmap(i/num))
      plt.scatter(trac[-1,0],trac[-1,1],color = cmap(i/num))
   plt.show()
