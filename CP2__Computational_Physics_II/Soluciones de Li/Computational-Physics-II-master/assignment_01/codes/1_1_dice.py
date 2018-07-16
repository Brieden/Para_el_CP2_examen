import numpy
import random
import time
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def genDicePair():
    return [random.randint(1,6), random.randint(1,6)]

def genDicetriplet():
    return [random.randint(1,6), random.randint(1,6), random.randint(1,6)]

def main():
    num = 1000000
    duplet = []
    triplet = []
    for i in range(num):
        temp_d=genDicePair()
        temp_t=genDicetriplet()
        duplet.append((temp_d[0]-1)*6+(temp_d[1]-1))
        triplet.append((temp_t[0]-1)*6*6+(temp_t[1]-1)*6+(temp_t[2]-1))
    
    duplet=numpy.array(duplet)

    plt.figure(0)
    plt.hist(duplet, numpy.arange(-0.5,36.5,1.0), density=True,histtype='bar')
    plt.grid()
    plt.savefig('figure_1_a.pdf')
    plt.close()

    plt.figure(1)
    plt.hist(triplet, numpy.arange(-0.5,216.5,1.0), density=True,histtype='bar')
    plt.grid()
    plt.savefig('figure_1_b.pdf')
    plt.close()

    return 0
    

if __name__ == "__main__":
    main()
