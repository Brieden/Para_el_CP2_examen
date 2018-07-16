""" Ising-Modell
    
    Einem (nxn)-Gitter wird jedem Punkt mit entsprechender Wahrscheinlichkeit
    (beeinflussbar durch die mittlere Magnetisierung m, die anfangs auf das 
    Gitter wirkt) der Spin 1 oder -1 zugeordnet. 
    Die Monte-Carlo-Methode berechnet dann, wie wahrscheinlich es ist, dass der
    Spin flipt. 
    Bei der Zeitentwicklung laufen mehrere Monte-Carlo-Schritte hintereinander
    ab und man kann das Verhalten mit den analytischen Werten vergleichen.
"""
    
from __future__ import division
from numpy import *
from matplotlib import pyplot as plt

def young(tau_a, tau_c, tau_e):
    """ Plottet die analytischen Werte fuer die mittlere Magnetisierung 
        in den zweiten Plotbereich.
            tau_a : Anfangswert des Plotbereichs
            tau_c : kritische Temperatur (dimensionslos)
            tau_e : Endwert des Plotbereichs
    """
    tau1 = linspace(tau_a, tau_c, 200)      # Graph wurde in 4 Teile aufgeteilt
    m1 = (1-1/sinh(2/tau1)**4)**(1/8)       # 2x tau < tau_c
    m2 = -m1                                # 
    tau3 = [tau_c, tau_c]                   # tau = tau_c 
    m3 = linspace(-0.538, 0.538, 2)         # 
    tau4 = linspace(tau_c, tau_e, 2)        # und tau > tau_c 
    m4 = zeros(2)                           #
    plt.axes(ax2)                           #
    plt.plot(tau1, m1, lw=2, c='b', label='analytischer Wert')
    plt.plot(tau1, m2, lw=2, c='b')
    plt.plot(tau3, m3, lw=2, c='b')
    plt.plot(tau4, m4, lw=2, c='b')

def matr(n, m, tau):
    """ Erstellt eine (nxn)-Matrix, in der die Spins erzeugt werden. 
        Dafuer werden die Vorzeichen von gleichverteilte Zufallszahlen um ei-
        nen Mittelpunkt berechnet. 
        Bei zunehmender Magnetisierung m verschiebt sich der Mittelpunkt der
        Zufallszahlen entsprechend.
        Ausserdem wird die erste Spinmatrix, sowie der erste (tau,m)-Zustand
        geplottet.
            n   : bestimmt Groesse der Matrix
            m   : mittlere Magnetisierung
            tau : dimensionslose Temperatur
    """
    matr = sign(random.uniform(-1+m, 1+m, (n,n))) # Erstellen der Spinmatrix
    m = sum(matr)/n**2                            # Berechnen der tatsaech-
                                                  # lichen mittleren Magneti-
                                                  # sierung 
    # Plotten der Spinmatrix
    plt.axes(ax1)
    plt.imshow(matr, interpolation='nearest', cmap ='gray', vmin =-1, vmax=1)
    
    # Plotten des ersten (tau,m)-Zustandes
    plt.axes(ax2)
    plt.plot(tau, m, '+', ms=10, c='r', label='Zustand')
    plt.draw()
    return matr
    
def montecarlo(n, m, tau, matrix):
    """ Die Monte-Carlo-Methode berechnet fuer jeder Stelle (i,j) der Matrix, 
        wie gross die Energiedifferenz bei einem Spinflip waere und berechnet
        dann die Wahrscheinlichkeit des Spinflips (FWS).
        Hier wird ein Monte-Carlo-Schritt durchgefuehrt. 
    """
    
    for i in arange(n**2):                   # n**2 Stellen der Matrix werden 
                                             # analysiert, wobei die Stellen
        i,j = int32(random.uniform(0, n, 2)) # zufaellig ausgewaehlt werden 
        delta_H = (2*matrix[i,j]             # Berechnung der Energiedifferenz
            * (matrix[(i-1)%n,j] + matrix[(i+1)%n,j]    # bei moeglichem Spin-
            + matrix[i,(j-1)%n] + matrix[i,(j+1)%n]))   # flip
        
        if delta_H < 0:                         # an dieser Stelle (i,j) wird
                                                # durch den Flip Energie frei
                                                # -> energetisch guenstiger 
            matrix[i,j] = -matrix[i,j]          # -> Flipwahrscheinlichkeit=1 
            
            
        else:                                   # an dieser Stelle (i,j) muss
                                                # fuer den Flip Energie aufge-
                                                # wendet werden
            FWS = exp(-delta_H/tau)             # Berechnung der Wahrscheinlich
            matrix[i,j] = (matrix[i,j]          # -> Flipwahrscheinlichkeit=FWS
                *sign(random.uniform(-FWS, 1-FWS))) 
    
    return matrix

def Zeitentwicklung(n, m, tau, t_schritte, matrix):
    """ Bei der Zeitentwicklung werden nacheinander mehrere Monte-Carlo-
        Schritte durchgefuehrt und das jeweilige Ergebnis in beiden Plot-
        bereichen geplottet.
            t_schritte : Anzahl der Monte-Carlo-Schritte
            matrix     : Anfangsmatrix, muss uebergeben werden, damit sie 
                         nur einmal berechnet wird (Zufallszahlen)
    """
    # Spinmatrix
    plt.axes(ax1)                     
    matrix_plot = plt.imshow(matrix, interpolation='nearest', 
                            cmap ='gray', vmin =-1, vmax=1)
    
    for t in arange(t_schritte):
        matrix = montecarlo(n, m, tau, matrix) # Berechnen der neuen Spinmatrix
        plt.setp(matrix_plot, array=matrix)    # 
                                               #
        # Phasendiagramm                       #
        plt.axes(ax2)                          #
        m = sum(matrix)/n**2                   # tatsaechliche mittlere Magne-
        plt.plot(tau,m,'+', ms=10, c='r')      # tisierung
        plt.draw() 

def maus(event):
    """ Klick in rechten Plotbereich waehlt neuen tau- und m-Wert, 
        Klick in linken Plotbereich startet die Zeitentwicklung.
    """
    global m, tau, matrix                        
    
    if (event.button == 1 and 
    plt.get_current_fig_manager().toolbar.mode == '' and event.inaxes):
    
        if event.inaxes == ax1:                # Spinmatrix-Plotbereich       
            Zeitentwicklung(n, m, tau, t_schritte, matrix)
                                                     
        else:                                  # wenn in Phasendiagramm
            tau = event.xdata                  # geklickt wird,
            m = event.ydata                    #   
            matrix = matr(n, m, tau)           # wird entsprechender Punkt
            plt.axes(ax1)                      # und zugehoerige Spinmatrix
            plt.imshow(matrix)                 # gezeichnet
    
# Hauptprogramm

n = 50                        #
m = 0.8                       # nur fuer erstes Bild
tau = 1.5                     # werden spaeter per Mausklick ausgewaehlt
t_schritte = 10               #  
tau_a = 0.01                  #
tau_c = 2.266                 # ungefaehrer Wert
tau_e = 4                     #

print __doc__
print ("Verwendete Parameter:\n \
Breite/Hoehe des Gitters                       n = %s \n \
Anfangswert der mittleren Magnetisierung       m = %s \n \
Anfangswert der dimensionslosen Temperatur   tau = %s \n \
Anzahl der Monte-Carlo-Schritte       t_schritte = %s \n \
Kritische dimensionslose Temperatur        tau_c = %s" 
%(n, m, tau, t_schritte, tau_c))
print "--------------------"
print (" \n \
Klick in den linken Plotbereich startet die Zeitentwicklung. \n \
Klick in den rechten Plotbereich waehlt neues tau, m. \n")
print "--------------------"


plt.figure(0, figsize=(16,8)) .canvas.set_window_title('Ising-Methode')

# Spinmatrix
ax1 = plt.subplot(121)
plt.title('Spinmatrix')

# Phasendiagramm
ax2 = plt.subplot(122)
plt.title('Phasendiagramm')
plt.xlabel(r'dimensionslose Temperatur $\tau$')               
plt.ylabel('mittlere Magnetisierung $m$')
plt.axis([tau_a, tau_e, -1.1, 1.1])

young(tau_a, tau_c, tau_e)
matrix = matr(n,m,tau) 

plt.connect("button_press_event", maus)

plt.legend()
plt.show()

""" tau = 1.5 < tau_c
    Je weiter die mittlere Magnetisierung m beim Start von 0 weg ist (also 
    naeher an der Grenze m=1 bzw m=-1), desto schneller naehert sich m der 
    naechstgelegenen Grenze an. (Das Spinbild nimmt nach und nach eine Farbe
    an)
    Ist der Start m-Wert bei +-0.5, oder noch etwas naeher bei m=0, so bilden
    sich mit der Zeit einige grosse Felder mit gleichem Spin, die sich nur 
    schwer aufloessen und somit die Geschwindigkeit, mit der m gegen die 
    naechste Grenze geht, vermindert.
    Waehlt man den Startpunkt sehr nahe an m=0, so scheinen die m um 0 zu 
    oszillieren, allerdings bilden sich schnell sehr grosse schwarze und 
    weisse Bereiche. Deshalb 'oszilliert' es auch, da sich grosse Bereiche
    wegen der Kopplung der Stelle (i,j) zu den umliegenden Partner langsamer
    wieder aufloesen. 
    Tatsaechlich wuerde sich m nach sehr vielen Schritten einer der beiden 
    Grenzen annaehern. Welcher Grenze wird zufaellig entschieden. 
    Das Gitter/der Stoff ist bei tau < tau_c nach unterschiedlich vielen 
    Zeitschritten vollstaendig in eine Richtung magnetisiert. 
    
    tau = 3 > tau_c
    Egal wie weit m von m=0 enfernt ist, m laeuft immer etwa gleich schnell zu
    m = 0, also dem analytischen Wert. 
    Das Gitter ist bei tau > tau_c nach unterschiedlich vielen Schritten un-
    magnetisch.
"""
