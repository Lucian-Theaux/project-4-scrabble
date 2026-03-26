# projet Decembre groupe 4
# coding=utf-8
# Projet réalisé par :
#* Lucian THEAUX
#* Raphaëlle RIVES
#* Roméo HUYNH

# -------------------- Ici on importe les fichiers nécéssaires pour le projet --------------------
import tkinter as tk
from tkinter import PhotoImage
import turtle as tt
import os
import verification as verif
import scrabble as scrabble

# -------------------- Initialisation du plateau --------------------
set_couleur = {                 # Dictionnaire qui associe à chaque type de case une couleur
    '  ':"#D5B486",
    'MT':"#c7291d",
    'LD':"#9daec5",
    'MD':"#deb364",
    'E':"#d9a751",
    'LT':"#348dbc"
}

plateau = scrabble.creation_plateau()          # Création de la variable qui va contenir la "matrice" contenant le plateau
plateau_bonus = [['MT', '  ', '  ', 'LD', '  ', '  ', '  ', 'MT', '  ', '  ', '  ', 'LD', '  ', '  ', 'MT'],  # Matrice 15x15 contenant les bonus de chaque case
                 ['  ', 'MD', '  ', '  ', '  ', 'LT', '  ', '  ', '  ', 'LT', '  ', '  ', '  ', 'MD', '  '], 
                 ['  ', '  ', 'MD', '  ', '  ', '  ', 'LD', '  ', 'LD', '  ', '  ', '  ', 'MD', '  ', '  '], 
                 ['LD', '  ', '  ', 'MD', '  ', '  ', '  ', 'LD', '  ', '  ', '  ', 'MD', '  ', '  ', 'LD'], 
                 ['  ', '  ', '  ', '  ', 'MD', '  ', '  ', '  ', '  ', '  ', 'MD', '  ', '  ', '  ', '  '], 
                 ['  ', 'LT', '  ', '  ', '  ', 'LT', '  ', '  ', '  ', 'LT', '  ', '  ', '  ', 'LT', '  '], 
                 ['  ', '  ', 'LD', '  ', '  ', '  ', 'LD', '  ', 'LD', '  ', '  ', '  ', 'LD', '  ', '  '], 
                 ['MT', '  ', '  ', 'LD', '  ', '  ', '  ', 'E' , '  ', '  ', '  ', 'LD', '  ', '  ', 'MT'],  # E = case départ (étoile)
                 ['  ', '  ', 'LD', '  ', '  ', '  ', 'LD', '  ', 'LD', '  ', '  ', '  ', 'LD', '  ', '  '], 
                 ['  ', 'LT', '  ', '  ', '  ', 'LT', '  ', '  ', '  ', 'LT', '  ', '  ', '  ', 'LT', '  '], 
                 ['  ', '  ', '  ', '  ', 'MD', '  ', '  ', '  ', '  ', '  ', 'MD', '  ', '  ', '  ', '  '], 
                 ['LD', '  ', '  ', 'MD', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'MD', '  ', '  ', 'LD'], 
                 ['  ', '  ', 'MD', '  ', '  ', '  ', 'LD', '  ', 'LD', '  ', '  ', '  ', 'MD', '  ', '  '], 
                 ['  ', 'MD', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'MD', '  '], 
                 ['MT', '  ', '  ', 'LD', '  ', '  ', '  ', 'MT', '  ', '  ', '  ', 'LD', '  ', '  ', 'MT']]

# -------------------- Initialisation de la fenêtre turtle --------------------

screen = tt.Screen()
screen.setup(1112, 712)                     #On définit la taille de la fenêtre afin que le plateau et l'historique puisse être affiché correctement

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
    """application_horizontal: fonction qui va être appelée lorsque l'utilisateur clique sur le bouton de placement horizontal. Elle vérifie que le mot peut être placé à l'endroit voulu et dans la direction voulue, puis elle ajoute le mot au plateau et affiche les tuiles correspondantes."""
    mot = ""
    for letter in lettre.get(): mot+=letter.capitalize()  # Convertir chaque lettre en majuscule

    mot = mot.upper()                           # Mettre le mot en majuscule pour la comparaison
    i = 1                                       # Initialisation de l'index   
    dossier = os.path.dirname(__file__)         # Récupération du dossier courant
    chemin_fichier = os.path.join(dossier, "mots_autorises.txt")  # Construction du chemin complet vers le fichier
    with open(chemin_fichier, "r", encoding="utf-8") as F:        # Ouverture du fichier en mode lecture avec encodage utf-8
        for ligne in F:                         # Parcours de chaque ligne du fichier
            if ligne[:-1] == mot:               # Comparaison du mot (enlevant le caractère de nouvelle ligne)
                autorise = True              # Si le mot est trouvé, renvoyer True 
            i += 1
        autorise == False                   # Si le mot n'est pas trouvé, renvoyer False 

    if autorise == False: # Si il y a refus on envoie un message d'alerte que le mot n'existe pas et on casse la fonction
        print("Votre mot n'est pas présent dans la liste des mots autorisés.")
        return None

    positions = lettre_coo.get().split(' ')  # Récupérer les coordonnées saisies (x et y)
    verification = verif.verification_place(plateau,y=int(positions[1]),x=int(positions[0]),direction="horizontal",mot=mot)             # On vérifie que le mot peut être placé à l'endroit voulu et dans la direction voulue   
    if verification == True:
        seconde_verification = verif.verification_mot_horizontal(plateau,y=int(positions[1]),x=int(positions[0]),mot=mot)      # On vérifie que le mot s'aligne correctement avec les autres mots déjà présents sur le plateau
        if seconde_verification==True:
            scrabble.ajout_mot_horizontal(x=int(positions[0]),y=int(positions[1]),mot=mot,plateau=plateau)          # On ajoute le mot au plateau
            tt.penup()
            tt.goto((int(positions[0])*47.47)-(1112/2),(712/2)-(47.47*int(positions[1]))-47.47)             # On se place à l'endroit où le mot doit être placé
            i = 0  # Index de la lettre dans le mot
            for letter in mot:  # Pour chaque lettre du mot
                couleur = set_couleur[plateau_bonus[int(positions[0])+i][int(positions[1])]]  # Couleur de la case bonus
                tt.setheading(0)  # Orientation horizontale
                tuile(letter, couleur)  # Dessiner la tuile de la lettre
                tt.setheading(0)  # Réorienter
                tt.penup()  # Lever le stylo pour avancer
                i += 1  # Passer à la lettre suivante

            with open('Scrabble Trophée NSI/historique.txt', 'a',encoding='utf-8') as fichier:  # Ouvrir l'historique en mode ajout
                fichier.write(f'{mot}\n')  # Ajouter le mot joué
            
            historique_list=[]                              # liste vide pour stocker les scores
            F = open('Scrabble Trophée NSI/historique.txt','r', encoding='utf-8')    # ouverture du fichier en mode lecture
            historique_list = F.read().split('\n')          # lecture du fichier et séparation des lignes
            F.close()                                       # fermeture du fichier
            while len(historique_list) > 20:                 # tant que la liste contient plus de 10 éléments on affiche les 10 derniers mots et scores
                historique_list.remove(historique_list[0])    # on supprimee mot le plus ancien (1er de la liste) quand un nouveau est ajouté
            
            tt.goto(220, 356-(47.47+40))  # Positionner pour l'historique
            tt.setheading(0)
            tt.fillcolor('white')
            tt.begin_fill()
            tt.fd(400)
            tt.rt(90)
            tt.fd(200)
            tt.rt(90)
            tt.fd(400)
            tt.rt(90)
            tt.fd(200)
            tt.rt(90)
            tt.end_fill()
            tt.goto(220, 356-(47.47+60))  # Positionner pour l'historique
            tt.setheading(270)  # Orientation vers le bas
            for ligne in historique_list:  # Afficher chaque mot de l'historique
                if ligne == '':  # Ignorer les lignes vides
                    pass
                tt.write(f'{ligne}', font=('Arial',15,'italic'))  # Écrire le mot
                tt.fd(15)  # Descendre à la ligne suivante
            
            longueur_mot_range = sorted(historique_list, key=len)  # Trier par longueur
            longueur_mot_range = longueur_mot_range[::-1]  # Inverser pour mettre le plus long d'abord
                
            tt.goto(220, -(47.47+40))  # Position scoreboard
            tt.setheading(0)
            tt.fillcolor('white')
            tt.begin_fill()
            for i in range(4):
                tt.fd(500)
                tt.rt(90)
            tt.end_fill()
            tt.goto(220, -(47.47+60))  # Position scoreboard
            tt.setheading(270)  # Bas
            tt.fillcolor('black')
            print(longueur_mot_range)
            i = 0
            for elem in longueur_mot_range:  #parcourir les mots
                if i > 20:
                    break
                tt.write(f'{elem}', font=('Arial',15,'italic'))  # Écrire le mot trié
                tt.fd(15)  # Descendre
                i += 1

    else:
        print(verification)

def application_vertical():
    """application_vertical: fonction qui va être appelée lorsque l'utilisateur clique sur le bouton de placement vertical. Elle vérifie que le mot peut être placé à l'endroit voulu et dans la direction voulue, puis elle ajoute le mot au plateau et affiche les tuiles correspondantes."""
    mot = ""  # Initialisation du mot en majuscules
    for letter in lettre.get(): mot+=letter.capitalize()  # Construire le mot

    mot = mot.upper()                           # Mettre le mot en majuscule pour la comparaison
    i = 1                                       # Initialisation de l'index   
    dossier = os.path.dirname(__file__)         # Récupération du dossier courant
    chemin_fichier = os.path.join(dossier, "mots_autorises.txt")  # Construction du chemin complet vers le fichier
    with open(chemin_fichier, "r", encoding="utf-8") as F:        # Ouverture du fichier en mode lecture avec encodage utf-8
        for ligne in F:                         # Parcours de chaque ligne du fichier
            if ligne[:-1] == mot:               # Comparaison du mot (enlevant le caractère de nouvelle ligne)
                autorise = True              # Si le mot est trouvé, renvoyer True 
            i += 1
        autorise == False                   # Si le mot n'est pas trouvé, renvoyer False 

    if autorise == False: # Si il y a refus on envoie un message d'alerte que le mot n'existe pas et on casse la fonction
        print("Votre mot n'est pas présent dans la liste des mots autorisés.")
        return None
    
    positions = lettre_coo.get().split(' ')  # Extraire x et y
    verification = verif.verification_place(plateau,y=int(positions[1]),x=int(positions[0]),direction="vertical",mot=mot)            # Vérifier que le mot peut être placé à cet endroit et dans cette direction
    if verification == True:
        seconde_verification = verif.verification_mot_vertical(plateau,y=int(positions[1]),x=int(positions[0]),mot=mot)             # Vérifier que le mot s'aligne correctement avec les autres mots déjà présents sur le plateau
        if seconde_verification == True:
            scrabble.ajout_mot_vertical(x=int(positions[0]),y=int(positions[1]),mot=mot,plateau=plateau)        # Ajouter le mot au plateau
            tt.penup()
            tt.goto((int(positions[0])*47.47)-(1112/2),(712/2)-(47.47*int(positions[1]))-47.47)         # Se positionner pour dessiner le mot
            i = 0                               # Index de la 1ere lettre dans le mot
            for letter in mot:
                couleur = set_couleur[plateau_bonus[int(positions[0])][int(positions[1])+i]]        # Couleur de la case bonus
                tt.setheading(0)
                tuile(letter, couleur)                  # Dessiner la tuile de la lettre
                tt.penup()
                tt.setheading(270)
                tt.fd(47.47)
                tt.rt(90)
                tt.fd(47.47)
                tt.setheading(0)
                tt.penup()
                i += 1                  # Passer à la lettre suivante

            with open('Scrabble Trophée NSI/historique.txt', 'a',encoding='utf-8') as fichier:  # Ouvrir l'historique en mode ajout
                fichier.write(f'{mot}\n')  # Ajouter le mot joué
            
            historique_list=[]                              # liste vide pour stocker les scores
            F = open('Scrabble Trophée NSI/historique.txt','r', encoding='utf-8')    # ouverture du fichier en mode lecture
            historique_list = F.read().split('\n')          # lecture du fichier et séparation des lignes
            F.close()                                       # fermeture du fichier
            while len(historique_list) > 20:                 # tant que la liste contient plus de 10 éléments on affiche les 10 derniers mots et scores
                historique_list.remove(historique_list[0])    # on supprimee mot le plus ancien (1er de la liste) quand un nouveau est ajouté
            
            tt.goto(220, 356-(47.47+40))  # Positionner pour l'historique
            tt.setheading(0)
            tt.fillcolor('white')
            tt.begin_fill()
            tt.fd(400)
            tt.rt(90)
            tt.fd(200)
            tt.rt(90)
            tt.fd(400)
            tt.rt(90)
            tt.fd(200)
            tt.rt(90)
            tt.end_fill()
            tt.goto(220, 356-(47.47+60))  # Positionner pour l'historique
            tt.setheading(270)  # Orientation vers le bas
            for ligne in historique_list:  # Afficher chaque mot de l'historique
                if ligne == '':  # Ignorer les lignes vides
                    pass
                tt.write(f'{ligne}', font=('Arial',15,'italic'))  # Écrire le mot
                tt.fd(15)  # Descendre à la ligne suivante
            
            longueur_mot_range = sorted(historique_list, key=len)  # Trier par longueur
            longueur_mot_range = longueur_mot_range[::-1]  # Inverser pour mettre le plus long d'abord
                
            tt.goto(220, -(47.47+40))  # Position scoreboard
            tt.setheading(0)
            tt.fillcolor('white')
            tt.begin_fill()
            for i in range(4):
                tt.fd(500)
                tt.rt(90)
            tt.end_fill()
            tt.goto(220, -(47.47+60))  # Position scoreboard
            tt.setheading(270)  # Bas
            tt.fillcolor('black')
            print(longueur_mot_range)
            i = 0
            for elem in longueur_mot_range:  #parcourir les mots
                if i > 20:
                    break
                tt.write(f'{elem}', font=('Arial',15,'italic'))  # Écrire le mot trié
                tt.fd(15)  # Descendre
                i += 1

        else:
            print("Votre ne peut pas rentrer sur le plateau, il ne s'aligne pas avec les autres tuiles")

    else:
        print(verification)


def tuile(ltr:str,couleur:str):
    """
    tuile: crée une tuile affichant la lettre et le score de cette même lettre
    - ltr: Prend en entré une chaine de caractère de une seule lettre
    """
    global plateau_bonus  # Accès à la matrice des bonus
    tt.pendown()  # Baisser le stylo pour dessiner
    metric = 47.47  # Taille d'une tuile en pixels
    points = {"A":1 ,"E":1 ,"I":1 ,"L":1 ,"N":1 ,"O":1 ,"R":1 ,"S":1 ,"T":1 ,"U":1 ,"D":2 ,"G":2 ,"M":2 ,"B":3 ,"C":3 ,"P":3 ,"F":4 ,"H":4 ,"V":4 ,"J":8 ,"Q":8 ,"K":10 ,"W":10 ,"X":10 ,"Y":10 ,"Z":10}  # Points Scrabble par lettre
    tt.pencolor('black')                    # Couleur du contour de la tuile: noir
    tt.fillcolor(couleur)                 # Couleur de remplissage de la tuile
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
        tt.write(points[ltr], font=('Arial', 10))   # Écriture du score de la lettre    
        tt.fd((2*metric)/7)                       # Repositionnement après l'écriture du score
    else:                       # Si le score de la lettre est inférieur à 10...
        tt.fd((4*metric)/7)
        tt.write(points[ltr], font=('Arial', 10))        # Écriture du score avec petite police
        # Repositionnement après l'écriture
        tt.fd((2*metric)/7)
    tt.pendown()

def bareme_scrabble():
    fen_bareme = tk.Toplevel()  # Créer fenêtre barème secondaire
    fen_bareme.geometry('700x445')  # Définir taille
    image_bareme = PhotoImage(file='Scrabble Trophée NSI/bareme.png') #Definir une image à associer
    image_label = tk.Label(fen_bareme, image=image_bareme) # Associer cette image à un Label
    image_label.pack() # On transforme en paquet le label pour pouvoir afficher l'image sur la fenêtre
    description = tk.Label(fen_bareme,text="Beige → 1pt | Orange → 2 pts | Orange-rouge → 3pts | \nRouge-clair → 4pts | Rouge → 8pts | Rouge-foncé → 10pts", font=('Arial',13,'italic')) # Description associée à l'image du dessus
    description.pack()
    fen_bareme.mainloop()  # Lancer la fenêtre

# -------------------- Zone d’interaction (faite par le groupe) --------------------

gauche = tk.Frame(root)                            # Créer un frame pour la zone de saisie Tkinter: crée une colonne à droite
droite = tk.Frame(root)                             # Créer un frame pour la zone d'affichage Tkinter: crée une colonne à gauche
coordonnée = tk.Frame(root)  # Frame pour les coordonnées
horizontal_vertical = tk.Frame(root)  # Frame pour les boutons de direction

input_label = tk.Label(gauche,text='Entrer un mot (sans accents):')  # Label pour indiquer à l'utilisateur d'entrer un mot
input_label.pack()                                # Placer le label dans le frame
lettre = tk.Entry(gauche)                          # Champ de saisie pour le mot
lettre.insert(0, 'exemple: tortue')               # Texte d'exemple
lettre.pack()

show_button = tk.Button(gauche,text='Afficher le barème', command=lambda:bareme_scrabble())  # Bouton du barème
show_button.pack()

lettre_coo = tk.Entry(coordonnée)                          # Champ de saisie pour le mot
lettre_coo.insert(0, '0 0')                                # Texte d'exemple
lettre_coo.grid(row=1)  # Placer dans la grille
horizontal_button = tk.Button(horizontal_vertical, text=" → ", command=lambda:application_horizontal())  # Bouton placement horizontal
horizontal_button.grid(column=1,row=2)  # Position dans grille
vertical_button = tk.Button(horizontal_vertical, text=" ↓ ", command=lambda:application_vertical())  # Bouton placement vertical
vertical_button.grid(column=2,row=2)  # Position

gauche.grid(column=1, row=0)                       # On initialiser "droite" à la colonne 1, ligne 0.  "droite" sera en paramètre pour les widgets
droite.grid(column=2, row=0)                        # Idemme avec "gauche"
coordonnée.grid(column=1, row=1)  # Placer frame coordonnées
horizontal_vertical.grid(column=1,row=2)  # Placer frame boutons

# -------------------- Mise en place des éléments turtle sur la fenêtre --------------------

# --- 1. La numérotation des cases ---
tt.penup()
tt.fd(170)
tt.lt(90)
tt.fd(356-(47.47*0.7))
tt.setheading(270)
for i in range(15):  # Numéroter les lignes 0 à 14
    tt.write(i, font=('Arial',20))  # Écrire le numéro
    tt.fd(47.47)  # Avancer à la ligne suivante

# --- 2. Titre "Historique" ---
tt.penup()
tt.goto(220, 356-(47.47+30))  # Position titre historique
tt.write("Historique", font=('Arial',40,"bold"))  # Écrire le titre

# --- 2. Titre "Scoreboard" ---
tt.penup()
tt.goto(220, -(47.47+30))  # Position titre scoreboard
tt.write("Scoreboard", font=('Arial',40,"bold"))  # Écrire le titre

root.mainloop();tt.mainloop()  # Démarrer les boucles d'événements Tkinter et Turtle
