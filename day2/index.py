textInput = open("input.txt", "r")
dictScore = {
    "A" : {"X" : 3 , "Y" : 6, "Z" : 0} , #rock
    "B" : {"X" : 0 , "Y" : 3, "Z" :6} , #paper
    "C" : {"X" : 6 , "Y" : 0, "Z" : 3} #scissors 
}
dictValeurP1 = {"X" : 1 , "Y" : 2, "Z" : 3} #Valeur du choix
dictValeurP2 = {"X" : 0 , "Y" : 3, "Z" :6}  #Valeur du score Attendu
scoreP1 = scoreP2 = 0

for l in textInput:
    elf = l[0]
    meP1 = resAttendu = l[2]

    #Partie 1
    scoreP1 += dictScore[elf][meP1] + dictValeurP1[meP1]
    
    #Partie 2
    scoreAttendu = dictValeurP2[resAttendu]
    for choix in dictScore[elf]:
        if dictScore[elf][choix] == scoreAttendu:
            scoreP2 += dictValeurP1[choix] + scoreAttendu


print(scoreP1,scoreP2)

# Partie 1 : 2e elem = notre choix
# Partie 2 : 2e elem = resultat de la partie 