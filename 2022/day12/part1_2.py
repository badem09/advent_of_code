f = open("input.txt","r")

liste = list(f)
liste = [list(i[:-1]) for i in liste]
alpha = 'SabcdefghijklmnopqrstuvwxyzE'

for i in range(len(liste)):
    for j in range(len(liste[i])):
        if liste[i][j] == 'S':
            start = (i,j)
        if liste[i][j] == 'E':
            end = (i,j)

