liste = [e.replace('\n', '').split(' ') for e in list(open("input.txt", "r"))]
liste = [[int(x) for x in e] for e in liste]


def is_safe(level):
    diff = level[0] - level[1]
    og_signe = 'p' if diff >= 0 else 'n'
    for j in range(len(level)-1 ):
        diff = level[j] - level[j+1]
        signe = 'p' if diff >= 0 else 'n'
        if diff==0 or abs(diff) > 3 or signe != og_signe:
            #print('u', level, level[j], level[j+1], diff )
            return False
    else:
        return True


def star1():
    safe = 0
    for e in liste:
        safe += 1 if is_safe(e) else 0
    return safe

def star2():
    safe = 0
    for level in liste:
        if is_safe(level) :
            safe += 1
        else:
            for i in range(len(level)):
                if is_safe([l for ic, l in enumerate(level) if ic != i]):
                    safe +=1
                    break
    return safe

print(star1())
print(star2())
