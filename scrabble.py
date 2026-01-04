# coding=utf-8
#* Projet réalisé par :
#* Roméo HUYNH
"""Ici on importe les fichiers nécéssaires pour le projet"""
import turtle as tt
import tkinter as tk
from Lucian_Theaux.search import recherche
from Lucian_Theaux.tuiles import tuile, letter_impression
from Lucian_Theaux.calcul_score import ajout_score, scoreboard
from RIVES_Raphaelle.dictionnaire_lettres import points
import time

#* -------------- Zone commentaire --------------------

#* LUCIAN - J'ai ajouté la condition de verif expliqué en Docstring de Score et j'ai changé l'output en tuple pour pouvoir récup l'information rapidement pour l'interface turtle.
#TODO - Attendre que Roméo ai finit sa partie sur turtle
#? Y'a des trucs que je dois faire en plus ou pas ?

#* ----------------------------------------------------

"""Ici on initialise quelques paramètres utiles"""
tt.title("Projet_4 Scrabble")                     #Fonction qui associé à ces paramètres permet de mettre la fenêtre graphique en full screen
tt.speed(8)
tt.hideturtle()
tt.down()
tt.screensize(300,300)
nbmots = 0


def Score(lettre : str, points : dict) -> str :
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

    verif, index = recherche(mot)

    if verif:
        for car in mot:
            resultat = resultat + points[car]
        ajout_score(resultat,mot)
        tt.up()
        tt.goto(-50,-200)
        tt.setheading(0)
        tt.down()
        mot_et_score(mot, resultat)
    else:
        tt.up()
        tt.goto(-50,-200)
        tt.setheading(0)
        tt.down()
        # tt.write(f'Le mot {mot} ne fait pas parti de la liste règlementaire...', font=('Arial', 16, 'bold'))
        return None
        # return f"Le mot {mot} ne fait pas parti de la liste règlementaire..."

def double(lettre : str, points : dict) -> str :
    verification =Score(lettre, points)
    if verification != None:
        res = verification[0]*2
        tt.write('Le mot %s compte double, il vaut %s pts.' % (lettre, res), font =('Calibri', 16, 'italic'))
    else:
        tt.write('Erreur', font =('Calibri', 16, 'italic'))

def bareme_scrabble():
    """
    Affiche toutes les tuiles du Scrabble classées par nombre de points
    """
    metric = slider_metric.get()
    tt.speed(0)
    tt.up()
    tt.goto(-600, 325)
    tt.write("Barème des points :", font=('Arial', 16, 'bold'))
    tt.goto(-600, float(tt.pos()[1]) - float(6*metric))
    tt.setheading(0)
    tt.down()
    groupes = [
        (1,  ['A','E','I','L','N','O','R','S','T','U']),
        (2,  ['D','G','M']),
        (3,  ['B','C','P']),
        (4,  ['F','H','V']),
        (8,  ['J','Q']),
        (10, ['K','W','X','Y','Z'])]
    for score, lettres in groupes:
        for ltr in lettres:
            tuile(ltr, slider_metric)
        tt.penup()
        tt.goto(-600, float(tt.pos()[1]) - 6*metric)
        tt.pendown()
    tt.hideturtle()

def impression(slider_metric, lettre, points):
    letter_impression(slider_metric, lettre)
    Score(lettre, points)
    scoreboard(length=5)





def historique_scores():
    """
    Affiche l'historique des scores enregistrés dans le fichier scores.txt
    """
    tt.up()
    tt.goto(200, 200)
    tt.setheading(0)
    tt.down()
    tt.write("Historique des scores :", font=('Arial', 16, 'bold'))
    tt.up()
    tt.goto(200, float(tt.pos()[1]) - 20)
    tt.setheading(0)
    tt.down()
    try:
        with open("scores.txt", "r") as f:
            lignes = f.readlines()
            for ligne in lignes:
                tt.write(ligne.strip(), font=('Arial', 12))
                tt.up()
                tt.goto(200, float(tt.pos()[1]) - 20)
                tt.setheading(0)
                tt.down()
    except FileNotFoundError:
        tt.write("Aucun score enregistré.", font=('Arial', 12))

def mot_et_score(lettre : str, points : dict) -> str :
    metric=slider_metric.get()
    tt.up()
    tt.goto(200, 200-nbmots*metric)
    tt.down()
    tt.write(' NEW %s = %s pts.' %(lettre, points), font =('Calibri', 16, 'italic'))
    nbmots += 1

root = tk.Tk()

#──────────────────── Interface graphique ─────────────────
tt.title('Scrabble.io')
tt.setup(1.0,1.0)
root.title('Scrabble.io')
# root.geometry('500x200')

# ────────────────── Zone d’interaction ────────────────────
# begin_vertical()
right = tk.Frame(root)
input_label = tk.Label(right,text='Entrer un mot (sans parenthèses):')
input_label.pack()
lettre = tk.Entry(right)
lettre.insert(0, 'exemple: tortue')
lettre.pack()
slider_metric = tk.Scale(right, orient='horizontal')
slider_metric.pack()
slider_metric.set(10)
send_button = tk.Button(right,text='Envoyer',command=lambda:impression(slider_metric, lettre, points))
send_button.pack()
# end_vertical()
# end_vertical()
show_button = tk.Button(right,text='Afficher le barème', command=bareme_scrabble)
show_button.pack()
show_button = tk.Button(right,text="Afficher l'historique", command=historique_scores)
show_button.pack()
right.grid(column=1, row=0)

# bareme_scrabble()
tt.listen()
tt.mainloop();root.mainloop()
