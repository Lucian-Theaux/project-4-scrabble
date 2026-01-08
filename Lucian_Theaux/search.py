import os 

def recherche(mot:str) -> tuple:
    """
    recherche: Cherche le mot dans le fichier texte mots_autorises.txt et renvoie un tuple contenant une vérification de la présence du mot (True/False) et son index dans le fichier (si False, renvoie 0)
    - mot: chaine de charactères prise en entrée
    """
    mot = mot.upper()
    i = 1
    dossier = os.path.dirname(__file__)
    chemin_fichier = os.path.join(dossier, "mots_autorises.txt")
    with open(chemin_fichier, "r", encoding="utf-8") as F:
        for ligne in F:
            if ligne[:-1] == mot:
                return (True, i)
            i += 1
        return (False, 0)          
    