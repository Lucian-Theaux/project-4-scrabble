import turtle as tt
from Lucian_Theaux.tuiles import tuile

def bareme_scrabble(metric):
    """
    Affiche toutes les tuiles du Scrabble classées par nombre de points
    """
    tt.speed(0)                                                     # Vitesse maximale pour l'affichage
    tt.up()                                                         # Lever le stylo pour ne pas dessiner en se déplaçant
    tt.goto(-600, 325)                                              # Position de départ pour l'affichage du barème                            
    tt.write("Barème des points :", font=('Arial', 16, 'bold'))      # Titre du barème
    tt.goto(-600, float(tt.pos()[1]) - float(6*metric))         # Descendre pour commencer à afficher les tuiles
    tt.setheading(0)                                             # Orientation vers la droite
    tt.down()
    groupes = [                                                     # Groupes de lettres par nombre de points
        (1,  ['A','E','I','L','N','O','R','S','T','U']),
        (2,  ['D','G','M']),
        (3,  ['B','C','P']),
        (4,  ['F','H','V']),
        (8,  ['J','Q']),
        (10, ['K','W','X','Y','Z'])]
    for score, lettres in groupes:                                      # Parcourt chaque groupe de lettres  
        for ltr in lettres:                                             # Parcourt chaque lettre dans le groupe
            tuile(ltr, metric)                                          # Affiche la tuile de la lettre
        tt.penup()                                                      # Lève le stylo pour le déplacement        
        tt.goto(-600, float(tt.pos()[1]) - 6*metric)                    # Descend pour la prochaine ligne de tuiles
        tt.pendown()                                                    # Abaisse le stylo pour dessiner    
    tt.hideturtle()                                                     # Cache la tortue après l'affichage du barème

