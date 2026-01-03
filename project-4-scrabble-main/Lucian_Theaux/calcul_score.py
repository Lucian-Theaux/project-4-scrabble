def ajout_score(score:int):
    """
    ajout_score: Écrit dans le fichier scores.txt le score donné en entrée
    - score: Prend en entrée un integer
    """
    with open('scores.txt', 'a', encoding='utf-8') as F:
        F.write(f'{score}\n')

def scoreboard(length:int) -> list:
    """
    scoreboard: Récupère tous les scores du fichier texte scores.txt pour créer un scoreboard length score du meilleur au plus petit
    - length: Prend en entrée un integer
    """
    with open('Lucian_Theaux/scores.txt', 'r', encoding='utf-8') as F:
        scoreboard_list = F.read().split('\n')
    scoreboard_list = [int(elem) for elem in scoreboard_list]
    scoreboard_list = sorted(scoreboard_list)
    if len(scoreboard_list) <= length:
        return scoreboard_list
    else:
        return scoreboard_list[:length]
