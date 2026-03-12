import turtle
import os

screen = turtle.Screen()
screen.setup(900, 900)

# Récupération du dossier courant
dossier = os.path.dirname(__file__)

# Chemin vers l'image
chemin_fichier = os.path.join(dossier, "image_plateau.gif")

# Image de fond
screen.bgpic(chemin_fichier)

turtle.mainloop()