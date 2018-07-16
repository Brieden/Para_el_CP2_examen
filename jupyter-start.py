import numpy as np
import matplotlib.pyplot as plt
#import sympy as sp
#import scipy.constants as constants
#from IPython.display import HTML, display, Math, Latex

#plt.style.use('dark_background')
plt.style.use('bmh')
plt.rcParams['figure.figsize'] = (15.0, 9.0)
plt.rcParams['figure.dpi'] = 200
plt.rcParams['font.size'] = 16
%matplotlib inline

def tabelle_darstellen(data):
    """Eine Funktion, die Tabellen und Arrays schön darstellt"""
    display(HTML(
        '<table><tr>{}</tr></table>'.format(
            '</tr><tr>'.join(
                '<td>{}</td>'.format('</td><td>'.join(str(_) for _ in row)) for row in data)
            )
     ))

def Fehlerfunktionsgenerator(funktion, variablen, name_funktion, name_ableitung):
    """Eine Funktion, die automatisch die Fehlerformel generiert
    orientiert bei https://www.physi.uni-heidelberg.de/Einrichtungen/AP/python/Fehlerrechnung.html
    """
    fehler = 0
    fehlersymbole=[]
    ableitungen_quadr = []

    for var in variablen:
        d = sp.symbols('d' + var.name)        #Symbole fuer die Fehler generieren
        fehlersymbole.append(d)               #Fehlersymbole in Liste eintragen
        partial = sp.diff(funktion, var) * d  #Partielle Differentation und mit mit Fehlersymbol 'd' multiplizieren
        ableitungen_quadr.append(partial**2)  
        fehler = fehler + partial**2

    fehler_abs=sp.sqrt(fehler)              #Latex Format fuer den absoluten Fehler
    fehler_abs_vereinfacht=sp.simplify(sp.sqrt(fehler))              #Latex Format fuer den absoluten Fehler
    
    print('Funktion: ', name_funktion,)
    display(Math("="+sp.latex(funktion)))
    print('Absoluter Fehler:', name_ableitung," = Δ", name_funktion)
    display(Math("="+sp.latex(fehler_abs).replace('d',r'\Delta ') +'='+sp.latex(fehler_abs_vereinfacht).replace('d',r'\Delta ')))   #Formel absoluter Fehler
    return fehler_abs_vereinfacht

def variablenname_zu_string(variable, lokale_variablen = locals()):
    """"Funktion um den Namen im Code einer Codevariabel als String zu erhalten"""
    for k, v in list(lokale_variablen.items()):
        if v is variable:
            return k