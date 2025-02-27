"""
Este programa analizará la hibridacion sp3 a sp2 de una molécula C2H6.

El resultado esperado es una lista de coordenadas de los átomos de hidrógeno, tomando en cuenta un átomo de carbono como el origen del plano x y z. La lista tendrá n elementos por cada n geometrías parciales deseadas.
"""

import numpy as np
import math as math

# Valores de interés de molécula en SP3
# Distancia de enlace entre C-H
rCH = 1.07
# Distancia de enlace entre C-C
rCC = 1.54
# Magnitud de todos los ángulos
teta = 109.47122



# Vectorizar la molécula C2H6 tomando C1 como el origen
a = np.array([np.array([(-rCH*(np.sin(math.radians(teta/2)))), (rCH*(np.cos(math.radians(teta/2)))), 0])])
b = np.array([np.array([(rCH*(np.sin(math.radians(teta/2)))), (rCH*(np.cos(math.radians(teta/2)))), 0])])

c = np.array([np.array([0, (-rCC*(np.cos(math.radians(teta/2)))), (rCC*(np.sin(math.radians(teta/2))))])])
d = np.array([np.array([0, (-rCH*(np.cos(math.radians(teta/2)))), (-rCH*(np.sin(math.radians(teta/2))))])])

e = (-1*d) + c
f = (-1*a) + c
g = (-1*b) + c

atomslist = [a,b,c,d,e,f,g]

# Imprimir coordenadas de la molécula inicial
# for x in range(7):
#    print(f"{a[x]}\n{b[x]}\n{d[x]}\n{c[x]}\n{e[x]}\n{f[x]}\n{g[x]}")
