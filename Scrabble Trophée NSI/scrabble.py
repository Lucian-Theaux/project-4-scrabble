plateau = []
continuer = True

def creation_plateau():
    global plateau
    plateau = [['' for i in range(15)] for i in range(15)]

creation_plateau()

def ajout_mot_horizontal(x:int,y:int,mot:str):
    global plateau
    i = 0
    for lettre in mot:
        plateau[y][x+i] = lettre.capitalize()
        i += 1

def ajout_mot_vertical(x:int,y:int,mot:str):
    global plateau
    i = 0
    for lettre in mot:
        plateau[y+i][x] = lettre.capitalize()
        i += 1

def position_clique_sur_matrice(x:int,y:int) -> list:
    position_x = x//40
    position_y = y//40
    return [position_x,position_y]

print(position_clique_sur_matrice(350,20))

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
