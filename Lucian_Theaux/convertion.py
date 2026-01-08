francais = open('francais.txt', 'r', encoding='utf-8')                      # Ouvrir le fichier en mode lecture
content = str(francais.read()).split('\n')                                  # Lire le contenu du fichier et le diviser en lignes
francais.close()                                                            # Fermer le fichier après la lecture    
print(content)                                                              # Afficher le contenu lu pour vérification 
with open('mots_autorises.txt', 'w', encoding='utf-8') as F:                    # Ouvrir le fichier en mode écriture

    for line in content:                                                    # Parcourir chaque ligne du contenu
        texte = line                                                        # Extraire le mot de la ligne  
        F.write(f'{str(texte.upper())}\n')                                  # Écrire le mot en majuscules dans le nouveau fichier
