#cette page contient toutes les vérifications: 
# #vérification que deux mots ne se chevauchent pas,
# #vérification que deux mots côte à côte forment un mot existant
import os 

def verification_place(matrice,y,x, direction,mot):
    if direction == "horizontal" : #horizontal
        for i in range(len(mot)):
            if matrice[y][x+i] != "" and matrice[y][x+i]!= mot[i] :
                return f"changez vos coordonnées, la case {y} {x+i} est déjà prise"
    elif direction == "vertical" : #vertical
        for i in range(len(mot)):
            if matrice[y+i][x] != "" and matrice[y+i][x] != mot[i]:
                return f"changez vos coordonnées, la case {y+i} {x} est déjà prise "
    return True


def verification_mot_horizontal(plateau,y,x,mot):
    dossier = os.path.dirname(__file__)
    chemin_fichier = os.path.join(dossier, "mots_autorises.txt")

    with open(chemin_fichier,'r', encoding='utf-8') as fichier:
        mots_valides = set(ligne.strip() for ligne in fichier)

    # gauche
    if x > 0 and plateau[y][x-1] != "":
        nouv_motA=[plateau[y][x-1] + mot]
        verif_boucle = False
        n = 1
        while not verif_boucle:
            n += 1
            if x-n >= 0 and plateau[y][x-n] != "":
                nouv_motA = [plateau[y][x-n]] + nouv_motA
            else:
                verif_boucle = True

        nouv_motA = "".join(nouv_motA)

        if nouv_motA not in mots_valides:
            return False

    # droite
    if x + len(mot) < len(plateau) and plateau[y][x + len(mot)] != "":
        nouv_motB=[mot + plateau[y][x + len(mot)]]
        verif_boucle = False
        n = 1
        while not verif_boucle:
            n += 1
            if x+n < len(plateau) and plateau[y][x+n] != "":
                nouv_motB = nouv_motB + [plateau[y][x+n]]
            else:
                verif_boucle = True

        nouv_motB="".join(nouv_motB)

        if nouv_motB not in mots_valides:
            return False

    # vertical
    for i in range(len(mot)):
        col = x+i

        if y > 0 and plateau[y-1][col] != "":
            nouv_mot1=[plateau[y-1][col],mot[i]]
            verif_boucle = False
            n = 1
            while not verif_boucle:
                n += 1
                if y-n >= 0 and plateau[y-n][col] != "":
                    nouv_mot1 =[plateau[y-n][col]] + nouv_mot1 
                else:
                    verif_boucle = True

            nouv_mot1="".join(nouv_mot1)

            if nouv_mot1 not in mots_valides:
                return False

        elif y+1 < len(plateau) and plateau[y+1][col] != "":
            nouv_mot2=[mot[i],plateau[y+1][col]]
            verif_boucle = False
            n = 1
            while not verif_boucle:
                n += 1
                if y+n < len(plateau) and plateau[y+n][col] != "":
                    nouv_mot2 = nouv_mot2 + [plateau[y+n][col]] 
                else:
                    verif_boucle = True

            nouv_mot2 = "".join(nouv_mot2)

            if nouv_mot2 not in mots_valides:
                return False

    return True
                

def verification_mot_vertical(plateau, y, x, mot):
    import os
    dossier = os.path.dirname(__file__)
    chemin_fichier = os.path.join(dossier, "mots_autorises.txt")

    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        mots_valides = set(ligne.strip() for ligne in fichier)

    # haut
    if y > 0 and plateau[y-1][x] != "":
        nouv_motC = [plateau[y-1][x]] + list(mot)
        verif_boucle = False
        n = 1
        while not verif_boucle:
            n += 1
            if y-n >= 0 and plateau[y-n][x] != "":
                nouv_motC = [plateau[y-n][x]] + nouv_motC
            else:
                verif_boucle = True

        nouv_motC = "".join(nouv_motC)
        if nouv_motC not in mots_valides:
            return False

    # bas
    if y + len(mot) < len(plateau) and plateau[y + len(mot)][x] != "":
        nouv_motD = list(mot) + [plateau[y + len(mot)][x]]
        verif_boucle = False
        n = 1
        while not verif_boucle:
            n += 1
            if y+n < len(plateau) and plateau[y+n][x] != "":
                nouv_motD = nouv_motD + [plateau[y+n][x]]
            else:
                verif_boucle = True

        nouv_motD = "".join(nouv_motD)
        if nouv_motD not in mots_valides:
            return False

    # horizontal pour chaque lettre du mot
    for i in range(len(mot)):
        row = y + i

        if x > 0 and plateau[row][x-1] != "":
            nouv_mot3 = [plateau[row][x-1], mot[i]]
            verif_boucle = False
            n = 1
            while not verif_boucle:
                n += 1
                if x-n >= 0 and plateau[row][x-n] != "":
                    nouv_mot3 = [plateau[row][x-n]] + nouv_mot3
                else:
                    verif_boucle = True

            nouv_mot3 = "".join(nouv_mot3)
            if nouv_mot3 not in mots_valides:
                return False

        elif x + 1 < len(plateau[0]) and plateau[row][x+1] != "":
            nouv_mot4 = [mot[i], plateau[row][x+1]]
            verif_boucle = False
            n = 1
            while not verif_boucle:
                n += 1
                if x+n < len(plateau[0]) and plateau[row][x+n] != "":
                    nouv_mot4 = nouv_mot4 + [plateau[row][x+n]]
                else:
                    verif_boucle = True

            nouv_mot4 = "".join(nouv_mot4)
            if nouv_mot4 not in mots_valides:
                return False

    return True