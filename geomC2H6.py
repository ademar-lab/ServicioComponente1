"""
Este programa analizará la hibridacion sp3 a sp2 de una molécula C2H6.

El resultado esperado es una lista de coordenadas de los átomos de hidrógeno, tomando en cuenta un átomo de carbono como el origen del plano x y z. La lista tendrá n elementos por cada n geometrías parciales deseadas.
"""

import numpy as np
import math as math

# Valores iniciales de las variables de interés (SP3)
# Distancia de enlace entre C-H
rCH = 1.07
# Distancia de enlace entre C-C
rCC = 1.54
# Ángulo que incrementará
teta1 = 109.47122
# Ángulo que disminuirá
teta2 =109.47122

# Vectorizar la molécula C2H6 tomando C1 como el origen
a = np.array([np.array([(-rCH*(np.sin(math.radians(teta1/2)))), (rCH*(np.cos(math.radians(teta1/2)))), 0])])
b = np.array([np.array([(rCH*(np.sin(math.radians(teta1/2)))), (rCH*(np.cos(math.radians(teta1/2)))), 0])])

c = np.array([np.array([0, (-rCC*(np.cos(math.radians(teta1/2)))), (rCC*(np.sin(math.radians(teta1/2))))])])
d = np.array([np.array([0, (-rCH*(np.cos(math.radians(teta1/2)))), (-rCH*(np.sin(math.radians(teta1/2))))])])

e = (-1*d) + c
f = (-1*a) + c
g = (-1*b) + c

# Imprimir coordenadas de la molécula inicial
# for x in range(7):
#    print(f"{a[x]}\n{b[x]}\n{d[x]}\n{c[x]}\n{e[x]}\n{f[x]}\n{g[x]}")

# Valores finales de las variables de interés (SP2)
# Se agrega un P(prima) para denotar que es el valor final
# Distancia del doble enlace C=C
rCCP = 1.3552
# Ángulo que incrementó
teta1P = 120
# Ángulo que disminuyó
teta2P = 0

# Diferencias entre SP3 y SP2
deltaRCC = abs(rCCP-rCC)
deltaT1 = abs(teta1P-teta1)
deltaT2 = abs(teta2P-teta2)

# Comenzar el algoritmo
print("\nESTE PROGRAMA ANALIZARÁ LA GEOMETRÍA DE LA HIBRIDACIÓN SP2 A SP3 DE UNA MOLÉCULA C2H6.\nLA SALIDA SERÁ UNA LISTA DE LAS COORDENADAS DE LOS ÁTOMOs EN LOS MOMENTOS DURANTE LA HIBRIDACIÓN SIN CONTAR C1(ORIGEN).")
print("_" * 100)

n = int(input("\nCual es la cantidad de geometrias graduales que deseas? ")) + 1

# Crear una lista de los valores parciales para cada variable
valoresRCC = [rCC-((deltaRCC/(n))*(x+1)) for x in range(n)]
# Troubleshooting
# print(f"r prima: {valoresRCC}")
valoresT1 = [teta1+((deltaT1/(n))*(x+1)) for x in range(n)]
# print(f"teta1: {valoresT1}")
valoresT2 = [teta2-((deltaT2/(n))*(x+1)) for x in range(n)]
# print(f"teta2: {valoresT2}\n")

# Crear una lista de vectores para cada átomo de cada geometría parcial
a = np.array([np.array([(-rCH*(np.sin(math.radians(x/2)))), (rCH*(np.cos(math.radians(x/2)))), 0]) for x in valoresT2])
b = np.array([np.array([(rCH*(np.sin(math.radians(teta1/2)))), (rCH*(np.cos(math.radians(teta1/2)))), 0]) for x in range(n)])

c = np.array([np.array([0, (-y*(np.cos(math.radians(x/2)))), (y*(np.sin(math.radians(x/2))))]) for x, y in zip(valoresT1, valoresRCC)])
d = np.array([np.array([0, (-rCH*(np.cos(math.radians(x/2)))), (-rCH*(np.sin(math.radians(x/2))))]) for x in valoresT1])

e = (-1*d) + c
f = (-1*a) + c
g = (-1*b) + c

# El átomo c cambia de lugar con d debido al posicinamiento de este átomo en el doc .gjf 
atomslist = [a,b,d,c,e,f,g]

for x in range(n-1):
    print(f"\nGEOMETRÍA PARCIAL {x+1}")
    print(f"{a[x]}\n{b[x]}\n{d[x]}\n{c[x]}\n{e[x]}\n{f[x]}\n{g[x]}")

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
        file_path = "templateC2H6.gjf"

        with open(file_path, 'r') as file:
            template = file.read()
            # Número de átomos
            for x in range(7):
                # Número de demensiones para el vector del átomo
                for y in range(3):
                    template = template.replace(f"{x+1}[n][{y}]", f"{atomslist[x][n][y]}")
        print(template)

        new_file_path = f"{n+1}geom.gjf."

        with open(new_file_path, 'w') as file:
            file.write(template)
    
    print(f"File '{new_file_path}' created successfully.")