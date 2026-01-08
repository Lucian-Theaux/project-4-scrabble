import turtle as tt
import tkinter as tk
from RIVES_Raphaelle.search import recherche
from Lucian_Theaux.tuiles import tuile, letter_impression
from Lucian_Theaux.calcul_score import ajout_score, scoreboard
from RIVES_Raphaelle.dictionnaire_lettres import points

def double(lettre : str, points : dict) -> str :
    verification =Score(lettre, points)                         # Appeler la fonction Score pour obtenir le score du mot
    if verification != None:                                # Vérifier si le mot est valide
        res = verification[0]*2                                 # Calculer le score double
        tt.write('Le mot %s compte double, il vaut %s pts.' % (lettre, res), font =('Calibri', 16, 'italic'))               # Afficher le score double
    else:
        tt.write('Erreur', font =('Calibri', 16, 'italic'))         # Afficher une erreur si le mot n'est pas valide    

def Score(lettre : str, points : dict, slider_metric :int) -> str :
    """
    Score: Prend en entrée le mot que l'on cherche et le dictionnaire de point, elle renvoie ensuite: 
           - Si le mot se trouve dans la liste du Scrabble, son score et sa position dans la liste sous forme de tuple, elle ajoute ensuite le score et le mot dans le fichier scores.txt.
           - Si le mot n'est pas dans la liste du Scrabble, None. 

    - mot : Prend en entrée le mot que l'on cherche sous forme de string
    - points : Prend en entrée le dictionnaire de point, officiel ou personnalisé
    """
    resultat = 0                            # Initialiser le score à 0
    mot = lettre.get()                      # Récupérer le mot entré par l'utilisateur
    mot = mot.upper()                           # Mettre le mot en majuscules pour la comparaison
    metric = slider_metric.get()                    # Récupérer la valeur du curseur pour la taille des tuiles

    verif, index = recherche(mot)        # Appeler la fonction recherche pour vérifier si le mot est dans la liste      

    if verif:                   # Si le mot est dans la liste
        for car in mot:             # Parcourir chaque caractère du mot
            resultat = resultat + points[car]                           # Ajouter le score de chaque lettre au score total
        ajout_score(resultat,mot)                       # Appeler la fonction ajout_score pour ajouter le score et le mot dans le fichier scores.txt
        letter_impression(slider_metric, lettre)            # Appeler la fonction letter_impression pour afficher les tuiles du mot 
        tt.up()                                         # Lever le stylo pour ne pas dessiner en se déplaçant
        tt.goto(-200,-200)                              # Se déplacer en bas à gauche de l'écran pour afficher le score
        tt.setheading(0)                                # Revenir à l'orientation initiale(droite)
        tt.down()
        tt.write(f'valeur {mot}: {resultat}pts', font=('Arial', 30, 'bold'))            # Afficher le score du mot
    else:                                # Si le mot n'est pas dans la liste on affiche un message d'erreur
        tt.up()
        tt.goto(-50,-200)
        tt.setheading(0)
        tt.down()
        tt.write(f'Le mot {mot} ne fait pas parti de la liste règlementaire...', font=('Arial', 16, 'bold'))
        return None
