#!/usr/bin/env python

import numpy as np

num_relaxation = 1000
num_statistics = 100000
l = 30
T = 1
lattice = np.random.choice([-1, 1], size=(l, l))

def energy_diff(lattice, L, i, j):
    l = lattice[i-1,j] if i > 0 else lattice[-1, j]
    r = lattice[i+1,j] if i < L-1 else lattice[ 0, j]
    b = lattice[i,j-1] if j > 0 else lattice[ i,-1]
    t = lattice[i,j+1] if j < L-1 else lattice[ i, 0]
    return 2 * lattice[i,j] * (l + r + b + t)

def magnetization_per_site(lattice):
    return np.sum(lattice[:]) / l**2

magn = []

def make_step(lattice, step=None, equilibration=False):
    i, j = np.random.randint(1, l, size=2)
    dE = energy_diff(lattice, l, i, j)
    if dE < 0 or np.random.rand() < np.exp(-dE/T):
        lattice[i,j] *= -1

    #if not equilibration and step % 100:
    #    magn.append(magnetization_per_site(lattice))

for k in range(num_relaxation):
    make_step(lattice, equilibration=True)

for k in range(num_statistics):
    make_step(lattice)