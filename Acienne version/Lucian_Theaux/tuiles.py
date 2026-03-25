# Lucian Théaux
# coding=utf-8

import sys                              # Importation du module sys pour la gestion des chemins de fichiers
import os                           # Importation du module os pour la gestion des chemins de fichiers
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))                 # Ajout du répertoire parent au chemin de recherche des modules

import tkinter                              # Importation du module tkinter pour l'interface graphique
import turtle                               # Importation du module turtle pour le dessin
from RIVES_Raphaelle.dictionnaire_lettres import points                 # Importation du dictionnaire de points
from Lucian_Theaux.calcul_score import scoreboard                 # Importation de la fonction d'affichage du score 

turtle.speed(0)                          # Régler la vitesse de dessin au maximum   

def tuile(ltr, slider_metric):
    """
    tuile: crée une tuile affichant la lettre et le score de cette même lettre
    - ltr: Prend en entré une chaine de caractère de une seule lettre
    """
    metric = slider_metric.get()                # Récupération de la taille des tuiles à dessiner grâce au slider metric
    turtle.pencolor('black')                    # Couleur du contour de la tuile: noir
    turtle.fillcolor('#D5B486')                 # Couleur de remplissage de la tuile
    turtle.begin_fill()                             # Début du remplissage de la tuile
    for i in range(4):                          # Boucle pour dessiner un carré
        turtle.fd(5*metric)
        turtle.lt(90)
    turtle.end_fill()                           # Fin du remplissage de la tuile
    turtle.penup()      
    turtle.fd(1.5*metric)                   # Positionnement pour écrire la lettre
    turtle.lt(90)                              # Tourner à gauche de 90 degrés
    turtle.fd(0.8*metric)
    turtle.rt(90)
    turtle.write(ltr, font=('Arial', 3*metric))      # Écriture de la lettre avec une taille proportionnelle à la taille de la tuile    
    turtle.rt(90)
    turtle.fd(0.8*metric)
    turtle.lt(90)
    if points[ltr] >= 10:                           # Si le score de la lettre est supérieur ou égal à 10 on se deplace différemment pour centrer le score
        turtle.fd(2.2*metric)                     # Positionnement pour écrire le score
        turtle.write(points[ltr], font=('Arial', metric))   # Écriture du score de la lettre    
        turtle.fd(1.4*metric)                       # Repositionnement après l'écriture du score
    else:                       # Si le score de la lettre est inférieur à 10...
        turtle.fd(2.7*metric)
        turtle.write(points[ltr], font=('Arial', metric))
        turtle.fd(0.8*metric)
    turtle.pendown()
    


def letter_impression(slider_metric, lettre):
    """
    letter_impression: fait apparaitre les tuiles du mot demandé à partir de la fonction tuiles
    """
    metric = slider_metric.get()                        # Récupération de la taille des tuiles à dessiner grâce au slider metric
    texte = lettre.get()                                # Récupération du mot entré par l'utilisateur  
    texte = texte.upper()                               # Mise en majuscule du mot pour correspondre aux clés du dictionnaire   
    turtle.goto(0,0)                                    # Repositionnement de la tortue au centre de l'écran     
    turtle.clear()                                      # Effacement de l'écran
    turtle.penup()
    turtle.setheading(180)                              # Orientation de la tortue vers la gauche   
    turtle.fd(((5*metric)*len(texte))/2)                # Positionnement pour centrer le mot à afficher
    turtle.setheading(0)                                    # Orientation de la tortue vers la droite
    turtle.pendown()
    for ltr in texte:                             # Pour chaque lettre du mot entré
        if ltr.isupper():                           # Vérification que le caractère est une lettre majuscule
            tuile(ltr, slider_metric)               # Appel de la fonction tuile pour dessiner la tuile correspondante
        else:
            print("ce n'est pas une lettre : {0}".format(ltr))          # Message d'erreur si le caractère n'est pas une lettre
            turtle.fd(5*metric)
    scoreboard(length=5)                                # Appel de la fonction scoreboard pour afficher le score total du mot dessiné
