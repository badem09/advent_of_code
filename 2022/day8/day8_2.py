f = open("input.txt")
file = [list(i[:-1]) if i[-1] == '\n' else list(i) for i in f]

non_visible = False
max = 0

for i in range(len(file)):
    for j in range(len(file[i])):
        prod = 1
        for di, dj in [(1, 0), (-1, 0), [0, 1], (0, -1)]:
            ni, nj = i + di, j + dj
            n = 0 # nb d'arbre pouvant être vu.

            #tant que pas sorti de la forêt et prochaine visible
            while len(file) > ni >= 0 and len(file) > nj >= 0 and not non_visible:
                non_visible = file[ni][nj] >= file[i][j] #concerne le prochain arbre
                ni += di
                nj += dj
                n +=1

            prod*=n
            if prod > max:
                max = prod
            non_visible = False

print(max)