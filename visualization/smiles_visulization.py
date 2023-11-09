from rdkit import Chem
from rdkit.Chem import Draw

# SMILES string

def visualise(smiles: str):

  # Create an RDKit molecule from the SMILES string
  mol = Chem.MolFromSmiles(smiles)
  
  # Generate a 2D depiction of the molecule
  img = Draw.MolToImage(mol)
  
  smiles_clean = smiles.replace("/", "")
  
  path_to_save = "./resources/" + smiles_clean + ".png"
 
  img.save(path_to_save, "PNG")
  return path_to_save
