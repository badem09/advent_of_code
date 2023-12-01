file_stack = open("stack.txt", "r")
file_instructions = open("instruction.txt", "r")
from collections import deque

liste1 = [i for i in list(file_stack)]
liste2 = [[] for i in range(len(liste1))]

for i in range(len(liste1) - 1, -1, -1):
    for j in range(len(liste1[i]) - 1, -1, -1):
        if liste1[i][j].isalpha():
            liste2[(j + 1) // 4].append(liste1[i][j])

liste_stack = [deque(i) for i in liste2 if len(i)>0]

for l in file_instructions:
    cut = l.split(" ")
    nb_to_move  = int(cut [1])
    col_from = int(cut [3]) - 1
    col_to = int(cut[5][0]) -1

    for _ in range(nb_to_move):
        x = liste_stack[col_from].pop()
        liste_stack[col_to].append(x)

r = ""
for e in liste_stack:
    r += e[-1]
print(r)





