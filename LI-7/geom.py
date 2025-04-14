import utilities as utils

atoms_list = utils.parse_atom_coordinates("LI-7/sp3-coordinates.txt")
sp2_atoms_list = utils.parse_atom_coordinates("LI-7/sp2-coordinates.txt") 

for i in atoms_list:
    print(f"{i}\n")
print(f"{len(atoms_list)}")

for i in sp2_atoms_list:
    print(f"{i}\n")
print(f"{len(sp2_atoms_list)}")
