
def creation_plateau():
    return [['' for i in range(15)] for i in range(15)]

def ajout_mot_horizontal(x:int,y:int,mot:str,plateau:list):
    i = 0
    for lettre in mot:
        plateau[y][x+i] = lettre.capitalize()
        i += 1

def ajout_mot_vertical(x:int,y:int,mot:str,plateau:list):
    i = 0
    for lettre in mot:
        plateau[y+i][x] = lettre.capitalize()
        i += 1

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

