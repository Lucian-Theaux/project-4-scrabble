mot = input('Quel est le mot : ')
mot = mot.upper()
print(mot)
i = 1

with open('mots_autorises.txt', 'r', encoding='utf-8') as F:
    for ligne in F:
        if ligne[:-1] == mot:
            print(i)
            break

        i += 1