def verification_place(matrice,y,x, direction,mot):
    if direction == ... : #horizontal
        for i in range(len(mot)):
            if matrice[y][x+i] != "" and matrice[y][x+i]!= mot[i] :
                return f"changez vos coordonnées, la case {y} {x+i} est déjà prise"
    elif direction == ... : #vertical
        for i in range(len(mot)):
            if matrice[y+i][x] != "" and matrice[y+i][x] != mot[i]:
                return f"changez vos coordonnées, la case {y+i} {x} est déjà prise "
    return True


def verification_mot(matrice,y,x, direction,mot):
    if direction == ... :#horizontal
        if matrice[y][x-1] !="":
                nouv_motA=[matrice[y][x-1] + [mot]]
                verif=False
                n=1
                while verif == False:
                    n=n+1
                    if matrice[y][x-n] !="":
                        nouv_motA = [matrice[y][x-n]] + nouv_motA
                    else:
                        verif = True
                nouv_motA="".join(nouv_motA)
                #puis regarder s'il est dans le dico, s'il est alors c'est bon , 
                #sinon return message d'erreur comme quoi le mot convient pas
        if matrice[y][x + len[mot]] !="":
                nouv_motB=[mot + matrice[y][x + len[mot]]]
                verif=False
                n=1
                while verif == False:
                    n=n+1
                    if matrice[y][x+n] !="":
                        nouv_motB = nouv_motB + [matrice[y][+-n]]
                    else:
                        verif = True
                nouv_motB="".join(nouv_motB)
                #regarder s'il est dans le dico, s'il est alors c'est bon , 
                #sinon return message d'erreur comme quoi le mot convient pas
        
        for i in range(len(mot)):
            if matrice[y-1][x+i] != "":
                nouv_mot1=[matrice[y-1][x+i],matrice[y][x+i]]
                verif=False
                n=1
                while verif == False:
                    n=n+1
                    if matrice[y-n][x+i] !="":
                        nouv_mot1 =[matrice[y-n][x+i]] + nouv_mot1 
                    else:
                        verif = True
                nouv_mot1="".join(nouv_mot1)
                #reformer le nouveau mot et regarder s'il est dans le dico, s'il est alors c'estc bon , 
                #sinon return message d'erreur comme quoi le mot convient pas
            elif matrice[y+1][x+i] != "":
                nouv_mot2=[matrice[y][x+i],matrice[y+1][x+i]]
                verif=False
                n=1
                while verif == False:
                    n=n+1
                    if matrice[y+n][x+i] !="":
                        nouv_mot2 =  nouv_mot2 +[matrice[y+n][x+i]] 
                    else:
                        verif = True
                nouv_mot2="".join(nouv_mot2)
                #reformer le nouveau mot et regarder s'il est dans le dico, s'il est alors c'estc bon , 
                #sinon return message d'erreur comme quoi le mot convient pas
                

    if direction == ... : #vertical
        if matrice[y-1][x] !="":
                nouv_motC= [matrice[y-1][x], mot]
                verif=False
                n=1
                while verif == False:
                    n=n+1
                    if matrice[y-n][x] !="":
                        nouv_motC = [matrice[y-n][x]] + nouv_motC 
                    else:
                        verif = True
                nouv_motC="".join(nouv_motC)
                #puis regarder s'il est dans le dico, s'il est alors c'est bon , 
                #sinon return message d'erreur comme quoi le mot convient pas

        elif matrice[y + len[mot]][x] !="":
                nouv_motD=[mot + matrice[y + len[mot]][x]]
                verif=False
                n=1
                while verif == False:
                    n=n+1
                    if matrice[y+n][x] !="":
                        nouv_motD =  + nouv_motD + [matrice[y+n][x]]
                    else:
                        verif = True
                nouv_motD="".join(nouv_motD)
                #regarder s'il est dans le dico, s'il est alors c'est bon , 
                #sinon return message d'erreur comme quoi le mot convient pas
        
        for i in range(len(mot)):
            if matrice[y+i][x-1] != "":
                nouv_mot3=[matrice[y+i][x-1],matrice[y+i][x]]
                verif=False
                n=1
                while verif == False:
                    n=n+1
                    if matrice[y+i][x-n] !="":
                        nouv_mot3 = [matrice[y+i][x-n]] + nouv_mot3 
                    else:
                        verif = True
                nouv_mot3= "".join(nouv_mot3)
                #reformer le nouveau mot et regarder s'il est dans le dico, s'il est alors c'estc bon , 
                #sinon return message d'erreur comme quoi le mot convient pas


            elif matrice[y+i][x+1] != "":
                nouv_mot4=[matrice[y+i][x],matrice[y+i][x+1]]
                verif=False
                n=1
                while verif == False:
                    n=n+1
                    if matrice[y+i][x+n] !="":
                        nouv_mot4 = nouv_mot4 + [matrice[y+i][x+n]]
                    else:
                        verif = True
                nouv_mot4="".join(nouv_mot4)
                #reformer le nouveau mot et regarder s'il est dans le dico, s'il est alors c'estc bon , 
                #sinon return message d'erreur comme quoi le mot convient pas