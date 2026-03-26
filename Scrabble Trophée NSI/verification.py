#cette page contient toutes les vérifications: 
# #vérification que deux mots ne se chevauchent pas,
# #vérification que deux mots côte à côte forment un mot existant
import os  # Module pour les chemins de fichiers

def verification_place(matrice,y,x, direction,mot):  # Vérifie si le placement est possible
    if direction == "horizontal" : #horizontal
        for i in range(len(mot)):  # Pour chaque lettre du mot
            if matrice[y][x+i] != "" and matrice[y][x+i]!= mot[i] :  # Si case occupée et différente
                return f"changez vos coordonnées, la case {y} {x+i} est déjà prise"  # Erreur de placement
    elif direction == "vertical" : #vertical
        for i in range(len(mot)):  # Pour chaque lettre
            if matrice[y+i][x] != "" and matrice[y+i][x] != mot[i]:  # Case occupée différente
                return f"changez vos coordonnées, la case {y+i} {x} est déjà prise "  # Erreur
    return True  # Placement valide


def verification_mot_horizontal(plateau,y,x,mot):  # Vérifie les mots formés horizontalement
    dossier = os.path.dirname(__file__)  # Répertoire du script
    chemin_fichier = os.path.join(dossier, "mots_autorises.txt")  # Chemin du fichier de mots
    with open(chemin_fichier,'r', encoding='utf-8') as fichier:  # Ouvrir le fichier
        mots_valides = set(ligne.strip() for ligne in fichier)  # Ensemble des mots valides

    # gauche
    if x > 0 and plateau[y][x-1] != "":  # Si lettre à gauche
        nouv_motA=[plateau[y][x-1] + mot]  # Nouveau mot avec lettre gauche
        verif_boucle = False  # Indicateur de boucle
        n = 1  # Compteur
        while not verif_boucle:  # Tant que pas fini
            n += 1  # Incrémenter
            if x-n >= 0 and plateau[y][x-n] != "":  # Lettre plus à gauche
                nouv_motA = [plateau[y][x-n]] + nouv_motA  # Ajouter au début
            else:
                verif_boucle = True  # Fin de la boucle
        nouv_motA = "".join(nouv_motA)  # Convertir en chaîne
        if nouv_motA not in mots_valides:  # Si mot invalide
            return False  # Erreur

    # droite
    if x + len(mot) < len(plateau) and plateau[y][x + len(mot)] != "":  # Si lettre à droite
        nouv_motB=[mot + plateau[y][x + len(mot)]]  # Nouveau mot avec lettre droite
        verif_boucle = False  # Indicateur
        n = 1  # Compteur
        while not verif_boucle:  # Boucle
            n += 1  # Incrémenter
            if x+n < len(plateau) and plateau[y][x+n] != "":  # Lettre plus à droite
                nouv_motB = nouv_motB + [plateau[y][x+n]]  # Ajouter à la fin
            else:
                verif_boucle = True  # Fin
        nouv_motB="".join(nouv_motB)  # Chaîne
        if nouv_motB not in mots_valides:  # Invalide
            return False  # Erreur

    # vertical
    for i in range(len(mot)):  # Pour chaque lettre du mot horizontal
        col = x+i  # Colonne actuelle
        if y > 0 and plateau[y-1][col] != "":  # Lettre au-dessus
            nouv_mot1=[plateau[y-1][col],mot[i]]  # Nouveau mot vertical
            verif_boucle = False  # Indicateur
            n = 1  # Compteur
            while not verif_boucle:  # Boucle
                n += 1  # Incrémenter
                if y-n >= 0 and plateau[y-n][col] != "":  # Lettre plus haut
                    nouv_mot1 =[plateau[y-n][col]] + nouv_mot1  # Ajouter au début
                else:
                    verif_boucle = True  # Fin
            nouv_mot1="".join(nouv_mot1)  # Chaîne
            if nouv_mot1 not in mots_valides:  # Invalide
                return False  # Erreur
        elif y+1 < len(plateau) and plateau[y+1][col] != "":  # Lettre en-dessous
            nouv_mot2=[mot[i],plateau[y+1][col]]  # Nouveau mot
            verif_boucle = False  # Indicateur
            n = 1  # Compteur
            while not verif_boucle:  # Boucle
                n += 1  # Incrémenter
                if y+n < len(plateau) and plateau[y+n][col] != "":  # Lettre plus bas
                    nouv_mot2 = nouv_mot2 + [plateau[y+n][col]]  # Ajouter à la fin
                else:
                    verif_boucle = True  # Fin
            nouv_mot2 = "".join(nouv_mot2)  # Chaîne
            if nouv_mot2 not in mots_valides:  # Invalide
                return False  # Erreur
    return True  # Tout valide
                

def verification_mot_vertical(plateau, y, x, mot):  # Vérifie les mots formés verticalement
    import os  # Import local
    dossier = os.path.dirname(__file__)  # Répertoire
    chemin_fichier = os.path.join(dossier, "mots_autorises.txt")  # Chemin fichier
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:  # Ouvrir
        mots_valides = set(ligne.strip() for ligne in fichier)  # Mots valides

    # haut
    if y > 0 and plateau[y-1][x] != "":  # Lettre au-dessus
        nouv_motC = [plateau[y-1][x]] + list(mot)  # Nouveau mot avec haut
        verif_boucle = False  # Indicateur
        n = 1  # Compteur
        while not verif_boucle:  # Boucle
            n += 1  # Incrémenter
            if y-n >= 0 and plateau[y-n][x] != "":  # Lettre plus haut
                nouv_motC = [plateau[y-n][x]] + nouv_motC  # Ajouter début
            else:
                verif_boucle = True  # Fin
        nouv_motC = "".join(nouv_motC)  # Chaîne
        if nouv_motC not in mots_valides:  # Invalide
            return False  # Erreur

    # bas
    if y + len(mot) < len(plateau) and plateau[y + len(mot)][x] != "":  # Lettre en-dessous
        nouv_motD = list(mot) + [plateau[y + len(mot)][x]]  # Nouveau mot avec bas
        verif_boucle = False  # Indicateur
        n = 1  # Compteur
        while not verif_boucle:  # Boucle
            n += 1  # Incrémenter
            if y+n < len(plateau) and plateau[y+n][x] != "":  # Lettre plus bas
                nouv_motD = nouv_motD + [plateau[y+n][x]]  # Ajouter fin
            else:
                verif_boucle = True  # Fin
        nouv_motD = "".join(nouv_motD)  # Chaîne
        if nouv_motD not in mots_valides:  # Invalide
            return False  # Erreur

    # horizontal pour chaque lettre du mot
    for i in range(len(mot)):  # Pour chaque lettre du mot vertical
        row = y + i  # Ligne actuelle
        if x > 0 and plateau[row][x-1] != "":  # Lettre à gauche
            nouv_mot3 = [plateau[row][x-1], mot[i]]  # Nouveau mot horizontal
            verif_boucle = False  # Indicateur
            n = 1  # Compteur
            while not verif_boucle:  # Boucle
                n += 1  # Incrémenter
                if x-n >= 0 and plateau[row][x-n] != "":  # Lettre plus à gauche
                    nouv_mot3 = [plateau[row][x-n]] + nouv_mot3  # Ajouter début
                else:
                    verif_boucle = True  # Fin
            nouv_mot3 = "".join(nouv_mot3)  # Chaîne
            if nouv_mot3 not in mots_valides:  # Invalide
                return False  # Erreur
        elif x + 1 < len(plateau[0]) and plateau[row][x+1] != "":  # Lettre à droite
            nouv_mot4 = [mot[i], plateau[row][x+1]]  # Nouveau mot
            verif_boucle = False  # Indicateur
            n = 1  # Compteur
            while not verif_boucle:  # Boucle
                n += 1  # Incrémenter
                if x+n < len(plateau[0]) and plateau[row][x+n] != "":  # Lettre plus à droite
                    nouv_mot4 = nouv_mot4 + [plateau[row][x+n]]  # Ajouter fin
                else:
                    verif_boucle = True  # Fin
            nouv_mot4 = "".join(nouv_mot4)  # Chaîne
            if nouv_mot4 not in mots_valides:  # Invalide
                return False  # Erreur
    return True  # Tout valide
