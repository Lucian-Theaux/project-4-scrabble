# coding=utf-8
#* Projet réalisé par :
#* Roméo HUYNH
"""Ici on importe les fichiers nécéssaires pour le projet"""
from turtle import*
from nsi_ui import*


"""Ici on initialise quelques paramètres utiles"""
title("Projet_4 Scrabble")
setup(1.0, 1.0)                                 #Fonction qui associé à ces paramètres permet de mettre la fenêtre graphique en full screens
speed(0)
hideturtle()
penup()
pendown()


begin_horizontal()
begin_vertical()
label('Barème des points : ')
begin_horizontal()
label(' A, E, I, L, N, O, R, S, T, U : 1 point')
end_horizontal()
begin_horizontal()
label(' D, G, M : 2 points')
end_horizontal()
begin_horizontal()
label(' B, C, P : 3 points')
end_horizontal()
end_vertical()
begin_vertical()
begin_horizontal()
label(' F, H, V : 4 points')
end_horizontal()
begin_horizontal()
label(' J, Q : 8 points')
end_horizontal()
begin_horizontal()
label(' K, W, X, Y, Z : 10 points')
end_horizontal()
end_vertical()
end_horizontal()

Champ1=entry('Coucou')



def carre():            # ROMEO NE MET PAS D4ACCENT EN PROGRAMMATION
   for i in range(4):
        down()
        forward(50)
        left(90)

def Bareme():           # ROMEO NE MET PAS D4ACCENT EN PROGRAMMATION
    up()
    goto(-800,350)
    write("Barème des Points : ", font=("Arial", 24, "normal"))
    goto(-800,280)
    for i in range(10):
        carre()
        up()
        forward(75)
        down()



def ecriture(mot):     # ROMEO NE MET PAS D4ACCENT EN PROGRAMMATION
    write(mot)
    

Bareme()



listen()
mainloop()