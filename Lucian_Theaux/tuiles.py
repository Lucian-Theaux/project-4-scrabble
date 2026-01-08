# coding=utf-8
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter                             
import turtle
from RIVES_Raphaelle.dictionnaire_lettres import points
from Lucian_Theaux.calcul_score import scoreboard               # Importer la fonction scoreboard pour afficher le score

turtle.speed(0)                         # Régler la vitesse de dessin au maximum

def tuile(ltr, slider_metric):
    """
    tuile: crée une tuile affichant la lettre et le score de cette même lettre
    - ltr: Prend en entré une chaine de caractère de une seule lettre
    """
    metric = slider_metric.get()                    # Récupérer la valeur du curseur pour la taille des tuiles
    turtle.pencolor('black')           # Définir la couleur du contour de la tuile  
    turtle.fillcolor('#D5B486')         # Définir la couleur de remplissage de la tuile
    turtle.begin_fill()              # Commencer le remplissage de la tuile 
    for i in range(4):                  # Dessiner un carré pour la tuile
        turtle.fd(5*metric)
        turtle.lt(90)
    turtle.end_fill()                   # Terminer le remplissage de la tuile
    turtle.penup()
    turtle.fd(1.5*metric)           # Se déplacer à l'intérieur de la tuile 
    turtle.lt(90)                   # Tourner à gauche
    turtle.fd(0.8*metric)
    turtle.rt(90)
    turtle.write(ltr, font=('Arial', 3*metric))                 # Écrire la lettre au centre de la tuile
    turtle.rt(90)
    turtle.fd(0.8*metric)
    turtle.lt(90)
    if points[ltr] >= 10:           # Ajuster la position pour écrire le score en bas à droite de la tuile si le score est à deux chiffres
        turtle.fd(2.2*metric)                                           # Se déplacer à la position du score
        turtle.write(points[ltr], font=('Arial', metric))                   # Écrire le score de la lettre
        turtle.fd(1.4*metric)                                   # Se déplacer à la fin de la tuile
    else:                           # Ajuster la position pour écrire le score en bas à droite de la tuile si le score est à un chiffre
        turtle.fd(2.7*metric)
        turtle.write(points[ltr], font=('Arial', metric))
        turtle.fd(0.8*metric)
    turtle.pendown()
    


def letter_impression(slider_metric, lettre):
    """
    letter_impression: fait apparaitre les tuiles du mot demandé à partir de la fonction tuiles
    """
    metric = slider_metric.get()
    texte = lettre.get()
    texte = texte.upper()                               # Mettre le mot en majuscules pour la comparaison
    turtle.goto(0,0)                 # Revenir au centre de l'écran     
    turtle.clear()                      # Effacer l'écran avant d'afficher les nouvelles tuiles
    turtle.penup()
    turtle.setheading(180)                  # Tourner vers la gauche
    turtle.fd(((5*metric)*len(texte))/2)            # Se déplacer à la position de départ pour centrer les tuiles
    turtle.setheading(0)           # Revenir à l'orientation initiale   
    turtle.pendown()
    for ltr in texte:                     # Parcourir chaque lettre du mot  
        if ltr.isupper():                   # Vérifier si le caractère est une lettre majuscule
            tuile(ltr, slider_metric)           # Appeler la fonction tuile pour dessiner la tuile
        else:                           # Gérer le cas où le caractère n'est pas une lettre majuscule
            print("ce n'est pas une lettre : {0}".format(ltr))                  # Afficher un message d'erreur dans la console
            turtle.fd(5*metric)
    scoreboard(length=5)                            # Appeler la fonction scoreboard pour afficher le score total des lettres affichées
