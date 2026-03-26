# projet Decembre groupe 4
# coding=utf-8
# Projet réalisé par :
#* Lucian THEAUX
#* Raphaëlle RIVES
#* Roméo HUYNH

#! A faire !!!!!
#* Trouver le problème de l'affichage des tuiles
#* Afficher l'historiquer
#* Afficher le scoreboard

# -------------------- Ici on importe les fichiers nécéssaires pour le projet --------------------
import tkinter as tk
import turtle as tt
import os
import verification as verif
import scrabble as scrabble

# -------------------- Initialisation du plateau --------------------
plateau = scrabble.creation_plateau()          # Création de la variable qui va contenir la "matrice" contenant le plateau


# -------------------- Initialisation de la fenêtre turtle --------------------

screen = tt.Screen()
screen.setup(1112, 712)

# --- Ici on initialise quelques paramètres utiles ---
tt.title("Projet Scrabble")                       # Titre de la fenêtre Turtle
# tt.hideturtle()                                   # Cacher le curseur de la tortue
tt.speed(0)                                       # Régler la vitesse de dessin au maximum

# --- On récupère l'image de fond ---
dossier = os.path.dirname(__file__)               # Récupération du dossier courant
chemin_fichier = os.path.join(dossier, "image_plateau.gif") # Chemin vers l'image
screen.bgpic(chemin_fichier)                      # Image de fond
root = tk.Tk()


# -------------------- Zone où se trouve les fonctions qui vont être utilisées par tkinter --------------------
def application_horizontal():
    mot = ""
    for letter in lettre.get(): mot+=letter.capitalize()
    positions = lettre_coo.get().split(' ')
    verification = verif.verification_place(plateau,y=int(positions[1]),x=int(positions[0]),direction="horizontal",mot=mot)
    if verification == True:
        seconde_verification = verif.verification_mot(plateau,y=int(positions[1]),x=int(positions[0]),direction="horizontal",mot=mot)
        if seconde_verification == True:
            scrabble.ajout_mot_horizontal(x=int(positions[0]),y=int(positions[1]),mot=mot,plateau=plateau)
            tt.penup()
            tt.goto((int(positions[0])*47.47)-(1112/2),(712/2)-(47.47*int(positions[1]))-47.47)
            for letter in mot:
                tt.setheading(0)
                tuile(letter)
                tt.setheading(0)
                # tt.rt(90)
                # tt.fd(47.47)
                # tt.setheading(0)
                tt.penup()
            with open('historique.txt', 'a',encoding='utf-8') as fichier:
                fichier.write(f'{mot}\n')
            
            with open('historique.txt', 'r',encoding='utf-8') as fichier:
                tt.goto(220, 356-(47.47+50))
                tt.setheading(270)
                for ligne in fichier:
                    tt.write(f'{ligne}', font=('Arial',10,'italic'))
                    tt.fd(15)




    else:
        print(verification)

def application_vertical():
    mot = ""
    for letter in lettre.get(): mot+=letter.capitalize()
    positions = lettre_coo.get().split(' ')
    verification = verif.verification_place(plateau,y=int(positions[1]),x=int(positions[0]),direction="vertical",mot=mot)
    if verification == True:
        seconde_verification = verif.verification_mot(plateau,y=int(positions[1]),x=int(positions[0]),direction="vertical",mot=mot)
        if seconde_verification == True:
            scrabble.ajout_mot_vertical(x=int(positions[0]),y=int(positions[1]),mot=mot,plateau=plateau)
            tt.penup()
            tt.goto((int(positions[0])*47.47)-1112/2,(int(positions[1])*47.47)-47.47)
            for letter in mot:
                tt.setheading(0)
                tuile(letter)
                tt.setheading(270)
                tt.fd(47.47)
                tt.rt(90)
                tt.fd(47.47)
                tt.setheading(0)
        else:
            print("Votre ne peut pas rentrer sur le plateau, il ne s'aligne pas avec les autres tuiles")

    else:
        print(verification)


def tuile(ltr):
    """
    tuile: crée une tuile affichant la lettre et le score de cette même lettre
    - ltr: Prend en entré une chaine de caractère de une seule lettre
    """
    tt.pendown()
    metric = 47.47
    points = {"A":1 ,"E":1 ,"I":1 ,"L":1 ,"N":1 ,"O":1 ,"R":1 ,"S":1 ,"T":1 ,"U":1 ,"D":2 ,"G":2 ,"M":2 ,"B":3 ,"C":3 ,"P":3 ,"F":4 ,"H":4 ,"V":4 ,"J":8 ,"Q":8 ,"K":10 ,"W":10 ,"X":10 ,"Y":10 ,"Z":10}
    tt.pencolor('black')                    # Couleur du contour de la tuile: noir
    tt.fillcolor('#D5B486')                 # Couleur de remplissage de la tuile
    tt.begin_fill()                             # Début du remplissage de la tuile
    for i in range(4):                          # Boucle pour dessiner un carré
        tt.fd(47.47)
        tt.lt(90)
    tt.end_fill()                           # Fin du remplissage de la tuile
    tt.penup()      
    tt.fd(metric/7)                   # Positionnement pour écrire la lettre
    tt.lt(90)                              # Tourner à gauche de 90 degrés
    tt.fd(metric/7)
    tt.rt(90)
    tt.write(ltr, font=('Arial', 20))      # Écriture de la lettre avec une taille proportionnelle à la taille de la tuile    
    tt.rt(90)
    tt.fd(metric/7)
    tt.lt(90)
    if points[ltr] >= 10:                           # Si le score de la lettre est supérieur ou égal à 10 on se deplace différemment pour centrer le score
        tt.fd((4*metric)/7)                     # Positionnement pour écrire le score
        tt.write(points[ltr], font=('Arial', 5))   # Écriture du score de la lettre    
        tt.fd((2*metric)/7)                       # Repositionnement après l'écriture du score
    else:                       # Si le score de la lettre est inférieur à 10...
        tt.fd((4*metric)/7)
        tt.write(points[ltr], font=('Arial', 5))
        tt.fd((2*metric)/7)
    tt.pendown()

# -------------------- Zone d’interaction (faite par le groupe) --------------------

gauche = tk.Frame(root)                            # Créer un frame pour la zone de saisie Tkinter: crée une colonne à droite
droite = tk.Frame(root)                             # Créer un frame pour la zone d'affichage Tkinter: crée une colonne à gauche
coordonnée = tk.Frame(root)
horizontal_vertical = tk.Frame(root)

input_label = tk.Label(gauche,text='Entrer un mot (sans accents):')  # Label pour indiquer à l'utilisateur d'entrer un mot
input_label.pack()                                # Placer le label dans le frame
lettre = tk.Entry(gauche)                          # Champ de saisie pour le mot
lettre.insert(0, 'exemple: tortue')               # Texte d'exemple
lettre.pack()

send_button2 = tk.Button(droite,text='x2',command=lambda:double(lettre, points, slider_metric))  # Bouton mot compte double
send_button2.pack()
send_button3 = tk.Button(droite,text='x4',command=lambda:quadruple(lettre, points, slider_metric))  # Bouton score du mot x 4
send_button3.pack()
send_button4 = tk.Button(droite,text='x9',command=lambda:nonuple(lettre, points, slider_metric))  # Bouton score du mot x 9
send_button4.pack()
send_button5 = tk.Button(droite,text='x27',command=lambda:gros_bonus(lettre, points, slider_metric))  # Bouton score du mot x 27
send_button5.pack()

show_button = tk.Button(gauche,text='Afficher le barème', command=lambda:bareme_scrabble(slider_metric))  # Bouton du barème
show_button.pack()

lettre_coo = tk.Entry(coordonnée)                          # Champ de saisie pour le mot
lettre_coo.insert(0, '0 0')                                # Texte d'exemple
lettre_coo.grid(row=1)
horizontal_button = tk.Button(horizontal_vertical, text=" → ", command=lambda:application_horizontal())
horizontal_button.grid(column=1,row=2)
vertical_button = tk.Button(horizontal_vertical, text=" ↓ ", command=lambda:application_vertical())
vertical_button.grid(column=2,row=2)

gauche.grid(column=1, row=0)                       # On initialiser "droite" à la colonne 1, ligne 0.  "droite" sera en paramètre pour les widgets
droite.grid(column=2, row=0)                        # Idemme avec "gauche"
coordonnée.grid(column=1, row=1)
horizontal_vertical.grid(column=1,row=2)

# -------------------- Mise en place des éléments turtle sur la fenêtre --------------------

# --- 1. La numérotation des cases ---
tt.penup()
tt.fd(170)
tt.lt(90)
tt.fd(356-(47.47*0.7))
tt.setheading(270)
for i in range(15):    
    tt.write(i, font=('Arial',20))
    tt.fd(47.47)

# --- 2. Titre "Historique"
tt.penup()
tt.goto(220, 356-(47.47+30))
tt.write("Historique", font=('Arial',40))

root.mainloop();tt.mainloop()