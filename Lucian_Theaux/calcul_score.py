# Lucian Théaux

import turtle as tt

def ajout_score(score:int,mot:str):
    """
    ajout_score: Écrit dans le fichier scores.txt le score donné en entrée
    - score: Prend en entrée un integer
    """
    with open('scores.txt', 'a', encoding='utf-8') as F:                    # Ouvre le fichier en mode ajout
        F.write(f'{score};{mot}\n')                                         # Écrit le score et le mot dans le fichier

def scoreboard(length:int):
    """
    scoreboard: Récupère tous les scores du fichier texte scores.txt pour créer un scoreboard length score du meilleur au plus petit
    - length: Prend en entrée un integer
    """
    scoreboard_dict = {}                                                        # Dictionnaire vide pour stocker les scores
    with open('scores.txt', 'r', encoding='utf-8') as F:                        # Ouvre le fichier en mode lecture
        scoreboard_list = F.read().split('\n')                                   # Lit le fichier et sépare les lignes en une liste
    print(scoreboard_list)                                                      # Liste des scores lus dans le fichier       
    for elem in scoreboard_list:                                             # Parcourt chaque élément de la liste 
        if elem == '':                                                      # Si l'élément est une chaîne vide, on:
            continue
        value,key = elem.split(';')                                         # Sépare l'élément en score (value) et mot (key)
        scoreboard_dict[key] = int(value)                                   # Ajoute le score et le mot au dictionnaire
    scoreboard_dict = dict(sorted(scoreboard_dict.items(), key= lambda item: item[1]))  # Trie le dictionnaire par score croissant
    print(scoreboard_dict)
    tt.fillcolor('white')
    tt.penup()
    tt.goto(230, -300)                                                      # Position du tableau                                                   
    tt.setheading(0)                                                        # Orientation de la tortue      
    tt.write('CLASSEMENT', font=('Minecraft',30, 'bold'))                   # Titre du tableau
    tt.seth(270)
    tt.fd(30)                                                               # Espace entre le titre et les scores 
    i = 0
    if len(list(scoreboard_dict)) < length:                                 # Si le nombre de scores est inférieur à length, on affiche tous les scores disponibles
        for i in range(1,len(list(scoreboard_dict))+1):                     # On affiche tous les scores disponibles
            key = list(scoreboard_dict)[-i]                                 # Récupère la clé (mot) du i-ème score le plus élevé
            value = list(scoreboard_dict.values())[-i]                      # Récupère la valeur (score) du i-ème score le plus élevé
            if i == 1:                                                      # Si c'est le meilleur score:
                tt.color("#D1A90F")                                                  # Couleur spéciale pour le meilleur score
                tt.write(f'{value} ☞ {key}', font=('Minecraft',20, 'italic'))          # Affiche le score et le mot
                tt.color('black')
                tt.fd(30)
            else:                                                           # Pour les autres scores:
                tt.write(f'{value} ☞ {key}', font=('Minecraft',20, 'italic'))          # Affiche le score et le mot en noir simple
                tt.fd(30)
            i+= 1
    else:

        for i in range(1,length+1):                                         # Sinon, on affiche seulement les length des meilleurs scores                                    
            key = list(scoreboard_dict)[-i]                                 # Récupère la clé (mot) du i-ème score le plus élevé
            value = list(scoreboard_dict.values())[-i]                      # Récupère la valeur (score) du i-ème score le plus élevé
            if i == 1:                                                      # Si c'est le meilleur score:
                tt.color("#D1A90F")                                         # Couleur spéciale pour le meilleur score   
                tt.write(f'{value} ☞ {key}', font=('Minecraft',20, 'italic'))        # Affiche le score et le mot
                tt.color('black')
                tt.fd(30)   
            else:                                                               # Pour les autres scores:
                tt.write(f'{value} ☞ {key}', font=('Minecraft',20, 'italic'))      # Affiche le score et le mot en noir simple
                tt.fd(30)
            i+= 1
        