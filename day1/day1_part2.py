#Partie 2

textInput = open("day1_input.txt", "r")
numeric = "1234567890"
somme = 0
liste_trois_max = [0,0,0]

for lign in textInput:
    if lign[0] not in numeric: #si la ligne est un espace 
        if somme > min(liste_trois_max):
            liste_trois_max[0] = somme # le minimum est remplacé
            liste_trois_max.sort()
        somme = 0 # on arrête de comter la somme
        continue
    somme += int(lign) 

print(sum(liste_trois_max))
