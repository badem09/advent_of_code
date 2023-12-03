# https://adventofcode.com/2023/day/3
import itertools

list_input = [list(e.replace('\n', '')) for e in list(open('input.txt', 'r'))]
numbers = []
gears = []


def look_for_num(i, j):
    """
    Looks for a number from the position (i,j)
    """
    num = ''
    while j > 0 and list_input[i][j].isnumeric():  # get to the start of the num
        j -= 1
    if not list_input[i][j].isnumeric():  # if we're too far back
        j += 1
    while j < len(list_input[0]) and list_input[i][j].isnumeric():
        num += list_input[i][j]
        list_input[i][j] = '.'
        j += 1
    return num


## Part 1

for i in range(len(list_input)):
    for j in range(len(list_input[i])):
        char = list_input[i][j]
        if not char.isalnum() and char != '.':  # found a special char
            for di, dj in list(itertools.product([1, 0, -1], repeat=2)):  # to get all 9 neighbours
                # if still on the board
                if 0 <= i + di < len(list_input) and 0 <= j + dj < len(list_input[j]) \
                        and list_input[i + di][j + dj].isnumeric():
                    numbers.append(look_for_num(i + di, j + dj))

print("Part 1 :", sum(int(x) for x in numbers if x != ''))

## Part 2

list_input = [list(e.replace('\n', '')) for e in list(open('input.txt', 'r'))]
for i in range(len(list_input)):
    for j in range(len(list_input[i])):
        char = list_input[i][j]
        if char == "*":
            num_gear = []
            for di, dj in list(itertools.product([1, 0, -1], repeat=2)):
                if list_input[i + di][j + dj].isnumeric():
                    num = look_for_num(i + di, j + dj)
                    if num:
                        num_gear.append(num)
            if len(num_gear) == 2:
                gears.append(num_gear)

gears = [[int(x[0]) * int(x[1])] for x in gears]
print("Part 2 :", sum(x[0] for x in gears))
