import os
import json

import pathlib											# utilisation de la bibliothèque pathlib
myFolderpath= pathlib.Path(__file__).parent.resolve()	# on récupère le chemin du programme
os.chdir(myFolderpath)									# on se positionne dans le bon dossier

dicBoissons = {}
if not os.path.exists('dicboissons.json'):
	# on déclare le dictionnaire des élèves
	dicBoissons = { 
		'cafe noir' : {"numero" : 1, "prix":15}, 
		'cafe au lait' : {"numero" : 2, "prix":25}, 
		'the' : {"numero" : 3, "prix":20},
		'chocolat au lait' : {"numero" : 4, "prix":35},
		'cappucino' : {"numero" : 5, "prix":40}, 
		'cafe long' : {"numero" : 6, "prix":20}, 
	}
else :
	# pour recharger le dictionnaire
	with open('dicboissons.json', 'r') as file:
		dicBoissons =  json.load(file)

dicPieces = {}
if os.path.exists('listpiece.csv'):
	# on ouvre le fichier en mode lecture
	with open('listpiece.csv', 'r') as file:
		# 5;10
		# 10;10
		# 20;10
		# 50;10
		# lecture des lignes du fichier
		for line in file:
			# on supprime le caractère de fin de ligne
			line = line.strip()
			# on récupère les données de la ligne
			piece, nombre = line.split(';')
			# on ajoute la pièce au dictionnaire
			dicPieces[int(piece)] = int(nombre)
else:
	dicPieces = {
		50 : 10,
		20 : 10,
		10 : 10,
		5 : 10
	}

# on déclare le dictionnaire des ventes
dicVentes = {}
while True:
	print ('Choisir votre boisson :')
	for boisson in dicBoissons:
		print (dicBoissons[boisson]['numero'], boisson, ":", dicBoissons[boisson]['prix'], "€")
	print (0, "Annuler")
	choix = input("Votre choix :")

	if choix > "0":
		# on récupère le nom de la boisson
		for tmpboisson in dicBoissons:
			if dicBoissons[tmpboisson]['numero'] == int(choix):
				boisson = tmpboisson
				break
		# alternative plus complexe mais plus rapide
		# boisson = list(dicBoissons.keys())[int(choix)-1]
		# on récupère le prix de la boisson
		prix = dicBoissons[boisson]['prix']

		# on ajoute le la boissons aux ventes
		if boisson in dicVentes:
			dicVentes[boisson] += 1
		else:
			dicVentes[boisson] = 1

		# on demande le montant à l'utilisateur
		montantSaisie = 0
		while True:
			montant = input("Montant " + str(prix) + " Insérer votre monnaie :")
			# on ajoute la pièce au dictionnaire
			dicPieces[int(montant)] +=1
			montantSaisie = montantSaisie + int(montant)
			if montantSaisie >= prix:
				break
		
		# on calcule la monnaie à rendre
		monnaie = int(montantSaisie) - prix
		print ( "-" * 10)
		print ("Monnaie à rendre :", monnaie)
		while True:
			if monnaie >= 50 and dicPieces[50] > 0:
				print ('\tune piece de 50 centimes')
				monnaie = monnaie - 50
				dicPieces[50] -=1
			elif monnaie >= 20 and dicPieces[20] > 0:
				print ('\tune piece de 20 centimes')
				monnaie = monnaie - 20
				dicPieces[20] -=1
			elif monnaie >= 10 and dicPieces[10] > 0:
				print ('\tune piece de 10 centimes')
				monnaie = monnaie - 10
				dicPieces[10] -=1
			elif monnaie >= 5 and dicPieces[5] > 0:
				print ('\tune piece de 5 centimes')
				monnaie = monnaie - 5
				dicPieces[5] -=1
				
			if monnaie == 0:
				break
			
			# gestion de l'absence de monnaie
			if monnaie == 5 and dicPieces[5] == 0:
				# on ne peut plus rendre la monnaie
				print ("Plus de monnaie à rendre")
				break

		# on affiche la boisson
		print ("Voici votre boisson :", boisson)
		print ( "=" * 20)
	elif choix == "-1":
		print ( "-" * 10)
		print ("Monnaie dans la machine :")
		for piece in dicPieces:
			print (piece, "centimes :", dicPieces[piece])
	elif choix == "-2":
		print ( "-" * 10)
		print ("Liste des Ventes :")
		# on affiche les ventes et le prix total
		for boisson in dicVentes:
			print (boisson, ":", dicVentes[boisson], dicBoissons[boisson]['prix'] * dicVentes[boisson], "€")

	else:
		break