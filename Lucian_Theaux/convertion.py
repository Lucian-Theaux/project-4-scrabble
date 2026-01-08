francais = open('francais.txt', 'r', encoding='utf-8')
content = str(francais.read()).split('\n')
francais.close()
print(content)
with open('mots_autorises.txt', 'w', encoding='utf-8') as F:

    for line in content:
        texte = line
        F.write(f'{str(texte.upper())}\n')

