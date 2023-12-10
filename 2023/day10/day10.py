import itertools
import sys

sys.setrecursionlimit(50000)
import copy

input_list = [e.replace('\n', '') for e in open('input.txt').readlines()]
p = [None for _ in range(len(input_list))]
positions = [p.copy() for _ in range(len(input_list[0]))]
pipes = {'F': ['s', 'e'], 'J': ['n', 'w'], '-': ['e', 'w'], '|': ['n', 's'], '7': ["s", 'w'], 'L': ['n', 'e']}
# pipes_val = {'F' : ['s','e'], 'dy':['n','w'], '-':['e','w'], '|':['n','s'], '7' : ["s",'w'], 'L': ['n','e']}
grid = [list(e) for e in input_list.copy()]
furthest_points = []


def find_start():
    for dx, l in enumerate(grid):
        if 'S' in l:
            return dx, l.index('S')


start = find_start()
liste_grid = []


def find_possible_pipes(start_pos, grid, k):
    possible = []
    for dx, dy in [(-1, 0), [0, 1], (1, 0), (0, -1)]:
        if 0 <= start_pos[0] + dx < len(grid) and 0 <= start_pos[1] + dy < len(grid[1]):
            elem = grid[start_pos[0] + dx][start_pos[1] + dy]
            np = (start_pos[0] + dx, start_pos[1] + dy) # new position

            if elem in pipes:
                if dy == -1 and dx == 0:  # from west
                    if 'e' in pipes[elem]:
                        possible.append((elem, np))
                if dy == 1 and dx == 0:  # from east
                    if 'w' in pipes[elem]:
                        possible.append((elem, np))
                if dy == 0 and dx == -1:  # from south
                    if 's' in pipes[elem]:
                        possible.append((elem, np))
                if dy == 0 and dx == 1:  # enter from north
                    if 'n' in pipes[elem]:
                        possible.append((elem, np))

            if elem == 0 and k > 3:
                liste_grid.append(copy.deepcopy(grid))

    for p, np in possible:
        prev_elem = grid[np[0]][np[1]]
        grid[np[0]][np[1]] = k
        grid = find_possible_pipes((np[0], np[1]), grid, k + 1)
        grid[np[0]][np[1]] = prev_elem

    return grid


def print_grid(g):
    print()
    for l in g:
        print(l)


grid[start[0]][start[1]] = 0
grid = find_possible_pipes(start, grid, k=1)
max_grid = sorted(liste_grid, key=lambda x: sum(e for row in x for e in row if isinstance(e, int)))[-1]
print("star 1 :", max([e for r in max_grid for e in r if isinstance(e, int)]) // 2 + 1)


def fill_from_outside(start, grid):
    """
    Replaces all the tiles outside of the loops by a special char using the exterior flooding approach
    """
    for dx, dy in [(-1, 0), [0, 1], (1, 0), (0, -1)]:
        nx = start[0] + dx
        ny = start[1] + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if not isinstance(grid[nx][ny], int) and grid[nx][ny] != '@':
                grid[nx][ny] = '@'
                fill_from_outside((nx, ny), grid)
    return grid


for i in range(len(max_grid)):
    for j in range(len(max_grid[i])):
        if (i == 0 or j == 0) or (i == len(max_grid) - 1 or j == len(max_grid[i]) - 1):
            max_grid = fill_from_outside((i, j), max_grid)
        elif isinstance(max_grid[i][j], str): # to replaces all the tiles inside the loop but not part of the loop by '.'
            max_grid[i][j] = "."

# replaces the tiles number by their value (J,L,S or |)
for i in range(len(max_grid)):
    for j in range(len(max_grid[i])):
        if isinstance(max_grid[i][j], int):
            max_grid[i][j] = grid[i][j]
grid[start[0]][start[1]] = 'S'

# count the no of J,L,S,|, if this no is pair, we are outside the loop
for i in range(len(max_grid)):
    for j in range(len(max_grid)):
        if max_grid[i][j] == '.' and len([x for x in max_grid[i][:j] if x in list('JLS|')]) % 2 == 0:
            max_grid[i][j] = "@"

print('star 2 : ', len(([x for row in max_grid for x in row if isinstance(x, str) and x == "."])))
