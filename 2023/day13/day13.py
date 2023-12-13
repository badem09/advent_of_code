import copy

input = open('input.txt','r').read()

input_l = [[list(e) for e in row] for row in [e.split('\n') for e in input.split('\n\n')] ]

left_v = []
above_h = []
left_v2 = []
above_h2 = []

def nb_errors(liste1, liste2):
    r = 0
    for i in range(min(len(liste1),len(liste2))):
        if liste1[i] != liste2[i]:
            r+=1
    return r

def fix_smudge (pattern):
    # find l'axe qui a quune erreur
    for i in range(len(pattern) - 1):  # vertical line
        if pattern[i] == pattern[i + 1]:
            left = pattern[0:i][::-1]
            right = pattern[i + 2:]
            nb_err = nb_errors(left, right)
            if nb_err == 1:
                return len(left) + 1
    return -1

def find_line(pattern):
    for i in range(len(pattern) - 1):  # vertical line
        if pattern[i] == pattern[i + 1]:
            left = pattern[0:i][::-1]
            right = pattern[i + 2:]
            nb_err = nb_errors(left,right)
            if nb_err == 0 or i in (0,len(pattern)-1):
                return len(left) + 1
    return -1


for pattern in input_l:
    res = find_line(pattern)
    if res == -1: # if no horizontal symetry
        pattern1 = list(map(list, zip(*copy.deepcopy(pattern))))
        res = find_line(pattern1)
        left_v.append(res)
    else :
        above_h.append(res)

    res2 = fix_smudge(pattern)
    if res2 == -1:
        pattern2 = list(map(list, zip(*copy.deepcopy(pattern))))
        res2 = fix_smudge(pattern2)
        left_v2.append(res2)
    else:
        above_h2.append(res2)







print("partie 1 :",sum([e for e in left_v if isinstance(e,int)]+[e*100 for e in above_h if isinstance(e,int)]))
print("partie 2 :",sum([e for e in left_v2 if isinstance(e,int)]+[e*100 for e in above_h2 if isinstance(e,int)]))
print(left_v2)
print(above_h2)




