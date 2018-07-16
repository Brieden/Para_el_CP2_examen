import numpy as np
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

class powderRandomType:

    def __init__(self, _alpha):
        self.alpha = _alpha

    def __call__(self, _num):
        return np.power(np.random.uniform(0, 1, _num), 1.0/(self.alpha+1.0))

def main():
    num = 1000000
    f = lambda x, alpha: (alpha+1.0)*np.power(x, alpha)
    alpha_list = np.array([-0.5, -0.3, 0.0, 0.3, 0.5, 1.0, 2.0, 3.0, 4.0])
    x = np.linspace(0.01, 1.0, 1000)
    y = np.empty(1000)
    data = np.empty(num)

    for i in range(8):
        y = f(x, alpha_list[i])
        random = powderRandomType(alpha_list[i])
        data = random(num)

        plt.figure(i)
        plt.hist(data, bins=100, range=(0.0, 1.0), histtype='bar', density=True)
        plt.plot(x, y, '--', label=r"\(\alpha={0}\)".format(alpha_list[i]))
        plt.legend()
        plt.grid()
        plt.xlabel("Random Numbers")
        plt.ylabel("probability density")
        plt.tight_layout()
        plt.savefig("figure_3{0}.pdf".format(i))
        plt.close()

    return 0

if __name__ == "__main__":
    main()
