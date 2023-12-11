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
index_to_expand = []
k = 0
for i in range(len(grid)):
    if grid[i].count('.') == len(grid[i]):
        expanded.insert(k,grid[i])
        k+=1
    k+=1

transposee_e = list(map(list, zip(*copy.deepcopy(expanded))))
res = copy.deepcopy(transposee_e)

k=0
for i in range(len(transposee_e)):
    if transposee_e[i].count('.') == len(transposee_e[i]):
        res.insert(k,transposee_e[i])
        k += 1
    k += 1

print_grid(res)
