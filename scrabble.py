# coding=utf-8
#* Projet réalisé par :
#* Roméo HUYNH
"""Ici on importe les fichiers nécéssaires pour le projet"""
import turtle as tt
import tkinter as tk
from Lucian_Theaux.search import recherche
from Lucian_Theaux.tuiles import tuile, letter_impression
from Lucian_Theaux.calcul_score import ajout_score
from RIVES_Raphaelle.dictionnaire_lettres import points
import time

#* -------------- Zone commentaire --------------------

#* LUCIAN - J'ai ajouté la condition de verif expliqué en Docstring de Score et j'ai changé l'output en tuple pour pouvoir récup l'information rapidement pour l'interface turtle.
#TODO - Attendre que Roméo ai finit sa partie sur turtle
#? Y'a des trucs que je dois faire en plus ou pas ?

#* ----------------------------------------------------

"""Ici on initialise quelques paramètres utiles"""
tt.title("Projet_4 Scrabble")                     #Fonction qui associé à ces paramètres permet de mettre la fenêtre graphique en full screen
tt.speed(0)
tt.hideturtle()
tt.down()
tt.screensize(300,300)


def Score(lettre : str, points : dict) -> str :
    """
    Score: Prend en entrée le mot que l'on cherche et le dictionnaire de point, elle renvoie ensuite: 
           - Si le mot se trouve dans la liste du Scrabble, son score et sa position dans la liste sous forme de tuple, elle ajoute ensuite le score et le mot dans le fichier scores.txt.
           - Si le mot n'est pas dans la liste du Scrabble, None. 

    - mot : Prend en entrée le mot que l'on cherche sous forme de string
    - points : Prend en entrée le dictionnaire de point, officiel ou personnalisé
    """
    resultat = 0
    mot = lettre.upper()

    verif, index = recherche(mot)

    if verif:
        for car in mot:
            resultat = resultat + points[car]
        ajout_score(resultat)
        tt.write('Le mot {0} vaut {1} pts, il est position {2} dans le dictionnaire.'.format(mot, resultat, index), font=('Arial', 16, 'bold'))
        return (resultat, index)
        # return f"Le mot {mot} vaut {resultat} pts, il est position {index} dans le dictionnaire."
    else:
        tt.write('Le mot {0} ne fait pas parti de la liste règlementaire...'.format(mot), font=('Arial', 16, 'bold'))
        return None
        # return f"Le mot {mot} ne fait pas parti de la liste règlementaire..."


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
            tuile(ltr)
        tt.penup()
        tt.goto(-600, float(tt.pos()[1]) - 6*metric)
        tt.pendown()
    tt.hideturtle()

root = tk.Tk()

#──────────────────── Interface graphique ─────────────────

Bareme = tk.Label(root,text='Barème des points : ')
# begin_vertical()
one_point = tk.Label(root,text='• A, E, I, L, N, O, R, S, T, U : 1 point')
one_point.pack()
two_points = tk.Label(root,text='• D, G, M : 2 points')
two_points.pack()
three_points = tk.Label(root,text='• B, C, P : 3 points')
three_points.pack()
# end_vertical()
# begin_vertical()
four_points = tk.Label(root,text='• F, H, V : 4 points')
four_points.pack()
height_points = tk.Label(root,text='• J, Q : 8 points')
height_points.pack()
ten_points = tk.Label(root,text='• K, W, X, Y, Z : 10 points')
ten_points.pack()
# end_vertical()
# end_horizontal()
# end_vertical()
empty = tk.Label(root,text='')
empty.pack()
# ────────────────── Zone d’interaction ────────────────────
# begin_vertical()
input_label = tk.Label(root,text='Entrer un mot :')
input_label.pack()
lettre = tk.Entry(root)
lettre.pack()
slider_metric = tk.Scale(root, orient='horizontal')
slider_metric.pack()
slider_metric.set(10)
send_button = tk.Button(root,text='Envoyer',command=letter_impression)
send_button.pack()
# end_vertical()
# end_vertical()
show_button = tk.Button(root,text='Afficher le barème', command=bareme_scrabble)
show_button.pack()

bareme_scrabble()
tt.listen()
tt.mainloop()#;root.mainloop()
