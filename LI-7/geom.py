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
    sp3_atoms_list[i] = sp3_atoms_list[i]-[-0.00004782, 0.49782449, 1.09904934]

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
    sp2_atoms_list[i] = sp2_atoms_list[i]-[0.00039556, 1.39654402, 0.00206175]

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

# # Crear una lista de vectores para cada átomo de cada geometría parcial
# partialgeoms = []
# for i in range(n):
#     partialgeom = []
#     for j in range(44):
#         if j == 8: # átomo a
#             vec = (difvecatomslist[j]*(i+1)) + sp3_atoms_list[j]
#             vec = vec * (rCH+(i+1)*(deltaRCH/n))/magnitude(vec)
#             np.append(partialgeom, vec)
#         elif j == 9: # átomo b
#             vec = (difvecatomslist[j]*(i+1)) + sp3_atoms_list[j]
#             vec =  vec * (rCH/magnitude(vec))
#             np.append(partialgeom, vec)
#         elif j == 7: # átomo c
#             partialgeom.append((difvecatomslist[j]*(i+1)) + sp3_atoms_list[j])
#             np.append(partialgeom, vec)
#         elif j == 15: # átomo d
#             vec = np.array(sp3_atoms_list[j] + (i+1)*difvecatomslist[j])
#             vec = vec * (rCH/magnitude(vec))
#             np.append(partialgeom, vec)
#         # elif j == 21: # átomo e
#         #     vec = -1*partialgeom[2] + partialgeom[3]
#         #     partialgeom.append(vec)
#         # elif j == 10: # átomo f
#         #     vec = -1*partialgeom[0] + partialgeom[3]
#         #     partialgeom.append(vec)
#         # elif j == 11: # átomo g
#         #     vec = -1*partialgeom[0] + partialgeom[3]
#         #     partialgeom.append(vec)
#         # elif j == 12: # átomo h
#         #     vec = -1*partialgeom[1] + partialgeom[3]
#         #     partialgeom.append(vec)}
#         else:
#             vec = (difvecatomslist[j]*(i+1)) + sp3_atoms_list[j]
#             np.append(partialgeom, vec)

#     partialgeoms.append(partialgeom)

# partialgeoms = np.array(partialgeoms)

# print(partialgeoms)

partialgeoms = []

for i in range(n):
    partialgeoms.append(difvecatomslist*(i+1) + sp3_atoms_list)

print(np.array(partialgeoms))

utils.generate_gjf(True, np.array(partialgeoms), n, 44, "template.gjf")