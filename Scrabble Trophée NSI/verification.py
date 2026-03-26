#cette page contient toutes les vérifications: 
# #vérification que deux mots ne se chevauchent pas,
# #vérification que deux mots côte à côte forment un mot existant
import os 

def verification_place(plateau,y,x, direction,mot):
    if direction == "horizontal" : #horizontal
        for i in range(len(mot)):
            if plateau[y][x+i] != "" and plateau[y][x+i]!= mot[i] :
                return f"changez vos coordonnées, la case {y} {x+i} est déjà prise"
    elif direction == "vertical" : #vertical
        for i in range(len(mot)):
            if plateau[y+i][x] != "" and plateau[y+i][x] != mot[i]:
                return f"changez vos coordonnées, la case {y+i} {x} est déjà prise "
    return True


def verification_mot(plateau,y,x, direction,mot):
    dossier = os.path.dirname(__file__)         # Récupération du dossier courant
    chemin_fichier = os.path.join(dossier, "mots_autorises.txt")  # Construction du chemin complet vers le fichier
    with open(chemin_fichier,'r', encoding= 'utf-8') as fichier:
        if direction == "horizontal":#horizontal
            if plateau[y][x-1] !="":
                    nouv_motA=[plateau[y][x-1] + mot]
                    verif=False
                    n=1
                    while verif == False:
                        n=n+1
                        if plateau[y][x-n] !="":
                            nouv_motA = [plateau[y][x-n]] + nouv_motA
                        else:
                            verif = True
                    nouv_motA="".join(nouv_motA)
                    for ligne in fichier:                         # Parcours de chaque ligne du fichier
                        if ligne[:-1] == nouv_motA:               # Comparaison du mot (enlevant le caractère de nouvelle ligne)
                            return True               # Si le mot est trouvé, renvoyer True et l'index
                        n += 1
                    return False
            if plateau[y][x + len(mot)] !="":
                    nouv_motB=[mot + plateau[y][x + len(mot)]]
                    verif=False
                    n=1
                    while verif == False:
                        n=n+1
                        if plateau[y][x+n] !="":
                            nouv_motB = nouv_motB + [plateau[y][+-n]]
                        else:
                            verif = True
                    nouv_motB="".join(nouv_motB)
                    for ligne in fichier:                         # Parcours de chaque ligne du fichier
                        if ligne[:-1] == nouv_motB:               # Comparaison du mot (enlevant le caractère de nouvelle ligne)
                            return True               # Si le mot est trouvé, renvoyer True et l'index
                        n += 1
                    return False

            for i in range(len(mot)):
                if plateau[y-1][x+i] != "":
                    nouv_mot1=[plateau[y-1][x+i],mot[i]]
                    print(nouv_mot1)
                    verif=False
                    n=1
                    while verif == False:
                        n=n+1
                        if plateau[y-n][x+i] !="":
                            nouv_mot1 =[plateau[y-n][x+i]] + nouv_mot1 
                        else:
                            verif = True
                    nouv_mot1="".join(nouv_mot1)
                    for ligne in fichier:                         # Parcours de chaque ligne du fichier
                        if ligne[:-1] == nouv_mot1:               # Comparaison du mot (enlevant le caractère de nouvelle ligne)
                            return True               # Si le mot est trouvé, renvoyer True et l'index
                        n += 1
                    return False
                    
                elif plateau[y+1][x+i] != "":
                    nouv_mot2=[mot[i],plateau[y+1][x+i]]
                    verif=False
                    n=1
                    while verif == False:
                        n=n+1
                        if plateau[y+n][x+i] !="":
                            nouv_mot2 =  nouv_mot2 +[plateau[y+n][x+i]] 
                        else:
                            verif = True
                    nouv_mot2="".join(nouv_mot2)
                    for ligne in fichier:                         # Parcours de chaque ligne du fichier
                        if ligne[:-1] == nouv_mot2:               # Comparaison du mot (enlevant le caractère de nouvelle ligne)
                            return True               # Si le mot est trouvé, renvoyer True et l'index
                        n += 1
                    return False
        elif direction == "vertical" : #vertical
            if plateau[y-1][x] !="":
                    nouv_motC= [plateau[y-1][x], mot]
                    verif=False
                    n=1
                    while verif == False:
                        n=n+1
                        if plateau[y-n][x] !="":
                            nouv_motC = [plateau[y-n][x]] + nouv_motC 
                        else:
                            verif = True
                    nouv_motC="".join(nouv_motC)
                    for ligne in fichier:                         # Parcours de chaque ligne du fichier
                        if ligne[:-1] == nouv_motC:               # Comparaison du mot (enlevant le caractère de nouvelle ligne)
                            return True               # Si le mot est trouvé, renvoyer True et l'index
                        n += 1
                    return False

            elif plateau[y + len(mot)][x] !="":
                    nouv_motD=[mot + plateau[y + len(mot)][x]]
                    verif=False
                    n=1
                    while verif == False:
                        n=n+1
                        if plateau[y+n][x] !="":
                            nouv_motD =  + nouv_motD + [plateau[y+n][x]]
                        else:
                            verif = True
                    nouv_motD="".join(nouv_motD)
                    for ligne in fichier:                         # Parcours de chaque ligne du fichier
                        if ligne[:-1] == nouv_motD:               # Comparaison du mot (enlevant le caractère de nouvelle ligne)
                            return True               # Si le mot est trouvé, renvoyer True et l'index
                        n += 1
                    return False

            for i in range(len(mot)):
                if plateau[y+i][x-1] != "":
                    nouv_mot3=[plateau[y+i][x-1],mot[i]]
                    verif=False
                    n=1
                    while verif == False:
                        n=n+1
                        if plateau[y+i][x-n] !="":
                            nouv_mot3 = [plateau[y+i][x-n]] + nouv_mot3 
                        else:
                            verif = True
                    nouv_mot3= "".join(nouv_mot3)
                    for ligne in fichier:                         # Parcours de chaque ligne du fichier
                        if ligne[:-1] == nouv_mot3:               # Comparaison du mot (enlevant le caractère de nouvelle ligne)
                            return True               # Si le mot est trouvé, renvoyer True et l'index
                        n += 1
                    return False


                elif plateau[y+i][x+1] != "":
                    nouv_mot4=[mot[i],plateau[y+i][x+1]]
                    verif=False
                    n=1
                    while verif == False:
                        n=n+1
                        if plateau[y+i][x+n] !="":
                            nouv_mot4 = nouv_mot4 + [plateau[y+i][x+n]]
                        else:
                            verif = True
                    nouv_mot4="".join(nouv_mot4)
                    for ligne in fichier:                         # Parcours de chaque ligne du fichier
                        if ligne[:-1] == nouv_mot4:               # Comparaison du mot (enlevant le caractère de nouvelle ligne)
                            return True               # Si le mot est trouvé, renvoyer True et l'index
                        n += 1
                    return False