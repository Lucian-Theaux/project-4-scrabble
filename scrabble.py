# coding=utf-8
#* Projet réalisé par :
#* Roméo HUYNH
"""Ici on importe les fichiers nécéssaires pour le projet"""
import turtle as tt
import tkinter as tk
from RIVES_Raphaelle.search import recherche
from Lucian_Theaux.tuiles import tuile, letter_impression
from Lucian_Theaux.calcul_score import ajout_score, scoreboard
from RIVES_Raphaelle.dictionnaire_lettres import points
from RIVES_Raphaelle.nombre_de_points import Score, historique
from Romeo.bareme_points import bareme_scrabble
import time

#* -------------- Zone commentaire --------------------

"""Ici on initialise quelques paramètres utiles"""
tt.title("Projet_4 Scrabble")                     # Titre de la fenêtre Turtle
tt.speed(8)                                       # Régler la vitesse initiale
tt.hideturtle()                                   # Cacher le curseur de la tortue
tt.down()                                         # Abaisser le stylo pour commencer à dessiner
tt.screensize(300,300)                            # Configurer la taille de l'écran
tt.speed(0)                                       # Régler la vitesse de dessin au maximum

root = tk.Tk()

#──────────────────── Interface graphique ─────────────────
tt.title('Scrabble.io')                           # Titre de la fenêtre Turtle
tt.setup(1.0,1.0)                                 # Configurer la taille de la fenêtre Turtle
root.title('Scrabble.io')                         # Titre de la fenêtre Tkinter

historique()                                     # Afficher l'historique des 10 derniers mots    

# ────────────────── Zone d’interaction ────────────────────
right = tk.Frame(root)                            # Créer un frame pour la zone de saisie
input_label = tk.Label(right,text='Entrer un mot (sans accents):')                  # Label pour indiquer à l'utilisateur d'entrer un mot
input_label.pack()                                  # Placer le label dans le frame
lettre = tk.Entry(right)                          # Champ de saisie pour le mot
lettre.insert(0, 'exemple: tortue')                 # Texte d'exemple
lettre.pack()      
slider_metric = tk.Scale(right, orient='horizontal')  # Curseur pour ajuster la taille
slider_metric.pack()
slider_metric.set(10)
send_button = tk.Button(right,text='Envoyer',command=lambda:Score(lettre, points, slider_metric))  # Bouton d'envoi
send_button.pack()
show_button = tk.Button(right,text='Afficher le barème', command=lambda:bareme_scrabble(slider_metric))  # Bouton du barème
show_button.pack()
right.grid(column=1, row=0)                       # Placer le frame sur la grille

tt.listen()                                       # Écouter les événements
tt.mainloop();root.mainloop()                     # Lancer les deux boucles principales
