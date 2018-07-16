import numpy as np
import matplotlib.pyplot as plt
from time import time

class SalesmanType:

    stability = 5

    def __init__(self, _num, _temperature, _assert_temperature):
        self.data_ = np.random.uniform(size=(_num, 2))
        self.num_ = _num
        self.temperature_ = _temperature
        self.assert_temperature_ = _assert_temperature
        self.sequence_ = np.copy(range(_num))
        self.duration_ = 0
        self.length = self.calLength_()
        self.diff_length_ = 0.0

    def do_step_(self):
        i, j = np.random.randint(0, self.num_, 2)
        self.sequence_[i], self.sequence_[j] = self.sequence_[j], self.sequence_[i]
        self.diff_length_ = self.calLength_() - self.length
        if (self.diff_length_ < 0.0) or (np.random.uniform() < np.exp(-self.diff_length_/self.temperature_)):
            self.length += self.diff_length_
            self.duration_ = 0
        else:
            self.sequence_[i], self.sequence_[j] = self.sequence_[j], self.sequence_[i]
            self.duration_ += 1
            if self.duration_ == self.stability:
                self.temperature_ *= 0.9
                self.duration_ = 0
        print(self.temperature_, self.length)

    def evaluate(self):
        while self.temperature_ > self.assert_temperature_:
            self.do_step_()

    def calLength_(self):
        length = np.linalg.norm(self.data_[self.sequence_[0],:]-self.data_[self.sequence_[1],:])
        for i in range(1, self.num_-1):
            length += np.linalg.norm(self.data_[self.sequence_[i],:]-self.data_[self.sequence_[i+1],:])
        return length

    def plotPath(self, _file_name):
        plt.figure()
        plt.scatter(self.data_[:,0], self.data_[:,1])
        path = np.empty_like(self.data_)
        for i in range(self.num_):
            path[i,:] = self.data_[self.sequence_[i],:]
        plt.plot(path[:,0], path[:,1])
        plt.xlim((0.0, 1.0))
        plt.ylim((0.0, 1.0))
        plt.savefig(_file_name)
        plt.close()

def main():
    HouchenLi = SalesmanType(9, 1, 0.01)
    HouchenLi.evaluate()
    HouchenLi.plotPath("figure_2.pdf")
    return 0

if __name__ == "__main__":
    main()
