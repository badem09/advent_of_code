import copy
from pprint import pprint

from IPython.display import display
input = open('input.txt','r').read()

input_l = [e.split('\n') for e in input.split('\n\n')]
input_l = [[list(e) for e in row] for row in input_l ]

left_v = []
above_h = []


def find_line(pattern):
    for i in range(len(pattern) - 1):  # vertical line
        if pattern[i] == pattern[i + 1]:
            left = pattern[0:i]
            right = pattern[i + 2:]
            k = 0
            for j in range(min(len(left), len(right))):
                if left[len(left) - j - 1] != right[j]:
                    return []
                k += 1
            return i + 1
    return []


for pattern in input_l:
    res = find_line(pattern)
    if res == []:
        pattern = list(map(list, zip(*copy.deepcopy(pattern))))
        #3e pattern trouve pas de left v
        res = find_line(pattern)
        left_v.append(res)
    else :
        above_h.append(res)

print(sum([e for e in left_v if isinstance(e,int)]+[e*100 for e in above_h if isinstance(e,int)]))
print(above_h, '\n',left_v)



