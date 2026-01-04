# coding=utf-8
import tkinter
import turtle
# from RIVES_Raphaelle.dictionnaire_lettres import points
from dictionnaire_lettres import points

turtle.speed(0)

def tuile(ltr, slider_metric):
    """
    tuile: crée une tuile affichant la lettre et le score de cette même lettre
    - ltr: Prend en entré une chaine de caractère de une seule lettre
    """
    metric = slider_metric.get()
    turtle.pencolor('black')
    turtle.fillcolor('#D5B486')
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(5*metric)
        turtle.lt(90)
    turtle.end_fill()
    turtle.penup()
    turtle.fd(1.5*metric)
    turtle.lt(90)
    turtle.fd(0.8*metric)
    turtle.rt(90)
    turtle.write(ltr, font=('Arial', 3*metric))
    turtle.rt(90)
    turtle.fd(0.8*metric)
    turtle.lt(90)
    if points[ltr] >= 10:
        turtle.fd(2.5*metric)
        turtle.write(points[ltr], font=('Arial', metric))
        turtle.fd(metric)
    else:
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
    texte = texte.upper()
    turtle.goto(0,0)
    turtle.clear()
    turtle.penup()
    turtle.setheading(180)
    turtle.fd(((5*metric)*len(texte))/2)
    turtle.setheading(0)
    turtle.pendown()
    for ltr in texte:
        if ltr.isupper():
            tuile(ltr, slider_metric)
        else:
            print("ce n'est pas une lettre : {0}".format(ltr))
            turtle.fd(5*metric)
