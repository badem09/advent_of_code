f = open("input.txt")

file = [list(i[:-1]) if i[-1] == '\n' else list(i) for i in f]
liste = [[] for i in range(len(file))]
foret = [liste.copy() for i in range(len(file))]
#foret : True ou False selon si l'arbre à i,j est visible ou pas

for di,dj in [(1,0),(-1,0),[0,1],(0,-1)]:
    for i in range(len(file)):
        for j in range(len(file[i])):
            if not foret[i][j]: #Si pas visible
                visible = True
                ni,nj = i+di, j+dj
                #tant que pas sorti de la forêt et prochain visible
                while len(file) > ni >= 0 and len(file) > nj >= 0 and visible:
                    visible = file[i][j] > file[ni][nj]
                    ni += di
                    nj += dj
                else:# soit arbre plus visble, soit dépassé le bors
                    if visible:
                        foret[i][j] = visible


print("Le nombre d'arbres visible est" ,sum([i.count(True) for i in foret]))



