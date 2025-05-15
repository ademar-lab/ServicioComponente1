import numpy as np
import math as math
import utilities as utils

# Definir función de magnitud para tomar en cuenta el cambio de distancia entre átomos 
def magnitude(vector): 
    return math.sqrt(sum(pow(element, 2) for element in vector))

# Obtener la lista de coordenadas de los átomos de la molécula
# Las coordenadas de los átomos se encuentran en el archivo "sp3-coordinates.txt" y "sp2-coordinates.txt"
sp3_atoms_list = utils.parse_atom_coordinates("sp3-coordinates.txt")
sp2_atoms_list = utils.parse_atom_coordinates("sp2-coordinates.txt") 

# Se alinean las moléculas cationicas centrales de sp3 y sp2 en la misma posición 
# Se alinea la molécula cationica central de sp3 con el eje z
print("\nSP3")
for i in range(44):
    # Se lleva el primer átomo de Carbono al origen
    sp3_atoms_list[i] = sp3_atoms_list[i]-[2.48855387, -0.84573070, 0.82053390]

sp3_atoms_list = np.array(sp3_atoms_list)

# Calcular el ángulo de rotación necesarrio con respecto al eje x
tetax = -(math.atan(sp3_atoms_list[0, 2]/sp3_atoms_list[0, 1])) # atan retorna valores de -PI/2 a PI/2
# Calcular la matriz de rotación respecto al eje x
matriz_rot_x = np.array([[1, 0, 0],
                        [0, math.cos(tetax), -math.sin(tetax)],
                        [0, math.sin(tetax), math.cos(tetax)]])

# Aplicar la matriz de rotación a cada átomo de la molécula sp3
for i in range(44):
    sp3_atoms_list[i] = np.dot(matriz_rot_x, sp3_atoms_list[i])

# Se alinea la molécula cationica central de sp2 con el eje z
print("\nSP2")
for i in range(44):
    # Se lleva el primer átomo de Carbono al origen
    sp2_atoms_list[i] = sp2_atoms_list[i]-[2.48872136, 0.02402876, 0.00962054]

sp2_atoms_list = np.array(sp2_atoms_list)

# Calcular el ángulo de rotación necesarrio con respecto al eje x
tetax = -(math.atan(sp2_atoms_list[0, 2]/sp2_atoms_list[0, 1])) # atan retorna valores de -PI/2 a PI/2

# Calcular la matriz de rotación respecto al eje x
matriz_rot_x = np.array([[1, 0, 0], 
                        [0, math.cos(tetax), -math.sin(tetax)],
                        [0, math.sin(tetax), math.cos(tetax)]])

# Aplicar la matriz de rotación a cada átomo de la molécula sp2
for i in range(44):
    sp2_atoms_list[i] = np.dot(matriz_rot_x, sp2_atoms_list[i])

# Calcular los vectores difereranciales (solo incluye cambio de ángulos)
difvecatomslist = sp2_atoms_list-sp3_atoms_list

# Comenzar el algoritmo
print("\nESTE PROGRAMA ANALIZARÁ LA GEOMETRÍA DE LA HIBRIDACIÓN SP2 A SP3 DE UNA MOLÉCULA LI-7 en el vacío.\nLA SALIDA SERÁ UNA LISTA DE LAS COORDENADAS DE LOS ÁTOMOS EN LOS MOMENTOS DURANTE LA HIBRIDACIÓN SIN CONTAR C1(ORIGEN).")
print("_" * 100)

n = int(input("\nCual es la cantidad de geometrias graduales que deseas? ")) + 1

# Crear una lista de los valores parciales para cada variable
difvecatomslist = difvecatomslist/n

# Valores iniciales de las variables de interés (SP3)
# Distancia de enlace entre C-H
rCH = 1.07
# Distancia de enlace entre C-C
rCC = 1.54
# Distancia de enlace entre C-N
rCN = 1.47
# Ángulo que incrementará
teta1 = 109.47122
# Ángulo que disminuirá
teta2 =109.47122

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

# Obtener las coordenadas de la molécula catiónica de un extremo con el C2 como origen
moleculaCationica = {}
for i in range(44):
    if i >= 20 and i <= 26:
        moleculaCationica[i] = sp3_atoms_list[i]
    elif i == 34:
        moleculaCationica[i] = sp3_atoms_list[i]
    elif i >= 36 and i <= 39:
        moleculaCationica[i] = sp3_atoms_list[i]

for i in range(44):
    if i in moleculaCationica:
        moleculaCationica[i] = moleculaCationica[i] - sp3_atoms_list[16]

# Obtener las coordenadas de la molécula catiónica de un extremo(izquierdo) con el C2 como origen
moleculaCationicaLeft = {}

for i in range(44):
    if i >= 27 and i <= 33:
        moleculaCationicaLeft[i] = sp3_atoms_list[i]
    elif i == 35:
        moleculaCationicaLeft[i] = sp3_atoms_list[i]
    elif i >= 40 and i <= 43:
        moleculaCationicaLeft[i] = sp3_atoms_list[i]

for i in range(44):
    if i in moleculaCationicaLeft:
        moleculaCationicaLeft[i] = moleculaCationicaLeft[i] - sp3_atoms_list[18]

# print("\nMolecula Cationica:")
# for i in range(44):
#     if i in moleculaCationica:
#         print(f"Átomo {i}: {moleculaCationica[i]}")

# Establecer coordenadas para formar dos moléculas de hidrógeno
hmol = np.array([0.3, 0, 5.0])

firstrun = 2

breakatom8 =  np.array([0.72862954, -0.77077669, 0.4012653])
breakatom10 = np.array([-0.01970927, 0.68764997, -1.71886428])
difatom8 = sp2_atoms_list[4] + hmol - breakatom8
difatom10 = sp2_atoms_list[4] + hmol*np.array([1, 1, -1]) - breakatom10

# Crear una lista de coordenadas para cada geometría parcial
partialgeoms = []

for i in range(n):
    partialgeom = []
    for j in range(44):
        # Lado derecho de la molécula
        if j == 8: # átomo b
            vec = (difvecatomslist[j]*(i+1)) + sp3_atoms_list[j]
            vec = vec/(magnitude(vec)/rCH)
            partialgeom.append(vec)
        elif j == 17: # átomo g
            vec = partialgeom[16] - partialgeom[8]
            partialgeom.append(vec)
        elif j == 7: # átomo a
            if rCH+(i+1)*(deltaRCH/n) > 1.13403:
                if firstrun == 2:
                    difatom8 /= (n-i)
                    iaux = 1
                    firstrun -= 1
                vec = breakatom8 + difatom8*(iaux)
                iaux += 1
            else:
                vec = (difvecatomslist[j]*(i+1)) + sp3_atoms_list[j]
                vec = vec/(magnitude(vec)/(rCH+(i+1)*(deltaRCH/n)))
            partialgeom.append(vec)
        # Se ajusta el átomo f después de que se haya calculado el átomo número 16 de la geometría parcial
        elif j == 9: # átomo f
            vec = np.array([0., 0., 0.])
            partialgeom.append(vec)
        elif j == 16: # átomo C2
            vec = (difvecatomslist[j]*(i+1)) + sp3_atoms_list[j]
            vec = vec/(magnitude(vec)/(rCC-(i+1)*(deltaRCC/n)))
            partialgeom.append(vec)
            # Se ajusta el átomo f
            if rCH+(i+1)*(deltaRCH/n) > 1.13403:
                if firstrun == 1:
                    difatom10 /= (n-i)
                    firstrun -= 1
                vec = breakatom10 + difatom10*(iaux-1)
            else: 
                vec = partialgeom[16] - partialgeom[7]
            partialgeom[9] += vec
            # partialgeom[9] += partialgeom[16] - partialgeom[7]
        elif j in moleculaCationica:
            # Se toma el átomo de C2(partialgeom[18]) como el nuevo origen
            vec = partialgeom[16] + moleculaCationica[j]
            partialgeom.append(vec)
        # Lado izquierdo de la molécula
        elif j == 11: # átomo b
            vec = (difvecatomslist[j]*(i+1)) + (sp3_atoms_list[j]-sp3_atoms_list[10])
            vec = vec/(magnitude(vec)/rCH)
            partialgeom.append(vec + sp3_atoms_list[10])
        elif j == 19: # átomo g
            vec = partialgeom[18] - partialgeom[11]
            partialgeom.append(vec + sp3_atoms_list[10])
        elif j == 12: # átomo a
            if rCH+(i+1)*(deltaRCH/n) > 1.13403:
                vec = partialgeom[7]*np.array([-1, 1, 1])
            else:
                vec = (difvecatomslist[j]*(i+1)) + (sp3_atoms_list[j]-sp3_atoms_list[10])
                vec = vec/(magnitude(vec)/(rCH+(i+1)*(deltaRCH/n)))
            partialgeom.append(vec + sp3_atoms_list[10])
        # Se ajusta el átomo f después de que se haya calculado el átomo número 16 de la geometría parcial
        elif j == 13: # átomo f
            vec = np.array([0., 0., 0.])
            partialgeom.append(vec + sp3_atoms_list[10])
        elif j == 18: # átomo C2
            vec = (difvecatomslist[j]*(i+1)) + (sp3_atoms_list[j]-sp3_atoms_list[10])
            vec = vec/(magnitude(vec)/(rCC-(i+1)*(deltaRCC/n)))
            partialgeom.append(vec + sp3_atoms_list[10])
            # Se ajusta el átomo f
            if rCH+(i+1)*(deltaRCH/n) > 1.13403:
                vec = partialgeom[9]*np.array([-1, 1, 1])
            else:
                vec = (partialgeom[18] - partialgeom[10]) - (partialgeom[12] - partialgeom[10]) 
            partialgeom[13] += vec
        elif j in moleculaCationicaLeft:
            # Se toma el átomo de C2(partialgeom[18]) como el nuevo origen
            vec = partialgeom[18] + moleculaCationicaLeft[j]
            partialgeom.append(vec)
        else:
            vec = (difvecatomslist[j]*(i+1)) + sp3_atoms_list[j]
            partialgeom.append(vec)
    # print(np.array(partialgeom)) 
    partialgeoms.append(partialgeom)

partialgeoms = np.array(partialgeoms)

# print(partialgeoms)

utils.generate_gjf(True, partialgeoms, n, 44, "template.gjf")