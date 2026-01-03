import os
import glob
import re

# === CONFIGURATION ===
BASE_DIR = "BassingaLib"
OLD_PATH = "/home/andresse/Documents/My_projects/Reference-Design"
NEW_PATH = "${KIPRJMOD}"

print("=== SCRIPT DE REMPLACEMENT DE CHEMINS ===\n")
print(f"Remplacement de: {OLD_PATH}")
print(f"Par: {NEW_PATH}\n")

# 1. Trouver tous les répertoires .pretty
pretty_dirs = glob.glob(os.path.join(BASE_DIR, "**", "*.pretty"), recursive=True)
print(f"1. Trouvé {len(pretty_dirs)} répertoires .pretty\n")

# Compteurs
total_files = 0
modified_files = 0
total_replacements = 0

# 2. Parcourir chaque répertoire .pretty
for pretty_dir in sorted(pretty_dirs):
    rel_path = os.path.relpath(pretty_dir)
    
    # Trouver tous les fichiers .kicad_mod
    mod_files = glob.glob(os.path.join(pretty_dir, "*.kicad_mod"))
    
    for mod_file in mod_files:
        total_files += 1
        
        # Lire le contenu
        with open(mod_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Compter les occurrences avant remplacement
        occurrences = content.count(OLD_PATH)
        
        if occurrences > 0:
            # Remplacer le chemin absolu par le chemin relatif
            new_content = content.replace(OLD_PATH, NEW_PATH)
            
            # Écrire le fichier modifié
            with open(mod_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            modified_files += 1
            total_replacements += occurrences
            
            print(f"✓ Modifié: {os.path.relpath(mod_file)}")
            print(f"  Remplacements: {occurrences}")

print(f"\n=== RÉSUMÉ ===")
print(f"Fichiers analysés: {total_files}")
print(f"Fichiers modifiés: {modified_files}")
print(f"Remplacements totaux: {total_replacements}")

if modified_files > 0:
    print(f"\n✓ Modification terminée avec succès!")
    print(f"  {OLD_PATH}")
    print(f"  → {NEW_PATH}")
else:
    print(f"\n⚠ Aucun fichier n'a été modifié.")
    print(f"  Le chemin '{OLD_PATH}' n'a pas été trouvé dans les fichiers.")
