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