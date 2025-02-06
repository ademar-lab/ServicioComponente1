"""
Este programa analizará la hibridacion sp3 a sp2 de una molécula de carbono tetrahedral.

El resultado esperado es una lista de coordenadas de los átomos de hidrógeno, tomando en cuenta el átomo de carbono como el origen del plano x y z. La lista tendrá 2+n elementos por cada n geometrías parciales deseadas.
"""

import numpy as np
import math as math

# Establecer los valores iniciales y finales de las variables de interés

# Valores iniciales (SP3)
# Distancia de los enlaces de CH4
r = 1.07
# Ángulo que incrementará
teta1 = 109
# Ángulo que disminuirá
tetaP1 = 109

# Valores finales (SP2)
# Distancia del doble enlace de CH3
rP = 0.9416
# Ángulo que incrementó
teta2 = 119
# Ángulo que disminuyó
tetaP2 = 0

# Diferencias entre SP3 y SP2
deltaR = abs(rP-r)
deltaT = abs(teta2-teta1)
deltaTP = abs(tetaP2-tetaP1)

# Comenzar el algoritmo
print("Este programa analizará la geometria de la hibridacion sp3 a sp2 de una molécula de carbono tetrahedral.\n")

n = int(input("Cual es la cantidad de geometrias graduales que deseas? "))

# Crear una lista de los valores parciales para cada variable
valoresRP = [r-((deltaR/(n))*(x+1)) for x in range(n)]
print(f"r prima: {valoresRP}")
valoresT = [teta1+((deltaT/(n))*(x+1)) for x in range(n)]
print(f"teta: {valoresT}")
valoresTP = [tetaP1-((deltaTP/(n))*(x+1)) for x in range(n)]
print(f"teta prima: {valoresTP}\n")

# Crear una lista de vectores para cada átomo de hidrógeno de cada geometría parcial
a = np.array([np.array([(-1*r*(np.cos(math.radians(x)))), (r*(np.sin(math.radians(x)))), 0]) for x in valoresT])
b = np.array([np.array([(r*(np.cos(math.radians(x)))), (r*(np.sin(math.radians(x)))), 0]) for x in valoresT])

# Trabajar aquí
c = np.array([np.array([0, (-1*y*(np.sin(math.radians(x)))), (y*(np.cos(math.radians(x))))]) for x,y in zip(valoresTP, valoresRP)])
d = np.array([np.array([0, (-1*y*(np.sin(math.radians(x)))), (-1*y*(np.cos(math.radians(x))))]) for x, y in zip(valoresTP, valoresRP)])

print(a)
print(b)
print(c)
print(d)