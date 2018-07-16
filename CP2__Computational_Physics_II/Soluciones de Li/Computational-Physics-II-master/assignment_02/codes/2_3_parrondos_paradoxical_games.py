import numpy as np
from time import time
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

class parrondos:

    def __init__(self, _jetons, _epsilon):
        self.jetons = _jetons
        self.epsilon = _epsilon
        self.duration = 0

    def doStrategyA(self):
        if self.jetons % 3 == 0:
            if np.random.uniform() < (0.1-self.epsilon):
                self.jetons += 1
            else:
                self.jetons -= 1
        else:
            if np.random.uniform() < (0.75-self.epsilon):
                self.jetons += 1
            else:
                self.jetons -= 1
        self.duration += 1

    def doStrategyB(self):
        if np.random.uniform() < (0.5-self.epsilon):
            self.jetons += 1
        else:
            self.jetons -= 1
        self.duration += 1

def main():
    np.random.seed(int(time()))
    num = 10000
    durations_list = []
    for i in range(num):    
        cirtical = 0
        HouchenLi = parrondos(100, 0.005)
        while HouchenLi.jetons > 0:
            if cirtical in [0, 1]:
                HouchenLi.doStrategyA()
                cirtical += 1
            else:
                HouchenLi.doStrategyB()
                cirtical = 0
            if HouchenLi.jetons > 50000:
                print("waring: HouchenLi has rearched the top.")
                break
        durations_list.append(HouchenLi.duration)
        if i % 100 == 0:
            print("2_3_parrondos_paradoxical_games.py: process has been finished {0}%.".format(int(i/100)))
    
    plt.figure(0)
    plt.hist(durations_list, bins=np.linspace(0,50000,51), density=True, histtype='bar')
    plt.grid()
    plt.xlabel(r"the durations to loss all jetons")
    plt.ylabel(r"probability density function")
    plt.tight_layout()
    plt.savefig("figure_3_4.pdf")
    plt.close()

    return 0

if __name__ == "__main__":
    main()
