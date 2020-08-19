class Atom:
  def __init__(self, label):
    self.label = label
  def __add__(self, other):
    return Molecule([self.label, other.label])
    
class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms
 
      
sodium = Atom("Na")
chlorine = Atom("Cl")
print(sodium.label)
print(chlorine.label)

salt = sodium + chlorine
print(str(salt.atoms))