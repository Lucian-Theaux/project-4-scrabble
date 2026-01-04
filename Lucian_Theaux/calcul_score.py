import turtle as tt

def ajout_score(score:int,mot:str):
    """
    ajout_score: Écrit dans le fichier scores.txt le score donné en entrée
    - score: Prend en entrée un integer
    """
    with open('scores.txt', 'a', encoding='utf-8') as F:
        F.write(f'{score};{mot}\n')

def scoreboard(length:int):
    """
    scoreboard: Récupère tous les scores du fichier texte scores.txt pour créer un scoreboard length score du meilleur au plus petit
    - length: Prend en entrée un integer
    """
    scoreboard_dict = {}
    with open('scores.txt', 'r', encoding='utf-8') as F:
        scoreboard_list = F.read().split('\n')
    print(scoreboard_list)
    for elem in scoreboard_list:
        if elem == '':
            continue
        value,key = elem.split(';')
        scoreboard_dict[key] = int(value)
    scoreboard_dict = dict(sorted(scoreboard_dict.items(), key= lambda item: item[1]))
    print(scoreboard_dict)
    tt.fillcolor('white')
    tt.penup()
    tt.goto(300, -300)
    tt.begin_fill()
    tt.fd(100)
    tt.rt(90)
    tt.fd(50)
    tt.rt(90)
    tt.fd(100)
    tt.rt(90)
    tt.fd(50)
    tt.end_fill()
    tt.rt(90)
    tt.fd(95)
    tt.rt(90)
    tt.write('CLASSEMENT', font=('Minecraft',30, 'bold'))
    tt.fd(30)
    i = 0
    for i in range(1,length+1):
        key = list(scoreboard_dict)[-i]
        value = list(scoreboard_dict.values())[-i]
        if i == 1:
            tt.color("#D1A90F")
            tt.write(f'{value} ☞ {key}', font=('Minecraft',20, 'italic'))
            tt.color('black')
            tt.fd(20)
        else:
            tt.write(f'{value} ☞ {key}', font=('Minecraft',20, 'italic'))
            tt.fd(20)
        i+= 1
        