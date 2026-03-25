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
    if direction == ... :#horizontal
        if plateau[y][x-1] !="":
                nouv_motA=[plateau[y][x-1] + [mot]]
                verif=False
                n=1
                while verif == False:
                    n=n+1
                    if plateau[y][x-n] !="":
                        nouv_motA = [plateau[y][x-n]] + nouv_motA
                    else:
                        verif = True
                nouv_motA="".join(nouv_motA)
                #puis regarder s'il est dans le dico, s'il est alors c'est bon , 
                #sinon return message d'erreur comme quoi le mot convient pas
        if plateau[y][x + len[mot]] !="":
                nouv_motB=[mot + plateau[y][x + len[mot]]]
                verif=False
                n=1
                while verif == False:
                    n=n+1
                    if plateau[y][x+n] !="":
                        nouv_motB = nouv_motB + [plateau[y][+-n]]
                    else:
                        verif = True
                nouv_motB="".join(nouv_motB)
                #regarder s'il est dans le dico, s'il est alors c'est bon , 
                #sinon return message d'erreur comme quoi le mot convient pas
        
        for i in range(len(mot)):
            if plateau[y-1][x+i] != "":
                nouv_mot1=[plateau[y-1][x+i],plateau[y][x+i]]
                verif=False
                n=1
                while verif == False:
                    n=n+1
                    if plateau[y-n][x+i] !="":
                        nouv_mot1 =[plateau[y-n][x+i]] + nouv_mot1 
                    else:
                        verif = True
                nouv_mot1="".join(nouv_mot1)
                #reformer le nouveau mot et regarder s'il est dans le dico, s'il est alors c'estc bon , 
                #sinon return message d'erreur comme quoi le mot convient pas
            elif plateau[y+1][x+i] != "":
                nouv_mot2=[plateau[y][x+i],plateau[y+1][x+i]]
                verif=False
                n=1
                while verif == False:
                    n=n+1
                    if plateau[y+n][x+i] !="":
                        nouv_mot2 =  nouv_mot2 +[plateau[y+n][x+i]] 
                    else:
                        verif = True
                nouv_mot2="".join(nouv_mot2)
                #reformer le nouveau mot et regarder s'il est dans le dico, s'il est alors c'estc bon , 
                #sinon return message d'erreur comme quoi le mot convient pas
                

    if direction == ... : #vertical
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
                #puis regarder s'il est dans le dico, s'il est alors c'est bon , 
                #sinon return message d'erreur comme quoi le mot convient pas

        elif plateau[y + len[mot]][x] !="":
                nouv_motD=[mot + plateau[y + len[mot]][x]]
                verif=False
                n=1
                while verif == False:
                    n=n+1
                    if plateau[y+n][x] !="":
                        nouv_motD =  + nouv_motD + [plateau[y+n][x]]
                    else:
                        verif = True
                nouv_motD="".join(nouv_motD)
                #regarder s'il est dans le dico, s'il est alors c'est bon , 
                #sinon return message d'erreur comme quoi le mot convient pas
        
        for i in range(len(mot)):
            if plateau[y+i][x-1] != "":
                nouv_mot3=[plateau[y+i][x-1],plateau[y+i][x]]
                verif=False
                n=1
                while verif == False:
                    n=n+1
                    if plateau[y+i][x-n] !="":
                        nouv_mot3 = [plateau[y+i][x-n]] + nouv_mot3 
                    else:
                        verif = True
                nouv_mot3= "".join(nouv_mot3)
                #reformer le nouveau mot et regarder s'il est dans le dico, s'il est alors c'estc bon , 
                #sinon return message d'erreur comme quoi le mot convient pas


            elif plateau[y+i][x+1] != "":
                nouv_mot4=[plateau[y+i][x],plateau[y+i][x+1]]
                verif=False
                n=1
                while verif == False:
                    n=n+1
                    if plateau[y+i][x+n] !="":
                        nouv_mot4 = nouv_mot4 + [plateau[y+i][x+n]]
                    else:
                        verif = True
                nouv_mot4="".join(nouv_mot4)
                #reformer le nouveau mot et regarder s'il est dans le dico, s'il est alors c'estc bon , 
                #sinon return message d'erreur comme quoi le mot convient pas