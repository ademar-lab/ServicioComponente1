import numpy as np
 
def parse_atom_coordinates(file_path):
    """
    Reads a text file containing atom coordinates and returns them as a list of numpy arrays.
    Args:
        file_path (str): Path to the text file containing atom coordinates
    Returns:
        list: List of numpy arrays, each containing [x, y, z] coordinates for an atom
    """
    atoms = []
    with open(file_path, 'r') as file:
        for line in file:
            # Skip empty lines
            if not line.strip():
                continue
            # Split the line into components
            parts = line.split()
            # The first part is the atom type, the rest are coordinates
            if len(parts) >= 4:  # Ensure we have atom type + x,y,z coordinates
                try:
                    # Convert string coordinates to floats
                    coords = np.array([float(parts[1]), float(parts[2]), float(parts[3])])
                    atoms.append(coords)
                except (ValueError, IndexError):
                    # Skip lines that don't have valid coordinates
                    continue
    return atoms
 
# Example usage:
# atom_list = parse_atom_coordinates('your_file.txt')
# print(atom_list[0])  # Prints first atom's coordinates as numpy array

def generate_gjf(flag, final_atom_list, num_geoms, num_atoms, template_file_path):
    """
    Generar un documento .gjf para cada lista de átomos que sea proporcionadas.

    Args: 
        flag (bool): Indica si se debe crear un archivo .gjf o no.
        final_atom_list (list): Lista de listas de átomos, cada lista contiene una geometría parcial.
        num_geoms (int): Número de geometrías parciales.
        num_atoms (int): Número de átomos en cada molécula.
        template_file_path (str): Ruta al archivo plantilla .gjf que se utilizará para crear los nuevos archivos.
    """

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
        for n in range(num_geoms):
            # Insertar las coordenadas en la plantilla .gjf
            with open(template_file_path, 'r') as file:
                template = file.read()
                # Número de átomos
                for x in range(num_atoms):
                    # Número de demensiones para el vector del átomo
                    for y in range(3):
                        template = template.replace(f" {x+1}[n][{y}]", f" {final_atom_list[n,x,y]}")

            new_file_path = f"{n+1}geom.gjf"

            with open(new_file_path, 'w') as file:
                file.write(template)
        
        print(f"File '{new_file_path}' created successfully.")

# Example usage:
# generate_gjf(True, [sp3-coordinates.txt], 1, 44, "template.gjf")