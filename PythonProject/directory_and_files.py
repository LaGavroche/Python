import os
import pathlib
from os import mkdir, getcwd
import csv
import json
dicEleves = {
	'titi' : {'notes':{'tp1':10, 'tp2':13,'tp3':17}, 'appréciation': 'moyenne' },
	'toto' : {'notes':{'tp1':19, 'tp2':11,'tp3':14}, 'appréciation': 'Très Bien' },
	'tata' : {'notes':{'tp1':15,'tp2':8,'tp3':13}, 'appréciation': 'Bonne' },
	'tutu' : {'notes':{'tp3':15,'tp4':13}, 'appréciation': 'Bonne' },
}


# utilisation de la bibliothèque pathlib
myFolderpath=pathlib.Path(__file__).parent.resolve()	# on récupère le chemin du programme
os.chdir(myFolderpath)			# on se positionne dans le dossier
os.path.exists("eleves")		# test si le fichier existe si non, le crée
if not os.path.exists("eleves"):
	os.mkdir("eleves")
	os.chdir("eleves")

# Parcours de chaque élève dans dicEleves
for eleve, data in dicEleves.items():
	# Création d'un dossier pour chaque élève
	eleve_folder = os.path.join("eleves", eleve)
	if not os.path.exists(eleve_folder):
		os.mkdir(eleve_folder)

	# Création du fichier appréciation.txt pour chaque élève
	with open(os.path.join(eleve_folder, 'appréciation.txt'), 'w') as appreciation_file:
		appreciation_file.write(f"{eleve}: {data['appréciation']}\n")

	# Création du fichier notes.csv pour chaque élève
	with open(os.path.join(eleve_folder, 'notes.csv'), 'w', newline='') as notes_file:
		writer = csv.writer(notes_file)
		# Écriture de l'en-tête
		writer.writerow(['TP', 'Note'])

		# Écriture des notes pour cet élève
		for tp, note in data['notes'].items():
			writer.writerow([tp, note])

# Fonction pour calculer la moyenne, la note minimale et maximale
def calculer_statistiques(notes):
    moyenne = sum(notes) / len(notes) if notes else 0
    min_note = min(notes) if notes else 0
    max_note = max(notes) if notes else 0
    return {'moyenne': moyenne, 'min': min_note, 'max': max_note}

# Créer le dossier 'eleves' si il n'existe pas déjà
if not os.path.exists("eleves"):
    os.mkdir("eleves")

# Dictionnaire pour stocker les résultats
resultats = {}

# Calculer les statistiques pour chaque élève
for eleve, data in dicEleves.items():
    # On récupère les notes de l'élève
    notes = list(data['notes'].values())
    # Calcul des statistiques (moyenne, min, max)
    statistiques = calculer_statistiques(notes)
    resultats[eleve] = statistiques


# Fonction pour calculer la moyenne, la note minimale et maximale
def calculer_statistiques(notes):
	moyenne = sum(notes) / len(notes) if notes else 0
	min_note = min(notes) if notes else 0
	max_note = max(notes) if notes else 0
	return {'moyenne': moyenne, 'min': min_note, 'max': max_note}


# Créer le dossier 'eleves' si il n'existe pas déjà
if not os.path.exists("eleves"):
	os.mkdir("eleves")

# Parcours de chaque élève dans dicEleves
for eleve, data in dicEleves.items():
	# Création du dossier pour l'élève s'il n'existe pas
	eleve_folder = os.path.join("eleves", eleve)
	if not os.path.exists(eleve_folder):
		os.mkdir(eleve_folder)

	# On récupère les notes de l'élève
	notes = list(data['notes'].values())
	# Calcul des statistiques (moyenne, min, max)
	statistiques = calculer_statistiques(notes)

	# Création du fichier JSON pour cet élève dans son dossier
	with open(os.path.join(eleve_folder, f"{eleve}.json"), 'w') as json_file:
		json.dump(statistiques, json_file, indent=4)

