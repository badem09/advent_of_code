f = open("input.txt","r")
tree = list(f)
ROWS, COLS = len(tree), len(tree[0])
part1, part2 = 0, 0
for r in range(ROWS):
    for c in range(COLS):
        visible = False
        score = 1
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            r2, c2 = r + dr, c + dc
            while 0 <= r2 < ROWS and 0 <= c2 < COLS:
                if tree[r2][c2] >= tree[r][c]:
                    break
                r2, c2 = r2 + dr, c2 + dc
            else:
                visible = True
            score *= abs(r - r2) + abs(c - c2)
        if visible:
            part1 += 1
        part2 = max(part2, score)
print(part1, part2)