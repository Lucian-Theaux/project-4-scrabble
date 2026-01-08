import os                           # Importation du module os pour la gestion des chemins de fichiers

def recherche(mot:str) -> tuple:
    """
    recherche: Cherche le mot dans le fichier texte mots_autorises.txt et renvoie un tuple contenant une vérification de la présence du mot (True/False) et son index dans le fichier (si False, renvoie 0)
    - mot: chaine de charactères prise en entrée
    """
    mot = mot.upper()                           # Mettre le mot en majuscule pour la comparaison
    i = 1                                       # Initialisation de l'index   
    dossier = os.path.dirname(__file__)         # Récupération du dossier courant
    chemin_fichier = os.path.join(dossier, "mots_autorises.txt")            # Construction du chemin complet vers le fichier
    with open(chemin_fichier, "r", encoding="utf-8") as F:                  # Ouverture du fichier en mode lecture avec encodage utf-8
        for ligne in F:                             # Parcours de chaque ligne du fichier
            if ligne[:-1] == mot:           # Comparaison du mot (enlevant le caractère de nouvelle ligne)
                return (True, i)                # Si le mot est trouvé, renvoyer True et l'index
            i += 1
        return (False, 0)               # Si le mot n'est pas trouvé, renvoyer False et 0 
