import os 

def recherche(mot:str) -> tuple:
    """
    recherche: Cherche le mot dans le fichier texte mots_autorises.txt et renvoie un tuple contenant une vérification de la présence du mot (True/False) et son index dans le fichier (si False, renvoie 0)
    - mot: chaine de charactères prise en entrée
    """
    mot = mot.upper()                       # Mettre le mot en majuscules pour la comparaison
    i = 1                         # Initialiser l'index à 1 
    dossier = os.path.dirname(__file__)             # Obtenir le chemin du dossier courant
    chemin_fichier = os.path.join(dossier, "mots_autorises.txt")        # Construire le chemin complet du fichier   
    with open(chemin_fichier, "r", encoding="utf-8") as F:              # Ouvrir le fichier en mode lecture avec encodage utf-8
        for ligne in F:                             # Parcourir chaque ligne du fichier
            if ligne[:-1] == mot:                                # Comparer le mot 
                return (True, i)                                    # Si trouvé, renvoyer True et l'index
            i += 1                                          # Incrémenter l'index
        return (False, 0)           # Si pas trouvé, renvoyer False et 0          
