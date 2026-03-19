# projet Decembre groupe 4
# coding=utf-8
# Projet réalisé par :
#* Lucian THEAUX
#* Raphaëlle RIVES
#* Roméo HUYNH

"""Ici on importe les fichiers nécéssaires pour le projet"""
import turtle as tt
import tkinter as tk
# from Lucian_Theaux.tuiles import tuile, letter_impression
# from Lucian_Theaux.calcul_score import ajout_score, scoreboard
# from RIVES_Raphaelle.dictionnaire_lettres import points
# from RIVES_Raphaelle.search import recherche
# from RIVES_Raphaelle.nombre_de_points import Score, double, quadruple, nonuple, gros_bonus, historique
# from Romeo_HUYNH.bareme_points import bareme_scrabble

#* -------------- Paramètres utiles --------------------

# """Ici on initialise quelques paramètres utiles"""
# tt.title("Projet_4 Scrabble")                     # Titre de la fenêtre Turtle
# tt.speed(8)                                       # Régler la vitesse initiale
# tt.hideturtle()                                   # Cacher le curseur de la tortue
# tt.down()                                         # Abaisser le stylo pour commencer à dessiner
# tt.speed(0)                                       # Régler la vitesse de dessin au maximum

root = tk.Tk()

#──────────────────── Interface graphique (faite par Raphaëlle) ─────────────────
# tt.title('Scrabble.io')                           # Titre de la fenêtre Turtle
# tt.setup(1.0,1.0)                                 # Configurer la taille de la fenêtre Turtle
# root.title('Interface.utilisateur')                         # Titre de la fenêtre Tkinter
# root.geometry(('300x150'))                          # Taille de la fenêtre Tkinter.utilisateur

# historique()                                     # Afficher l'historique des 10 derniers mots

# ────────────────── Zone d’interaction (faite par le groupe)────────────────────
gauche = tk.Frame(root)                            # Créer un frame pour la zone de saisie Tkinter: crée une colonne à droite
droite = tk.Frame(root)                             # Créer un frame pour la zone d'affichage Tkinter: crée une colonne à gauche
coordonnée = tk.Frame(root)
horizontal_vertical = tk.Frame(root)

input_label = tk.Label(gauche,text='Entrer un mot (sans accents):')  # Label pour indiquer à l'utilisateur d'entrer un mot
input_label.pack()                                # Placer le label dans le frame
lettre = tk.Entry(gauche)                          # Champ de saisie pour le mot
lettre.insert(0, 'exemple: tortue')               # Texte d'exemple
lettre.pack()
slider_metric = tk.Scale(gauche, orient='horizontal')  # Curseur pour ajuster la taille
slider_metric.pack()
slider_metric.set(10)                               # Valeur initiale du curseur
send_button = tk.Button(gauche,text='Envoyer',command=lambda:Score(lettre, points, slider_metric))  # Bouton d'envoi
send_button.pack()

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

lettre = tk.Entry(coordonnée)                          # Champ de saisie pour le mot
lettre.insert(0, '"2 3 (min 0 | max 14)"')               # Texte d'exemple
lettre.grid(row=1)
horizontal_button = tk.Button(horizontal_vertical, text=" → ", anchor="center")
horizontal_button.grid(column=1,row=2)
vertical_button = tk.Button(horizontal_vertical, text=" ↓ ", anchor="center")
vertical_button.grid(column=2,row=2)

gauche.grid(column=1, row=0)                       # On initialiser "droite" à la colonne 1, ligne 0.  "droite" sera en paramètre pour les widgets
droite.grid(column=2, row=0)                        # Idemme avec "gauche"
coordonnée.grid(column=1, row=1)
horizontal_vertical.grid(column=1,row=2)

tt.listen()                                       # Écouter les événements (par exemple les clics de souris ou les frappes clavier)
tt.mainloop();root.mainloop()  