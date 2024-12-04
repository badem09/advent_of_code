from itertools import product

lines = [e.replace('\n', '') for e in open("input.txt").readlines()]
word_ex = 'XMAS'

def search_xmas1(lines, word, xmas_count=0):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == word_ex[0]:
                for dx, dy in list(product([0,1,-1], [0,1,-1])):
                    if not dx == dy == 0:
                        for k in range(4): # take 4 next letters
                            ni = i+k*dy
                            ny = j+k*dx
                            if ni < 0 or ny < 0 or ny >= len(lines[0]) or ni >= len(lines): # if out
                                break
                            word += lines[ni][ny]
                        xmas_count += 1 if word == word_ex else 0
                        word = ""
    return xmas_count

print(search_xmas1(lines, word=""))


def serach_xmas2(lines, word, mas_count=0):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] =="A":
                if i-1 < 0 or i+1 >= len(lines) or j-1 < 0 or j+1 >= len(lines[0]):
                    continue
                s1 = lines[i-1][j-1] + "A" + lines[i+1][j+1]
                s2 = lines[i+1][j-1] + "A" + lines[i-1][j+1]
                if s1 in ["MAS", "SAM"] and s2 in ["MAS", "SAM"]:
                    mas_count+=1
    return mas_count

print(serach_xmas2(lines, word=""))