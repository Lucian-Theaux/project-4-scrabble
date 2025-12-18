francais = open('francais.txt', 'r', encoding='utf-8')
content = str(francais.read()).split('\n')
francais.close()

with open('mots_autorises.txt', 'a', encoding='utf-8') as F:

    for line in content:
        print(line)
        F.write(f'{str(line.capitalize)}\n')

