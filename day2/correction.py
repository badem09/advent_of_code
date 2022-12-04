parties = [s.split() for s in open("input.txt").readlines()]


win = { 'A' : {'X' : 0 , 'Y' :  1,  'Z' : -1},
        'B' : {'X' : -1 , 'Y' :  0,   'Z' : 1},
        'C' : {'X' : 1, 'Y' :  -1,   'Z' : 0}}
score_win = {0:3,1:6,-1:0} 
score_choix = {'X':1, 'Y':2, 'Z':3}

def part1():
    return sum( [score_choix[b] + score_win[win[a][b]] for a,b in parties])
    
meaning = {'X':-1, 'Y':0, 'Z':1}
def strategy(opponent, result):
    """renvoie la strategy à choisir pour la deuxième partie"""
    for x in win[opponent]:
        if meaning[result] == win[opponent][x]:
            return x

def part2():
    return sum( [score_choix[strategy(a,b)] + score_win[win[a][strategy(a,b)]] for a,b in parties])

print(part1())
print(part2())