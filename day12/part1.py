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


l_trajet = []
def explore(l,debut,visited):
    for x,y in ((1,0),(0,-1),(-1,0),(0,1)):
        x+=debut[0]
        y+=debut[1]

        if len(liste[0]) > y > -1 and len(liste) > x > -1:
            ia,ib = alpha.index(liste[x][y]) ,alpha.index(liste[debut[0]][debut[1]])
            a,b = liste[x][y] , liste[debut[0]][debut[1]]

            if alpha.index(liste[x][y]) - alpha.index(liste[debut[0]][debut[1]]) in (0,1) and (x,y) not in visited:
                l+=1
                if liste[x][y] == "E":
                    l_trajet.append(l)
                    #print(l)
                else:
                    visited.append((x,y))
                    #print(l,(x,y),liste[x][y])
                    explore(l,(x,y),visited)
                    l-=1
                    visited.remove((x,y))

print(start)
print(end)
explore(0,start,[])
print(l_trajet)
print(min(l_trajet))