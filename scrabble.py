from Lucian_Theaux.search import recherche
from Lucian_Theaux.calcul_score import ajout_score
from RIVES_Raphaelle.dictionnaire_lettres import points
import time

def score(mot : str, points : dict) -> str :
    resultat = 0
    mot = mot.upper()

    verif, index = recherche(mot)
    for car in mot:
        resultat = resultat + points[car]
    ajout_score(resultat)
    return f"Le mot {mot} vaut {resultat} pts"

# print(score('zoo', points))
