f = open("input.txt")


body = [[0,0] for i in range(10)]
val_d = {"R" : [1,0], "L" : [-1,0], "U" : [0,1], "D" : [0,-1]}
visite_t = set()

for l in f:
    d = l.split(" ")[0]
    n = l.split(" ")[1][:-1]

    for _ in range(int(n)):
        for i in range(len(body)):
            if i == 0: # si tête de corde
                h = body[i]
                old_h = h.copy()
                body[i][0] += val_d[d][0]
                body[i][1] += val_d[d][1]

            else:
                # si l'élément i (courant) et l'élément i - 1 (précédant) ne sont plus alignés verticalement, horizontalement
                # ou en diagonale: l'élement i doit se déplacer en diagonale.
                if abs(body[i-1][1] - body[i][1]) > 1 or abs(body[i-1][0] - body[i][0]) > 1  :
                    if body[i][0] < body[i-1][0]:
                        body[i][0] +=1
                    if body[i][0] > body[i-1][0]:
                        body[i][0] -=1
                    if body[i][1] < body[i-1][1]:
                        body[i][1] +=1
                    if body[i][1] > body[i-1][1]:
                        body[i][1] -=1

                #sinon, prend l'ancienne place de l'élement précedant (i-1)
                elif abs(body[i-1][0] - body[i][0]) > 1 or  abs(body[i-1][1] - body[i][1]) >1:
                    body[i],old_h = old_h,body[i]

            if i == len(body) - 1 :
                visite_t.add(tuple(body[i]))

print(len(visite_t))
