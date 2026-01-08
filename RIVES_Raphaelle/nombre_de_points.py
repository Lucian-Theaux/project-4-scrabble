import turtle as tt
import tkinter as tk
from RIVES_Raphaelle.search import recherche
from Lucian_Theaux.tuiles import tuile, letter_impression
from Lucian_Theaux.calcul_score import ajout_score, scoreboard
from RIVES_Raphaelle.dictionnaire_lettres import points

def double(lettre : str, points : dict) -> str :
    verification =Score(lettre, points)
    if verification != None:
        res = verification[0]*2
        tt.write('Le mot %s compte double, il vaut %s pts.' % (lettre, res), font =('Calibri', 16, 'italic'))
    else:
        tt.write('Erreur', font =('Calibri', 16, 'italic'))

def Score(lettre : str, points : dict, slider_metric :int) -> str :
    """
    Score: Prend en entrée le mot que l'on cherche et le dictionnaire de point, elle renvoie ensuite: 
           - Si le mot se trouve dans la liste du Scrabble, son score et sa position dans la liste sous forme de tuple, elle ajoute ensuite le score et le mot dans le fichier scores.txt.
           - Si le mot n'est pas dans la liste du Scrabble, None. 

    - mot : Prend en entrée le mot que l'on cherche sous forme de string
    - points : Prend en entrée le dictionnaire de point, officiel ou personnalisé
    """
    resultat = 0
    mot = lettre.get()
    mot = mot.upper()
    metric = slider_metric.get()

    verif, index = recherche(mot)

    if verif:
        for car in mot:
            resultat = resultat + points[car]
        ajout_score(resultat,mot) 
        letter_impression(slider_metric, lettre)     
        tt.up()
        tt.goto(-200,-200)
        tt.setheading(0)
        tt.down()
        tt.write(f'valeur {mot}: {resultat}pts', font=('Arial', 30, 'bold')) 
    else:
        tt.up()
        tt.goto(-50,-200)
        tt.setheading(0)
        tt.down()
        tt.write(f'Le mot {mot} ne fait pas parti de la liste règlementaire...', font=('Arial', 16, 'bold'))
        return None
    historique()
    
def historique():
    """
    fonction historique qui affiche les 10 derniers mots
    """
    historique_list=[]
    F = open('scores.txt','r', encoding='utf-8')
    historique_list = F.read().split('\n')
    F.close()
    while len(historique_list) >10:
      historique_list.remove(historique_list[0]) 
    tt.up()
    tt.goto(300,100)
    tt.down() 
    tt.write('Historique des 10 derniers: \n'+'\n'.join(historique_list), font=('Arial', 16, 'italic'))

