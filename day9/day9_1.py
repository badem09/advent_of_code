f = open("input.txt")

ligne = [None]*6
grille = [[None,None,None,None,None,None],
          [None,None,None,None,None,None],
          [None,None,None,None,None,None],
          [None,None,None,None,None,None],
          [None,None,None,None,None,None]]

ncol = len(grille)
nli = len(grille[0])


h = [0,0]
t = [0,0] #x,y
visited = [t]
val_d = {"R" : [1,0], "L" : [-1,0], "U" : [0,1], "D" : [0,-1]}

for l in f:
    d = l.split(" ")[0]
    n = l.split(" ")[1][:-1]
    print(d,n,h,t)
    print("")
    for _ in range(int(n)):

        #h = [sum(pos) if 5>sum(pos)>=0 else 0 if sum(pos)<0 else 4  for pos in zip(h,val_d[d])]

        if 6 > h[0] + val_d[d][0] >= 0:
            h[0] += val_d[d][0]
        if 5 > h[1] + val_d[d][1] >= 0:
            h[1] += val_d[d][1]

        if abs(h[0] - t[0]) > 1 or  abs(h[1] - t[1]) >1:
            t = [eh - epos for eh,epos in zip(h,val_d[d])]
        print(h,t)
        grille [t[0]][t[1]] = "#"

print(grille)

print(len([i for ligne in grille for i in ligne if i == "#"]))