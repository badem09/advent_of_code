# n  * n-1 pairs
import copy
from itertools import combinations

pairs = list(combinations(list(range(9)), 2))
input_list = [list(e.replace('\n', '')) for e in open('input.txt').readlines()]
grid = copy.deepcopy(input_list)

def print_grid(g):
    print()
    for l in g:
        print(l)


transposee = list(map(list, zip(*copy.deepcopy(grid))))
print_grid(grid)
print()
expanded = copy.deepcopy(grid)
for i in range(len(grid)):
    if grid[i].count('.') == len(grid[i])-1:
        expanded.insert(i,grid[i])

transposee_e = list(map(list, zip(*copy.deepcopy(expanded))))

for i in range(len(transposee_e)):
    if grid[i].count('.') == len(grid[i])-1:
        transposee_e.insert(i,grid[i])

print_grid(transposee_e)
