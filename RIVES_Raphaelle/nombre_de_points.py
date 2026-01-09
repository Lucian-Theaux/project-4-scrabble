#projet Decembre Raphaëlle Rives 1ere4

import turtle as tt                                               # Importation du module turtle pour le dessin
import tkinter as tk                                              # Importation du module tkinter pour l'interface graphique
from RIVES_Raphaelle.search import recherche                      # Importation de la fonction de recherche de mot
from Lucian_Theaux.tuiles import tuile, letter_impression         # Importation des fonctions d'affichage des tuiles    
from Lucian_Theaux.calcul_score import ajout_score, scoreboard    # Importation des fonctions de calcul et d'affichage du score
from RIVES_Raphaelle.dictionnaire_lettres import points           # Importation du dictionnaire de points    


def Score(lettre : str, points : dict, slider_metric :int) -> str :
    """
    Score: Prend en entrée le mot que l'on cherche et le dictionnaire de point, elle renvoie ensuite: 
           - Si le mot se trouve dans la liste du Scrabble, son score et sa position dans la liste sous forme de tuple, elle ajoute ensuite le score et le mot dans le fichier scores.txt.
           - Si le mot n'est pas dans la liste du Scrabble, None. 

    - mot : Prend en entrée le mot que l'on cherche sous forme de string
    - points : Prend en entrée le dictionnaire de point, officiel ou personnalisé
    """
    resultat = 0                    # Initialisation du score à 0
    mot = lettre.get()              # Récupération du mot entré par l'utilisateur
    mot = mot.upper()               # Mise en majuscule du mot pour correspondre aux clés du dictionnaire
    metric = slider_metric.get()    # Récupération de la taille des tuiles à dessiner

    verif, index = recherche(mot)   # Utilisation de la fonction recherche pour vérifier si le mot est dans la liste

    if verif:                       # Si le mot est trouvé dans la liste:
        for car in mot:             # Pour chaque caractère du mot:
            resultat = resultat + points[car]       # On ajoute le point correspondant à la lettre au score total
        ajout_score(resultat,mot)                   # On ajoute le score et le mot au fichier scores.txt
        letter_impression(slider_metric, lettre)    # On affiche les tuiles du mot 
        tt.up()
        tt.goto(-200,-150)                          # Positionnement pour afficher le score
        tt.setheading(0)                            # Orientation de la tortue
        tt.down()
        tt.write(f'valeur de {mot}: {resultat}pts', font=('Arial', 30, 'bold'))  # Affichage du score
        historique()                # on affiche l'historique des 10 derniers mots
        return resultat             # On renvoie le score du mot dans la liste
    else:                           # Si le mot n'est pas trouvé dans la liste:
        tt.up()
        tt.goto(-50,-200)
        tt.setheading(0)
        tt.down()
        tt.write(f'Le mot {mot} ne fait pas parti de la liste règlementaire...', font=('Arial', 16, 'bold'))  # Affichage du message d'erreur si le mot n'est pas valide
        historique()                # on affiche l'historique des 10 derniers mots
        return None                 # On renvoie None pour indiquer que le mot n'est pas valide


def double(lettre : str, points : dict, slider_metric :int) -> str :
    """
    double: Prend en entrée le mot que l'on cherche, le dictionnaire de point et la valeur de slider_metric, 
    elle renvoie ensuite le score du mot demandé multiplié par deux si le mot est valide.
    """
    verification =Score(lettre, points, slider_metric)  # On utilise la fonction Score pour vérifier si le mot est valide et obtenir son score
    mot = lettre.get()                                  # on récupère dans la variable mot le mot écrit dans le champ d'entrée lettre 
    tt.up()
    tt.setheading(0)
    tt.goto(-300,-200)                                  # Positionnement pour afficher le score doublé
    tt.down()
    if verification != None:                            # Si le mot est validé:
        res = verification*2                            # On double le score
        tt.write('Mais le mot %s compte double, il vaut donc %s pts.' % (mot, res), font =('Calibri', 20, 'italic'))  # On affiche le résultat
    else:                                               # Si le mot n'est pas validé:
        tt.write('Erreur', font =('Calibri', 16, 'italic')) # On affiche une erreur 


def quadruple(lettre : str, points : dict, slider_metric :int) -> str :
    """
    quadruple: Prend en entrée le mot que l'on cherche, le dictionnaire de point et la valeur de slider_metric, 
    elle renvoie ensuite le score du mot demandé multiplié par 4 si le mot est valide.
    """
    # même fonctionnement que double(lettre, points, sider_metric)
    verification =Score(lettre, points, slider_metric)  
    mot = lettre.get()
    tt.up()
    tt.setheading(0)
    tt.goto(-300,-200)                                  
    tt.down()
    if verification != None:                                
        res = verification*4                             
        tt.write('Mais le mot %s est multiplié par 4, il vaut donc %s pts.' % (mot, res), font =('Calibri', 20, 'italic'))          
    else:
        tt.write('Erreur', font =('Calibri', 16, 'italic')) 


def nonuple(lettre : str, points : dict, slider_metric :int) -> str :
    """
    pontuple: Prend en entrée le mot que l'on cherche, le dictionnaire de point et la valeur de slider_metric, 
    elle renvoie ensuite le score du mot demandé multiplié par deux si le mot est valide.
    """
    # même fonctionnement que double(lettre, points, sider_metric)
    verification =Score(lettre, points, slider_metric)                     
    mot = lettre.get()
    tt.up()
    tt.setheading(0)
    tt.goto(-300,-200)                                  
    tt.down()
    if verification != None:                                
        res = verification*9                            
        tt.write('Mais le mot %s est multiplié par 9, il vaut donc %s pts.' % (mot, res), font =('Calibri', 20, 'italic'))           
    else:
        tt.write('Erreur', font =('Calibri', 16, 'italic')) 


def gros_bonus(lettre : str, points : dict, slider_metric :int) -> str :
    """
    gros_bonus: Prend en entrée le mot que l'on cherche, le dictionnaire de point et la valeur de slider_metric, 
    elle renvoie ensuite le score du mot demandé multiplié par 27 si le mot est valide.
    """
    # même fonctionnement que double(lettre, points, sider_metric)
    verification =Score(lettre, points, slider_metric)  
    mot = lettre.get()
    tt.up()
    tt.setheading(0)
    tt.goto(-300,-200)                                  
    tt.down()
    if verification != None:                     
        res = verification*27                          
        tt.write('Mais le mot %s est multiplié par 27, il vaut donc %s pts.' % (mot, res), font =('Calibri', 20, 'italic'))           
    else:
        tt.write('Erreur', font =('Calibri', 16, 'italic')) 


def historique():
    """
    fonction historique qui affiche les 10 derniers mots
    elle ne prend rien en paramètre 
    """
    historique_list=[]                              # liste vide pour stocker les scores
    F = open('scores.txt','r', encoding='utf-8')    # ouverture du fichier en mode lecture
    historique_list = F.read().split('\n')          # lecture du fichier et séparation des lignes
    F.close()                                       # fermeture du fichier
    while len(historique_list) >10:                 # tant que la liste contient plus de 10 éléments on affiche les 10 derniers mots et scores
      historique_list.remove(historique_list[0])    # on supprimee mot le plus ancien (1er de la liste) quand un nouveau est ajouté
    tt.up()
    tt.goto(230,350)                                # positionnement pour afficher l'historique 
    # affichage de l'historique 
    tt.write('Historique des 10 derniers: \n',font=('Minecraft', 30, 'bold'))   
    tt.setheading(270)                              # orientation de la tortue vers le bas
    print(historique_list)                          # affichage dans la console pour vérification
    for elem in historique_list:                    
        if elem == '':                              # si elem est une chaine vide on passe au suivant 
            continue
        print(elem)
        score,mot = elem.split(';')                 # séparation de la chaine en 2 par ';'
        tt.setheading(270)
        tt.write(f'{mot}, {score}pts', font=('Minecraft', 20, 'italic'))  # affichage du score du mot
        tt.fd((30))                                   # espace entre deux mots