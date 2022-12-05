file_stack = open("stack.txt","r")
file_instructions = open("instruction.txt","r")

from collections import deque

stack = deque()

liste_stack = []
liste1 = [list(i) for i in list(file_stack)]

liste2 = [[] for i in range(len(liste1)-1)]
print(liste2)
print(liste1)
for i in range(len(liste1)-1):
    for j in range(len(liste1[i])-1):
        if liste1[i][j] != " " and liste1[i][j] != "[" and liste1[i][j] != "]":
            liste2[j].append(liste1[i][j])

print(liste2)