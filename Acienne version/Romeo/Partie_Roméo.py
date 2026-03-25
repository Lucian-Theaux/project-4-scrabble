# coding=utf-8
#* Projet réalisé par :
#* Roméo HUYNH

# Imports des modules nécessaires
import turtle as tt
import tkinter as tk
from RIVES_Raphaelle.search import recherche
from Lucian_Theaux.tuiles import tuile, letter_impression
from Lucian_Theaux.calcul_score import ajout_score, scoreboard
from RIVES_Raphaelle.dictionnaire_lettres import points
from RIVES_Raphaelle.nombre_de_points import Score
from Romeo.bareme_points import bareme_scrabble
import time


# ==================== Configuration initiale ====================

tt.title("Projet_4 Scrabble")    # Titre de la fenêtre Turtle
tt.hideturtle()                 # Cacher le curseur de la tortue
tt.down()                   # Abaisser le stylo pour commencer à dessiner
tt.screensize(1.0, 1.0)        # Configurer la fenêtre graphique Turtle en plein écran
tt.speed(0)                    # Régler la vitesse de dessin au maximum

# Créer la fenêtre principale Tkinter
root = tk.Tk()

# ==================== Interface graphique ====================

# Configurer les titres des fenêtres
tt.title('Scrabble.io')
tt.setup(1.0, 1.0)
root.title('Scrabble.io')

# ==================== Zone d'interaction utilisateur ====================

# Créer un frame pour la zone de saisie
right = tk.Frame(root)

# Label pour indiquer à l'utilisateur d'entrer un mot
input_label = tk.Label(right, text='Entrer un mot (sans parenthèses):')
input_label.pack()

# Champ de saisie pour le mot
lettre = tk.Entry(right)
lettre.insert(0, 'exemple: tortue')
lettre.pack()

# Curseur pour ajuster la taille des tuiles
slider_metric = tk.Scale(right, orient='horizontal')
slider_metric.pack()
slider_metric.set(10)

# Bouton pour envoyer le mot et afficher les tuiles
send_button = tk.Button(right, text='Envoyer', command=lambda: letter_impression(slider_metric, lettre, points))
send_button.pack()

# Bouton pour afficher le barème des points
show_button = tk.Button(right, text='Afficher le barème', command=bareme_scrabble)
show_button.pack()

# Placer le frame sur la grille
right.grid(column=1, row=0)

# ==================== Lancer l'application ====================

# Écouter les événements de la souris et du clavier
tt.listen()

# Lancer les deux boucles principales (Turtle et Tkinter)
tt.mainloop()
root.mainloop()