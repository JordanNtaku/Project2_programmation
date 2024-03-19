# -*- coding: utf-8 -*-

def lire_csv(nom_fichier):
    contacts = []
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()
        for ligne in lignes:
            contact = ligne.strip().split(',')
            contacts.append(contact)
    return contacts

def ecrire_csv(nom_fichier, contacts):
    with open(nom_fichier, 'w') as fichier:
        for contact in contacts:
            ligne = ','.join(contact) + '\n'
            fichier.write(ligne)

def afficher_menu():
    print("\nMenu du programme:")
    print("1. Filtrer les données météo pour une ville donnée")
    print("2. Filtrer les données météo d'une ville pour une période donnée")
    print("3. Déterminer la température maximale et minimale d'une ville")
    print("4. Calculer la température moyenne d'une ville")
    print("5. Quitter")

def filtrer_ville(donnees, ville):
    for enregistrement in donnees:
        if enregistrement[1] == ville:
            print(enregistrement)

def filtrer_entre_dates(donnees, date_debut, date_fin):
    for enregistrement in donnees:
        if date_debut <= enregistrement[0] <= date_fin:
            print(enregistrement)

def max_min_temperature_ville(donnees, ville):
    max_temp = float('-inf')
    min_temp = float('inf')
    for enregistrement in donnees:
        if enregistrement[1] == ville:
            max_temp = max(max_temp, enregistrement[2])
            min_temp = min(min_temp, enregistrement[3])
    print(f"Température maximale à {ville}: {max_temp}")
    print(f"Température minimale à {ville}: {min_temp}")

def moyenne_temperature_ville(donnees, ville):
    total_temp = 0
    count = 0
    for enregistrement in donnees:
        if enregistrement[1] == ville:
            total_temp += (enregistrement[2] + enregistrement[3]) / 2
            count += 1
    moyenne = total_temp / count if count != 0 else 0
    print(f"Température moyenne à {ville}: {moyenne}")

def main():
    donnees_meteo = [
        ['2024-01-01', 'Paris', 5, 9, 15],
        ['2024-01-02', 'Paris', 19, 5, 14],
        ['2024-01-03', 'Paris', 7, -5, 13],
        ['2024-01-04', 'Paris', 22, 5, 15],
        ['2024-01-05', 'Paris', 2, 2, 20],
        ['2024-01-06', 'Paris', -1, -2, 20],
        ['2024-01-07', 'Paris', 5, 6, 15],
        ['2024-01-08', 'Paris', 4, -4, 9],
        ['2024-01-09', 'Paris', 5, 5, 3],
        ['2024-01-10', 'Paris', 31, 30, 17],
        ['2024-01-01', 'Lyon', 32, 5, 8],
        ['2024-01-02', 'Lyon', 0, -2, 20],
        ['2024-01-03', 'Lyon', 22, 4, 1],
        ['2024-01-04', 'Lyon', 26, -10, 8],
        ['2024-01-05', 'Lyon', 16, 7, 6],
        ['2024-01-06', 'Lyon', 11, 2, 11],
        ['2024-01-07', 'Lyon', 10, 23, 20],
        ['2024-01-08', 'Lyon', 3, 7, 8],
        ['2024-01-09', 'Lyon', 34, 24, 17],
        ['2024-01-10', 'Lyon', -3, 25, 11]
    ]

    while True:
        afficher_menu()
        choix = input("Entrez votre choix (1-5): ")

        if choix == '1':
            ville = input("Entrez le nom de la ville : ")
            filtrer_ville(donnees_meteo, ville)
        elif choix == '2':
            date_debut = input("Entrez la date de début (YYYY-MM-DD) : ")
            date_fin = input("Entrez la date de fin (YYYY-MM-DD) : ")
            filtrer_entre_dates(donnees_meteo, date_debut, date_fin)
        elif choix == '3':
            ville = input("Entrez le nom de la ville : ")
            max_min_temperature_ville(donnees_meteo, ville)
        elif choix == '4':
            ville = input("Entrez le nom de la ville : ")
            moyenne_temperature_ville(donnees_meteo, ville)
        elif choix == '5':
            print("Fin du programme.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
