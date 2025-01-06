while True:
    try:
        print("Veuillez saisir une chaîne de caractères :")
        ma_chaine = input()

        if not ma_chaine.strip():  # Vérifie si la chaîne est vide ou contient uniquement des espaces
            raise ValueError("La chaîne ne peut pas être vide.")

        # Vérifie si la chaîne ne contient que des lettres et des espaces
        if not all(char.isalpha() or char.isspace() for char in ma_chaine):
            raise ValueError("La chaîne ne doit contenir que des lettres et des espaces.")

        print("Vous avez saisi :", ma_chaine)
        break  # Sort de la boucle si toutes les vérifications sont validées

    except ValueError as e:
        print(e)  # Affiche le message d'erreur et redemande une saisie

#definir les voyelles
voyelles = "AEIOUYaeiouy"

#compter les voyelles
nombre_voyelles = sum(1 for char in ma_chaine if char in voyelles)

print(nombre_voyelles)

