from functools import reduce

input = open("input.txt", "r")
r, g, b, = 12, 13, 14
constraint = {'red' : 12, 'green' : 13, 'blue' : 14}
max_col = {'red' : 0, 'green' : 0, 'blue' : 0}
sum_part1 = 0
sum_part2 = 0

for l in input:
    l = l.replace('\n','')
    id = l.split(":")[0].split(' ')[1]
    games = [e.split(',') for e in l.split(':')[1].split(";")]
    valid_game = True
    for game in games:
        for cube in game:
            nb = int(cube.split(" ")[1])
            col = cube.split(" ")[2]
            valid_game = False if nb > constraint[col] else valid_game
            max_col[col] = nb if nb > max_col[col] else max_col[col]

    if valid_game:
        sum_part1 += int(id)

    min_nb = [e[1] for e in max_col.items()]
    sum_part2 += reduce(lambda x,y: x*y, min_nb) # π (prod)
    for col in max_col.keys():
        max_col[col] = 0

print(sum_part1, sum_part2)
