"""
Este programa analizará la hibridacion sp3 a sp2 de una molécula de carbono tetrahedral.

El resultado esperado es una lista de coordenadas de los átomos de hidrógeno, tomando en cuenta el átomo de carbono como el origen del plano x y z. La lista tendrá n elementos por cada n geometrías parciales deseadas.
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
print("\nESTE PROGRAMA ANALIZARÁ LA GEOMETRÍA DE LA HIBRIDACIÓN SP2 A SP3 DE UNA MOLÉCULA CH4.\nLA SALIDA SERÁ UNA LISTA DE LAS COORDENADAS DE LOS ÁTOMOS H EN LOS MOMENTOS DURANTE LA HIBRIDACIÓN.")
print("_" * 100)

n = int(input("\nCual es la cantidad de geometrias graduales que deseas? ")) + 1

# Crear una lista de los valores parciales para cada variable
valoresRP = [r-((deltaR/(n))*(x+1)) for x in range(n)]
# Troubleshooting: print(f"r prima: {valoresRP}")
valoresT = [teta1+((deltaT/(n))*(x+1)) for x in range(n)]
# print(f"teta: {valoresT}")
valoresTP = [tetaP1-((deltaTP/(n))*(x+1)) for x in range(n)]
# print(f"teta prima: {valoresTP}\n")

# Crear una lista de vectores para cada átomo de hidrógeno de cada geometría parcial
a = np.array([np.array([(-1*r*(np.cos(math.radians(90-(x/2))))), (r*(np.sin(math.radians(90-(x/2))))), 0]) for x in valoresT])
b = np.array([np.array([(r*(np.cos(math.radians(90-(x/2))))), (r*(np.sin(math.radians(90-(x/2))))), 0]) for x in valoresT])

c = np.array([np.array([0, (-1*y*(np.sin(math.radians(90-(x/2))))), (y*(np.cos(math.radians(90-(x/2)))))]) for x,y in zip(valoresTP, valoresRP)])
d = np.array([np.array([0, (-1*y*(np.sin(math.radians(90-(x/2))))), (-1*y*(np.cos(math.radians(90-(x/2)))))]) for x, y in zip(valoresTP, valoresRP)])

atomslist = [a,b,c,d]

for x in range(n-1):
    print(f"\nGEOMETRÍA PARCIAL {x+1}")
    print(f"{a[x]}\n{b[x]}\n{c[x]}\n{d[x]}")

# Generar los documentos .gjf
flag = True
print("_"*100)
# Restringir las entradas a 'y' y 'n'
while(flag):
    ans = input("\n¿QUIERES CREAR UN DOCUMENTO .gjf PARA CADA UNA DE LAS GEOMETRÍAS PARCIALES?\n Responde 'y' para sí, 'n' para no. ")
    if ans == 'y' or ans == 'n':
        flag = False
        if ans == 'y':
            ans = True
        else:
            ans = False

if ans:
    # Creación de un archivo .gjf por cada geometria parcial
    for n in range(n-1):
        # Insertar las coordenadas en la plantilla .gjf
        file_path = "template.gjf"

        with open(file_path, 'r') as file:
            template = file.read()
            # Número de átomos de H
            for x in range(4):
                # Número de demensiones para el vector del átomo H
                for y in range(3):
                    template = template.replace(f"{x+1}[n][{y}]", f"{atomslist[x][n][y]}")
        print(template)

        new_file_path = f"{n+1}geom.gjf."

        with open(new_file_path, 'w') as file:
            file.write(template)
    
    print(f"File '{new_file_path}' created successfully.")