import os
import argparse
import shutil # Ajouté pour l'option --clean

# Définition de la structure de cours par défaut, sans le répertoire racine
DEFAULT_COURSE_STRUCTURE = {
    'maths': ['project_1'],
    'truc': ['project_1', 'project_2']
}

parser = argparse.ArgumentParser(description="Crée une arborescence de dossiers et de fichiers pour des cours.")
parser.add_argument('--root_dir', type=str, default='.',
                    help='Répertoire racine où créer l\'arborescence (par défaut: .).')
args = parser.parse_args()

courses_to_create = DEFAULT_COURSE_STRUCTURE

# Construire la structure finale des répertoires avec le root_dir
final_directory_structure_paths = {}
for main_dir_name, sub_dirs_list in courses_to_create.items():
    actual_main_dir_path = os.path.join(args.root_dir, main_dir_name)
    final_directory_structure_paths[actual_main_dir_path] = sub_dirs_list

# Créer les répertoires et y ajouter des fichiers
for main_dir_path, sub_dirs in final_directory_structure_paths.items():
    os.makedirs(main_dir_path, exist_ok=True)
    print(f"Répertoire principal créé : {main_dir_path}/")
    for sub_dir in sub_dirs:
        path = os.path.join(main_dir_path, sub_dir)
        os.makedirs(path, exist_ok=True)
        print(f"  Sous-répertoire créé : {path}/")

        with open(os.path.join(path, 'README.md'), 'w') as f: f.write('Informations sur le projet..')
        with open(os.path.join(path, f'cours_{1}.txt'), 'w') as f: f.write('Résumé du cours.\nLigne 2 du cours.\nLigne 3 du cours.')

print("\nArborescence de dossiers et fichiers créée avec succès.")
