import math

f = open("input.txt")
liste = list(f)
x = 1
num_cylce = 0
liste_signal = []


ctr = []
for _ in range(6): #Obligé de faire des boucles sinon certaines listes pointent
    ligne_ctr = [] #vers le même endroit
    for _ in range(40):
        ligne_ctr.append(".")
    ctr.append(ligne_ctr.copy())

for i in range(len(liste)):
    j=1 #nb de cycles requis pour executer la commande
    n=0
    if "addx" in liste[i]:
        j = 2
        n = liste[i].split(' ')[1]
    for j in range(j):
        ctr_j = num_cylce % 40
        ctr_i = num_cylce // 40
        sprite = list(range(x-1,x+2))
        for k in sprite:
            if k == ctr_j:
                ctr[ctr_i][ctr_j] = "#"

        num_cylce += 1
        if num_cylce in [20, 60, 100, 140, 180, 220]:
            liste_signal.append([num_cylce, x])
    x+=int(n)

print(sum([math.prod(i) for i in liste_signal])) # Partie 1

for e in ctr : #Partie 2
    print(e)