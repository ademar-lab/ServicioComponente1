"""
Este programa analizará la hibridacion sp3 a sp2 de una molécula C2H6.

El resultado esperado es una lista de coordenadas de los átomos de hidrógeno, tomando en cuenta un átomo de carbono como el origen del plano x y z. La lista tendrá n elementos por cada n geometrías parciales deseadas.
"""

import numpy as np
import math as math

# Definir función de magnitud para tomar en cuenta el cambio de distancia entre átomos 
def magnitude(vector): 
    return math.sqrt(sum(pow(element, 2) for element in vector))

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
a = np.array([(-rCH*(np.sin(math.radians(teta1/2)))), (rCH*(np.cos(math.radians(teta1/2)))), 0])
b = np.array([(rCH*(np.sin(math.radians(teta1/2)))), (rCH*(np.cos(math.radians(teta1/2)))), 0])

c = np.array([0, (-rCC*(np.cos(math.radians(teta1/2)))), (rCC*(np.sin(math.radians(teta1/2))))])
d = np.array([0, (-rCH*(np.cos(math.radians(teta1/2)))), (-rCH*(np.sin(math.radians(teta1/2))))])

e = (-1*d) + c
f = (-1*a) + c
g = (-1*b) + c

iniatialatomslist = [a,b,d,c,e,f,g]

# Imprimir coordenadas de la molécula inicial
# for x in range(7):
#    print(f"{a[x]}\n{b[x]}\n{d[x]}\n{c[x]}\n{e[x]}\n{f[x]}\n{g[x]}")

# Valores finales de las variables de interés (SP2)
# Se agrega un P(prima) para denotar que es el valor final
# Distancia del doble enlace C=C
rCCp = 1.3552
# Ángulo que incrementó
teta1p = 120
# Ángulo que disminuyó
teta2p = 0

# Diferencias entre SP3 y SP2
deltaRCC = abs(rCCp-rCC)
# Diferencia entre los átomos de hidrógeno que entran y C
deltaRCH = abs(rCCp-rCH)
# Diferencia del ángulo que incrementó
deltaT1 = abs(teta1p-teta1)
# Diferencia del anguló que disminuyó
deltaT2 = abs(teta2p-teta2)

# Vectorizar la molécula C2H6 tomando C1 como el origen
ap = np.array([0, (-rCCp*(np.cos(math.radians(teta1/2)))), (rCCp*(np.sin(math.radians(teta1/2))))])
bp = np.array([0, (rCH*(np.sin(math.radians(90-deltaT1)))), (rCH*(np.cos(math.radians(90-deltaT1))))])

cp = ap
dp = np.array([0, (-rCH*(np.cos(math.radians((teta1/2)+deltaT1)))), (-rCH*(np.sin(math.radians((teta1/2)+deltaT1))))])

ep = (-1*dp) + cp
fp = (-1*ap) + cp
gp = (-1*bp) + cp

finalatomslist = [ap,bp,dp,cp,ep,fp,gp]

# Calcular los vectores difereranciales (solo incluye cambio de ángulos)
difvecatomslist = []
for i in range(7):
    difvecatomslist.append(finalatomslist[i]-iniatialatomslist[i])
    # print(difvecatomslist[i])
difvecatomslist = np.array(difvecatomslist)

# Comenzar el algoritmo
print("\nESTE PROGRAMA ANALIZARÁ LA GEOMETRÍA DE LA HIBRIDACIÓN SP2 A SP3 DE UNA MOLÉCULA C2H6.\nLA SALIDA SERÁ UNA LISTA DE LAS COORDENADAS DE LOS ÁTOMOs EN LOS MOMENTOS DURANTE LA HIBRIDACIÓN SIN CONTAR C1(ORIGEN).")
print("_" * 100)

n = int(input("\nCual es la cantidad de geometrias graduales que deseas? ")) + 1

# Crear una lista de los valores parciales para cada variable
difvecatomslist = difvecatomslist/n
# print("\ndifvectatomslist/n:\n")
# for i in range(7):
#     print(difvecatomslist[i])
# print("\ninitialatomslist:\n")
# for i in range(7):
#     print(iniatialatomslist[i])

# Crear una lista de vectores para cada átomo de cada geometría parcial
partialgeoms = []
for i in range(n):
    print("\n")
    partialgeom = []
    for j in range(7):
        #Se multiplica el vector por una variable aux que ajustará su magnitud a la apropiada 
        # #Se ajusta el vector a
        if j == 0:
            vec = np.array([iniatialatomslist[j] + (i+1)*difvecatomslist[j]])
            vec = vec * (rCH+(i+1)*(deltaRCH/n))/magnitude(vec[0])
            print(magnitude(vec[0]))
            partialgeom.append(vec)
        # #Se ajusta el vector b
        if j == 1:
            vec = np.array([iniatialatomslist[j] + (i+1)*difvecatomslist[j]])
            vec = vec * (rCH/magnitude(vec[0]))
            print(magnitude(vec[0]))
            partialgeom.append(vec)
        # Se ajusta el vector c
        if j == 3:
            partialgeom.append(np.array([iniatialatomslist[j] + (i+1)*difvecatomslist[j]]))
        # Se ajustan los vectores d y e
        if j == 2 or j == 4:
            # print("d or e")
            partialgeom.append(np.array([iniatialatomslist[j] + (i+1)*difvecatomslist[j]]))
        # vector f
        if j == 5:
            vec = -1*partialgeom[0][0] + partialgeom[3][0]
            partialgeom.append(np.array([vec]))
        # vector g
        if j == 6:
            vec = -1*partialgeom[1][0] + partialgeom[3][0]
            partialgeom.append(np.array([vec]))
    partialgeoms.append(partialgeom)
# print(magnitude(partialgeoms[0][0][0]))

partialgeoms = np.array(partialgeoms)
# for x in partialgeoms[2,5,0]:
#     print(x)

print(partialgeoms)

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
    for n in range(n):
        # Insertar las coordenadas en la plantilla .gjf
        file_path = "templateC2H6.gjf"

        with open(file_path, 'r') as file:
            template = file.read()
            # Número de átomos
            for x in range(7):
                # Número de demensiones para el vector del átomo
                for y in range(3):
                    template = template.replace(f"{x+1}[n][{y}]", f"{partialgeoms[n,x,0,y]}")
        #print(template)

        new_file_path = f"{n+1}geom.gjf."

        with open(new_file_path, 'w') as file:
            file.write(template)
    
    print(f"File '{new_file_path}' created successfully.")