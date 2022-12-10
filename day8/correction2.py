from math import prod

grid = open('input.txt').read().splitlines()
trees = []
for y in range(1, len(grid)-1):
  for x in range(1, len(grid[y])-1):
    trees.append({
      'height': grid[y][x],
      'sides': [
        [grid[i][x] for i in range(y)][::-1], # up
        grid[y][:x][::-1], # left
        [grid[i][x] for i in range(y+1, len(grid))], # down
        grid[y][x+1:] # right
      ]
    })

side_visible = lambda tree, side: not any([other >= tree['height'] for other in side])
visible = lambda tree: any([side_visible(tree, side) for side in tree['sides']])
print('Part 1: ', sum(map(visible, trees)) + (len(grid)*4)-4)

side_score = lambda tree, side: next((i+1 for i, other in enumerate(side) if other >= tree['height']), len(side))
score = lambda tree: prod([side_score(tree, side) for side in tree['sides']])
print('Part 2: ', max(map(score, trees)))