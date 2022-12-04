import math
f = open("input.txt","r")
s1 = s2 = k = 0

for li in f:
    liste = [i.split("-") for i in li.split(",")]
    liste = [[int(i[0]),int(i[1])] for i in liste]

    #Partie 1:
    if (liste[0][0] <= liste[1][0] and liste[0][1] >= liste[1][1]) or (liste[1][0] <= liste[0][0] and liste[1][1] >= liste[0][1]):
        s1+=1

    #Partie 2 :
    if liste[0][1] >= liste[1][0] and liste[0][0] <= liste[1][1]:
        s2+=1

print(s1,s2)