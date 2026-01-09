# projet Decembre groupe 4
# coding=utf-8
# Projet réalisé par :
#* Lucian THEAUX
#* Raphaëlle RIVES
#* Roméo HUYNH

"""Ici on importe les fichiers nécéssaires pour le projet"""
import turtle as tt
import tkinter as tk
from Lucian_Theaux.tuiles import tuile, letter_impression
from Lucian_Theaux.calcul_score import ajout_score, scoreboard
from RIVES_Raphaelle.dictionnaire_lettres import points
from RIVES_Raphaelle.search import recherche
from RIVES_Raphaelle.nombre_de_points import Score, double, quadruple, nonuple, gros_bonus, historique
from Romeo_HUYNH.bareme_points import bareme_scrabble

#* -------------- Paramètres utiles --------------------

"""Ici on initialise quelques paramètres utiles"""
tt.title("Projet_4 Scrabble")                     # Titre de la fenêtre Turtle
tt.speed(8)                                       # Régler la vitesse initiale
tt.hideturtle()                                   # Cacher le curseur de la tortue
tt.down()                                         # Abaisser le stylo pour commencer à dessiner
tt.speed(0)                                       # Régler la vitesse de dessin au maximum

root = tk.Tk()

#──────────────────── Interface graphique (faite par Raphaëlle) ─────────────────
tt.title('Scrabble.io')                           # Titre de la fenêtre Turtle
tt.setup(1.0,1.0)                                 # Configurer la taille de la fenêtre Turtle
root.title('Interface.utilisateur')                         # Titre de la fenêtre Tkinter
root.geometry(('300x150'))                          # Taille de la fenêtre Tkinter.utilisateur

historique()                                     # Afficher l'historique des 10 derniers mots

# ────────────────── Zone d’interaction (faite par le groupe)────────────────────
right = tk.Frame(root)                            # Créer un frame pour la zone de saisie Tkinter: crée une colonne à droite
left = tk.Frame(root)                             # Créer un frame pour la zone d'affichage Tkinter: crée une colonne à gauche
input_label = tk.Label(right,text='Entrer un mot (sans accents):')  # Label pour indiquer à l'utilisateur d'entrer un mot
input_label.pack()                                # Placer le label dans le frame
lettre = tk.Entry(right)                          # Champ de saisie pour le mot
lettre.insert(0, 'exemple: tortue')               # Texte d'exemple
lettre.pack()
slider_metric = tk.Scale(right, orient='horizontal')  # Curseur pour ajuster la taille
slider_metric.pack()
slider_metric.set(10)                               # Valeur initiale du curseur
send_button = tk.Button(right,text='Envoyer',command=lambda:Score(lettre, points, slider_metric))  # Bouton d'envoi
send_button.pack()
send_button2 = tk.Button(left,text='Mot compte double',command=lambda:double(lettre, points, slider_metric))  # Bouton mot compte double
send_button2.pack()
send_button3 = tk.Button(left,text='x 4',command=lambda:quadruple(lettre, points, slider_metric))  # Bouton score du mot x 4
send_button3.pack()
send_button4 = tk.Button(left,text='x 9',command=lambda:nonuple(lettre, points, slider_metric))  # Bouton score du mot x 9
send_button4.pack()
send_button5 = tk.Button(left,text='x 27',command=lambda:gros_bonus(lettre, points, slider_metric))  # Bouton score du mot x 27
send_button5.pack()
show_button = tk.Button(right,text='Afficher le barème', command=lambda:bareme_scrabble(slider_metric))  # Bouton du barème
show_button.pack()
right.grid(column=1, row=0)                       # On initialiser "droite" à la colonne 1, ligne 0.  "droite" sera en paramètre pour les widgets
left.grid(column=2, row=0)                        # Idemme avec "gauche"

tt.listen()                                       # Écouter les événements (par exemple les clics de souris ou les frappes clavier)
tt.mainloop();root.mainloop()                     # Lancer les deux boucles principales