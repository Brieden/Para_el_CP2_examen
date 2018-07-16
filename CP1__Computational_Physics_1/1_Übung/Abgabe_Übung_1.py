import numpy as np
import matplotlib.pyplot as plt
#%matplotlib notebook
#%matplotlib qt
#######################################################################
#                               Aufgabe 1                             #
#######################################################################
"""
errechnete kleinste Zahl in Python = 5e-324
das enstpricht dem Binary String:
bstr = '0000000000000000000000000000000000000000000000000000000000000001'
Nach dem Industriestandert IEEE 754-1985 Double precision: 64 bits	
Zahlenspektrum voller Genauigkeit: ±2.23×10^−308 to ±1.80×10^308
Genauigkeit ungefähr 16 Stellen

64bit = 1bit Vorzeichen + 11bit Exponent + 52bit Mantisse

11bit Exponent = 1bit Vorzeichen + 10bit Zahl
größte Zahl aus 10bit: 2^10-1 
  
"""

def suche_kleine_Zahl():
    Zahl = 1
    Zahl_halbe = 1
    while Zahl_halbe > 0 :
        Zahl = Zahl_halbe
        Zahl_halbe = Zahl_halbe/2
    return Zahl

def augabe1(x):
    ε = 1
    while x != x + ε:
        ε = ε / 2
    return ε * 2

if 0:
    print("%E" %augabe1(1))
    print("%.75f" % (1+augabe1(1)))

    exit()
#######################################################################
#                               Aufgabe 2                             #
#######################################################################


def Vorwärtsdifferenziernug(func, x, h):
    return (func( x + h) - func( x )) / h
def Rückwärtsdifferenziernug(func, x, h):
    return (func( x ) - func( x - h)) / h
def Zentralerdifferenziernug(func, x, h):
    return (func( x + h ) - func( x - h)) / (2 * h)

def testfunktion(x):
    if 1:
        ausgabe = []
        for xp in x:
            if xp<np.pi:
                ausgabe.append(xp/2)
            elif xp<7.5:
                ausgabe.append(1.5)

            else:
                ausgabe.append(np.sin(xp))
        return np.array(ausgabe)

x = 1
n = np.arange(0, 50)
h = (2.**(-n))

Ableitung1 = [Vorwärtsdifferenziernug(np.cos, x, h_) for h_ in h]
Ableitung2 = [Rückwärtsdifferenziernug(np.cos, x, h_) for h_ in h]
Ableitung3 = [Zentralerdifferenziernug(np.cos, x, h_) for h_ in h]

#plt.plot(h, -np.sin(x)-Ableitung1, "+")
plt.plot(h, -np.sin(x)-Ableitung2, "x")
#plt.plot(h, -np.sin(x)-Ableitung3, "--")


#plt.legend()
plt.loglog()
#plt.ylim([-0.0000001, ])
plt.show()

