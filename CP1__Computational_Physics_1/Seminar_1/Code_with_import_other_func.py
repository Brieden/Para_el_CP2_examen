import numpy as np
import matplotlib.pyplot as plt
from In_der_Übung import Reihe as Reihe
import os

#if not os.mkdir("data2"):

#print(Reihe(100, 0.2, 2))

index = 6
name = "Daten"
Data = np.array(Reihe(100, 0.2, 2))
np.save("data/run" + str(index) + ".npy", Data)

#print(os.path())
