import numpy
import random
import time
import copy
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

class MoMType:
    rank_ = {'31':0, '32':1, '41':2, '42':3, '43':4, '51':5, '52':6, '53':7, '54':8, '61':9, '62':10, '63':11, '64':12, '65':13, '11':14, '22': 15, '33':16, '44':17, '55':18, '66':18, '21':19}

    def __init__(self, _n1, _n2):
        self.data_ = str(numpy.maximum(_n1,_n2)*10+numpy.minimum(_n1,_n2))

    def __lt__(self, other):
        return MoMType.rank_[self.data_] < MoMType.rank_[other.data_]

    def __le__(self, other):
        return MoMType.rank_[self.data_] <= MoMType.rank_[other.data_]

    def __eq__(self, other):
        return self.data_ == other.data_

    def __ne__(self, other):
        return self.data_ != other.data_

    def __gt__(self, other):
        return MoMType.rank_[self.data_] > MoMType.rank_[other.data_]

    def __ge__(self, other):
        return MoMType.rank_[self.data_] >= MoMType.rank_[other.data_]

def main():
    random.seed(time.time())
    MoM_list = []
    duration = []
    num = 1000000
    for i in range(num):
        if len(MoM_list) != 0:
            temp = MoMType(random.randint(1,6), random.randint(1,6))
            if temp >= MoM_list[-1]:
                MoM_list.append(copy.copy(temp))
            else:
                duration.append(len(MoM_list))
                del temp
                del MoM_list[:]
        else:
            temp = MoMType(random.randint(1,6), random.randint(1,6))
            MoM_list.append(copy.copy(temp))
    
    plt.figure(0)
    plt.hist(duration, numpy.arange(0.5, 10.5, 1.0), density=True, histtype='bar')
    plt.grid()
    plt.xlabel("length of non-decreasing duration")
    plt.ylabel("probability")
    plt.savefig("figure_3.pdf")
    plt.close()

    return 0

if __name__ == "__main__":
    main()
