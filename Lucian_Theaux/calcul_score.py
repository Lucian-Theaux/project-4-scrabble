def ajout_score(score):
    with open('scores.txt', 'a', encoding='utf-8') as F:
        F.write(f'{score}\n')

def scoreboard(length):
    with open('scores.txt', 'r', encoding='utf-8') as F:
        scoreboard_list = F.read()
        print(scoreboard)
    scoreboard_list = scoreboard_list.sort()
    if scoreboard_list <= length:
        return scoreboard_list
    else:
        return scoreboard_list[:4]

print(scoreboard(5))