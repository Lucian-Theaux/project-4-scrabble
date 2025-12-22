# coding=utf-8
#* Projet réalisé par :
#* Roméo HUYNH
"""Ici on importe les fichiers nécéssaires pour le projet"""
from turtle import*
from nsi_ui import*
from Lucian_Theaux.search import recherche
from Lucian_Theaux.calcul_score import ajout_score
from RIVES_Raphaelle.dictionnaire_lettres import points
import time


#* -------------- Zone commentaire --------------------

#* LUCIAN - J'ai ajouté la condition de verif expliqué en Docstring de Score et j'ai changé l'output en tuple pour pouvoir récup l'information rapidement pour l'interface turtle.
#TODO - Attendre que Roméo ai finit sa partie sur turtle
#? Y'a des trucs que je dois faire en plus ou pas ?

#* ----------------------------------------------------

"""Ici on initialise quelques paramètres utiles"""
title("Projet_4 Scrabble")
setup(1.0, 1.0)                         #Fonction qui associé à ces paramètres permet de mettre la fenêtre graphique en full screen
speed(0)
hideturtle()
down()


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



def tuile(ltr):
    """
    tuile: crée une tuile affichant la lettre et le score de cette même lettre
    - ltr: Prend en entré une chaine de caractère de une seule lettre
    """
    metric = get_int(slider_metric)
    pencolor('black')
    fillcolor('#CCA46C')
    begin_fill()
    for i in range(4):
        fd(5*metric)
        lt(90)
    end_fill()
    penup()
    fd(1.5*metric)
    lt(90)
    fd(0.8*metric)
    rt(90)
    write(ltr, font=('Arial', 3*metric))
    rt(90)
    fd(0.8*metric)
    lt(90)
    if points[ltr] >= 10:
        fd(2*metric)
        write(points[ltr], font=('Arial', metric))
        fd(metric)
    else:
        fd(2.7*metric)
        write(points[ltr], font=('Arial', metric))
        fd(0.8*metric)
    pendown()


def letter_impression():
    """
    letter_impression: fait apparaitre les tuiles du mot demandé à partir de la fonction tuiles
    """
    metric = get_int(slider_metric)
    texte = get_string(lettre)
    texte = texte.upper()
    clearscreen()
    speed(0)
    up()
    goto(-((len(texte)/2)*5*metric),-200)
    setheading(0)
    down()
    for ltr in texte:
        if ltr.isupper():
            tuile(ltr)
        else:
            print("ce n'est pas une lettre : {0}".format(ltr))
            fd(5*metric)


def bareme_scrabble():
    """
    Affiche toutes les tuiles du Scrabble classées par nombre de points
    """
    metric = get_int(slider_metric)
    speed(0)
    up()
    goto(-600, 325)
    write("Barème des points :", font=('Arial', 16, 'bold'))
    goto(-600, ycor() - 6*metric)
    setheading(0)
    down()
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
        penup()
        goto(-600, ycor() - 6*metric)
        pendown()
    hideturtle()



#──────────────────── Interface graphique ─────────────────
begin_vertical()
label('Barème des points : ')
begin_horizontal()
begin_vertical()
label('• A, E, I, L, N, O, R, S, T, U : 1 point')
label('• D, G, M : 2 points')
label('• B, C, P : 3 points')
end_vertical()
begin_vertical()
label('• F, H, V : 4 points')
label('• J, Q : 8 points')
label('• K, W, X, Y, Z : 10 points')
end_vertical()
end_horizontal()
end_vertical()
label('')
# ────────────────── Zone d’interaction ────────────────────
begin_vertical()
label('Entrer un mot :')
lettre = entry('')
slider_metric = slider('Valeur du curseur', 0, 100)
button('Envoyer', letter_impression)
end_vertical()
end_vertical()
set_value(slider_metric, 10)
button('Afficher le barème', bareme_scrabble)



bareme_scrabble()
listen()
mainloop()
