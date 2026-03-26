
def creation_plateau():  # Crée un plateau vide 15x15
    return [['' for i in range(15)] for i in range(15)]  # Liste de listes vides

def ajout_mot_horizontal(x:int,y:int,mot:str,plateau:list):  # Ajoute un mot horizontalement
    i = 0  # Index de la lettre
    for lettre in mot:  # Pour chaque lettre du mot
        plateau[y][x+i] = lettre.capitalize()  # Placer la lettre en majuscule sur le plateau
        i += 1  # Passer à la colonne suivante

def ajout_mot_vertical(x:int,y:int,mot:str,plateau:list):  # Ajoute un mot verticalement
    i = 0  # Index de la lettre
    for lettre in mot:  # Pour chaque lettre du mot
        plateau[y+i][x] = lettre.capitalize()  # Placer la lettre en majuscule verticalement
        i += 1  # Passer à la ligne suivante

# while continuer:
#     ask = input('Mot [Vide si arrêter] : ')

#     if ask == '':
#         continuer = False
#         break

#     orientation = input('Horizontal -> 1 | Vertical -> 2 : ')
#     coordonnees_x = int(input('x : '))
#     coordonnees_y = int(input('y : '))

#     print(coordonnees_x)

#     if orientation == 1:
#         ajout_mot_horizontal(coordonnees_x,coordonnees_y,ask)
#     else:
#         ajout_mot_vertical(coordonnees_x,coordonnees_y,ask)

#     for liste in plateau:
#         print(liste)
