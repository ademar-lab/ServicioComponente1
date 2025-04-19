import numpy as np
import math as math
import utilities as utils

# Definir función de magnitud para tomar en cuenta el cambio de distancia entre átomos 
def magnitude(vector): 
    return math.sqrt(sum(pow(element, 2) for element in vector))

sp3_atoms_list = utils.parse_atom_coordinates("LI-7/sp3-coordinates.txt")
sp2_atoms_list = utils.parse_atom_coordinates("LI-7/sp2-coordinates.txt") 

print("Sp3")

for i in range(44):
    sp3_atoms_list[i] = sp3_atoms_list[i]-[-0.00004782, 0.49782449, 1.09904934]
    sp2_atoms_list[i] = sp2_atoms_list[i] - [0.00039556, 1.39654402, 0.00206175]
    print(sp3_atoms_list[i])

print("\nSp2")

for i in range(44):
    print(sp2_atoms_list[i])

sp3_atoms_list = np.array(sp3_atoms_list)

utils.generate_gjf(True, np.array([sp3_atoms_list]), 1, 44, "LI-7/template.gjf")

# # Valores iniciales de las variables de interés (SP3)
# # Distancia de enlace entre C-H
# rCH = 1.07
# # Distancia de enlace entre C-C
# rCC = 1.54
# # Ángulo que incrementará
# teta1 = 109.47122
# # Ángulo que disminuirá
# teta2 =109.47122

# # Valores finales de las variables de interés (SP2)
# # Se agrega un P(prima) para denotar que es el valor final
# # Distancia del doble enlace C=C
# rCCp = 1.3552
# # Ángulo que incrementó
# teta1p = 120
# # Ángulo que disminuyó
# teta2p = 0

# # Diferencias entre SP3 y SP2
# deltaRCC = abs(rCCp-rCC)
# # Diferencia entre los átomos de hidrógeno que entran y C
# deltaRCH = abs(rCCp-rCH)
# # Diferencia del ángulo que incrementó
# deltaT1 = abs(teta1p-teta1)
# # Diferencia del anguló que disminuyó
# deltaT2 = abs(teta2p-teta2)

# # Calcular los vectores difereranciales (solo incluye cambio de ángulos)
# difvecatomslist = []
# for i in range(44):
#     difvecatomslist.append(sp2_atoms_list[i]-sp3_atoms_list[i])
#     print(difvecatomslist[i])
# difvecatomslist = np.array(difvecatomslist)

# # Comenzar el algoritmo
# print("\nESTE PROGRAMA ANALIZARÁ LA GEOMETRÍA DE LA HIBRIDACIÓN SP2 A SP3 DE UNA MOLÉCULA LI-7 en el vacío.\nLA SALIDA SERÁ UNA LISTA DE LAS COORDENADAS DE LOS ÁTOMOS EN LOS MOMENTOS DURANTE LA HIBRIDACIÓN SIN CONTAR C1(ORIGEN).")
# print("_" * 100)

# n = int(input("\nCual es la cantidad de geometrias graduales que deseas? ")) + 1

# # Crear una lista de los valores parciales para cada variable
# difvecatomslist = difvecatomslist/n
# # print("\ndifvectatomslist/n:\n")
# # for i in range(7):
# #     print(difvecatomslist[i])
# # print("\ninitialatomslist:\n")
# # for i in range(7):
# #     print(iniatialatomslist[i])

# # Crear una lista de vectores para cada átomo de cada geometría parcial
# partialgeoms = []
# for i in range(n):
#     print("\n")
#     partialgeom = []
#     for j in range(7):
#         #Se multiplica el vector por una variable aux que ajustará su magnitud a la apropiada 
#         # #Se ajusta el vector a
#         if j == 0:
#             vec = np.array(iniatialatomslist[j] + (i+1)*difvecatomslist[j])
#             vec = vec * (rCH+(i+1)*(deltaRCH/n))/magnitude(vec)
#             print(magnitude(vec))
#             partialgeom.append(vec)
#         # #Se ajusta el vector b
#         if j == 1:
#             vec = np.array(iniatialatomslist[j] + (i+1)*difvecatomslist[j])
#             vec = vec * (rCH/magnitude(vec))
#             print(magnitude(vec))
#             partialgeom.append(vec)
#         # Se ajusta el vector c
#         if j == 3:
#             partialgeom.append(np.array(iniatialatomslist[j] + (i+1)*difvecatomslist[j]))
#         # Se ajusta el vector d
#         if j == 2:
#             # print("d or e")
#             vec = np.array(iniatialatomslist[j] + (i+1)*difvecatomslist[j])
#             vec = vec * (rCH/magnitude(vec))
#             print(magnitude(vec))
#             partialgeom.append(vec)
#         # vector e
#         if j == 4:
#             vec = -1*partialgeom[2] + partialgeom[3]
#             partialgeom.append(np.array(vec))
#         # vector f
#         if j == 5:
#             vec = -1*partialgeom[0] + partialgeom[3]
#             partialgeom.append(np.array(vec))
#         # vector g
#         if j == 6:
#             vec = -1*partialgeom[1] + partialgeom[3]
#             partialgeom.append(np.array(vec))
#     partialgeoms.append(partialgeom)
# # print(magnitude(partialgeoms[0][0][0]))

# partialgeoms = np.array(partialgeoms)
# # for x in partialgeoms[2,5,0]:
# #     print(x)

# print(partialgeoms)