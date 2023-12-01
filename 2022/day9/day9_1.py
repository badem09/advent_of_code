f = open("input.txt")

visite_t = []
h = [0, 0] # ligne,colonne
t = [0, 0]
val_d = {"R": [1, 0], "L": [-1, 0], "U": [0 ,1], "D": [0 ,-1]}

for l in f:
    d = l.split(" ")[0]
    n = l.split(" ")[1][:-1]

    for _ in range(int(n)):
        old_h = h.copy() #position de la tête avant déplacement
        h[0] += val_d[d][0]
        h[1] += val_d[d][1]

        if abs(h[0] - t[0]) > 1 or abs(h[1] - t[1]) > 1:
            t = old_h

        if not (t in visite_t): # marche mais est limité si la queue revient à une position
            visite_t.append(t)  # qu'elle a déja visité

print(len(visite_t))