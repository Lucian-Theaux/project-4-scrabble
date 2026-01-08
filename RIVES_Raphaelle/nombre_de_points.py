import turtle as tt                                                 # Importation du module turtle pour le dessin
import tkinter as tk                                                # Importation du module tkinter pour l'interface graphique
from RIVES_Raphaelle.search import recherche                            # Importation de la fonction de recherche de mot
from Lucian_Theaux.tuiles import tuile, letter_impression         # Importation des fonctions d'affichage des tuiles    
from Lucian_Theaux.calcul_score import ajout_score, scoreboard              # Importation des fonctions de calcul et d'affichage du score
from RIVES_Raphaelle.dictionnaire_lettres import points                  # Importation du dictionnaire de points    

def double(lettre : str, points : dict) -> str :
    """
    double: Prend en entrée le mot que l'on cherche et le dictionnaire de point, elle renvoie ensuite le score du mot demandé multiplié par deux si le mot est valide.
    """
    verification =Score(lettre, points)                             # On utilise la fonction Score pour vérifier si le mot est valide et obtenir son score
    if verification != None:                                # Si le mot est validé:
        res = verification[0]*2                             # On double le score
        tt.write('Le mot %s compte double, il vaut %s pts.' % (lettre, res), font =('Calibri', 16, 'italic'))           # On affiche le résultat
    else:
        tt.write('Erreur', font =('Calibri', 16, 'italic'))         # On affiche une erreur si le mot n'est pas valide

def Score(lettre : str, points : dict, slider_metric :int) -> str :
    """
    Score: Prend en entrée le mot que l'on cherche et le dictionnaire de point, elle renvoie ensuite: 
           - Si le mot se trouve dans la liste du Scrabble, son score et sa position dans la liste sous forme de tuple, elle ajoute ensuite le score et le mot dans le fichier scores.txt.
           - Si le mot n'est pas dans la liste du Scrabble, None. 

    - mot : Prend en entrée le mot que l'on cherche sous forme de string
    - points : Prend en entrée le dictionnaire de point, officiel ou personnalisé
    """
    resultat = 0                        # Initialisation du score à 0
    mot = lettre.get()           # Récupération du mot entré par l'utilisateur
    mot = mot.upper()                   # Mise en majuscule du mot pour correspondre aux clés du dictionnaire
    metric = slider_metric.get()                # Récupération de la taille des tuiles à dessiner

    verif, index = recherche(mot)               # Utilisation de la fonction recherche pour vérifier si le mot est dans la liste

    if verif:                       # Si le mot est trouvé dans la liste:
        for car in mot:                 # Pour chaque caractère du mot:
            resultat = resultat + points[car]               # On ajoute le point correspondant à la lettre au score total
        ajout_score(resultat,mot)                   # On ajoute le score et le mot au fichier scores.txt
        letter_impression(slider_metric, lettre)                # On affiche les tuiles du mot 
        tt.up()
        tt.goto(-200,-200)                          # Positionnement pour afficher le score
        tt.setheading(0)                            # Orientation de la tortue
        tt.down()
        tt.write(f'valeur {mot}: {resultat}pts', font=('Arial', 30, 'bold'))            # Affichage du score
    else:               # Si le mot n'est pas trouvé dans la liste:
        tt.up()
        tt.goto(-50,-200)
        tt.setheading(0)
        tt.down()
        tt.write(f'Le mot {mot} ne fait pas parti de la liste règlementaire...', font=('Arial', 16, 'bold'))                # Affichage du message d'erreur si le mot n'est pas valide
        return None                  # On renvoie None pour indiquer que le mot n'est pas valide
    historique()
    
def historique():
    """
    fonction historique qui affiche les 10 derniers mots
    """
    historique_list=[]                                          # liste vide pour stocker les scores
    F = open('scores.txt','r', encoding='utf-8')                # ouverture du fichier en mode lecture
    historique_list = F.read().split('\n')                      # lecture du fichier et séparation des lignes
    F.close()                                               # fermeture du fichier
    while len(historique_list) >10:                         # tant que la liste contient plus de 10 éléments on affiche les 10 derniers mots et scores
      historique_list.remove(historique_list[0]) 
    tt.up()
    tt.goto(300,100)                                        # positionnement pour afficher l'historique 
    tt.down() 
    tt.write('Historique des 10 derniers: \n'+'\n'.join(historique_list), font=('Arial', 16, 'italic'))             # affichage des 10 derniers scores

