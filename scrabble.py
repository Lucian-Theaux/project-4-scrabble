from Lucian_Theaux.search import recherche
from Lucian_Theaux.calcul_score import ajout_score
from RIVES_Raphaelle.dictionnaire_lettres import points
import time



#* -------------- Zone commentaire --------------------

#* LUCIAN - J'ai ajouté la condition de verif expliqué en Docstring de Score et j'ai changé l'output en tuple pour pouvoir récup l'information rapidement pour l'interface turtle.
#TODO - Attendre que Roméo ai finit sa partie sur turtle
#? Y'a des trucs que je dois faire en plus ou pas ?

#* ----------------------------------------------------



def Score(mot : str, points : dict) -> str :
    """
    Score: Prend en entrée le mot que l'on cherche et le dictionnaire de point, elle renvoie ensuite: 
           - Si le mot se trouve dans la liste du Scrabble, son score et sa position dans la liste sous forme de tuple, elle ajoute ensuite le score et le mot dans le fichier scores.txt.
           - Si le mot n'est pas dans la liste du Scrabble, None. 

    - mot : Prend en entrée le mot que l'on cherche sous forme de string
    - points : Prend en entrée le dictionnaire de point, officiel ou personnalisé
    """
    resultat = 0
    mot = mot.upper()

    verif, index = recherche(mot)

    if verif:
        for car in mot:
            resultat = resultat + points[car]
        ajout_score(resultat)
        return (resultat, index)
        # return f"Le mot {mot} vaut {resultat} pts, il est position {index} dans le dictionnaire."
    else:
        return None
        # return f"Le mot {mot} ne fait pas parti de la liste règlementaire..."

print(Score('zoo', points))

