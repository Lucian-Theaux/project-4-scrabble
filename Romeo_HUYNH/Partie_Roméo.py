# coding=utf-8
#* Projet réalisé par :
#* Roméo HUYNH

# Imports des modules nécessaires
import sys                              # Pour manipuler les chemins d'accès
import os                       # Pour les opérations liées au système d'exploitation
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))                 # Ajouter le répertoire parent au chemin d'accès
                                        # Permet d'importer des modules situés dans des répertoires parents
import turtle as tt                     # Pour la création de l'interface graphique avec Turtle
import tkinter as tk                    # Pour la création de l'interface graphique avec Tkinter
from RIVES_Raphaelle.search import recherche                # Pour la recherche de mots dans le dictionnaire
from Lucian_Theaux.tuiles import tuile, letter_impression   # Pour la gestion des tuiles et l'impression des lettres    
from Lucian_Theaux.calcul_score import ajout_score, scoreboard          # Pour le calcul et l'affichage du score
from RIVES_Raphaelle.dictionnaire_lettres import points             # Pour obtenir les points associés aux lettres
from RIVES_Raphaelle.nombre_de_points import Score          # Pour le calcul du score total     
from Romeo_HUYNH.bareme_points import bareme_scrabble           # Pour afficher le barème des points du Scrabble


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
input_label = tk.Label(right, text='Entrer un mot (sans parenthèses):')                         # Label d'instruction pour l'utilisateur
input_label.pack()                                                                              # Placer le label dans le frame

# Champ de saisie pour le mot
lettre = tk.Entry(right)                                    # Champ de saisie pour entrer le mot
lettre.insert(0, 'exemple: tortue')                     # Texte par défaut dans le champ de saisie
lettre.pack()

# Curseur pour ajuster la taille des tuiles
slider_metric = tk.Scale(right, orient='horizontal')                    # Curseur horizontal pour ajuster la taille des tuiles
slider_metric.pack()
slider_metric.set(10)                                                   # Valeur par défaut du curseur

# Bouton pour envoyer le mot et afficher les tuiles
send_button = tk.Button(right, text='Envoyer', command=lambda: letter_impression(slider_metric, lettre))                    # Bouton pour envoyer le mot et afficher les tuiles
send_button.pack()

# Bouton pour afficher le barème des points
show_button = tk.Button(right, text='Afficher le barème', command=lambda: bareme_scrabble(slider_metric))                   # Bouton pour afficher le barème des points
show_button.pack()

# Placer le frame sur la grille
right.grid(column=1, row=0)                                                 # Placer le frame à la colonne 1, ligne 0

# ==================== Lancer l'application ====================

# Lancer la boucle d'événements Tkinter
root.mainloop()