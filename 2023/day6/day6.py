# instruction : https://adventofcode.com/2023/day/6

import math, time

input = open('input.txt',('r'))
l = "".join(input).split("\n")
times = [int(e) for e in l[0].split(":")[1].split(' ') if e!='']
distances = [int(e) for e in l[1].split(":")[1].split(' ') if e!='']

times2 = int(l[0].split(":")[1].replace(' ',''))
distances2 = int(l[1].split(":")[1].replace(' ',''))

def naive_approach(times,distances):
    """
    The naive approach is to go through the range(0,distance) and test each waiting time
    """
    wt = []
    j = 0
    for i,t in enumerate(times):
        wt.append([])
        for wait in range(t+1):
            td = wait * (t-wait) # traveled distance
            d = distances[i]
            if td > d and t not in wt[j]:
                wt[j].append(wait)
        j+=1
    return wt

wt1 = naive_approach(times, distances)
print('star 1 : ', math.prod([len(e) for e in wt1]))

def math_approach(time, distance):
    """
    The smart approach.
    Let lt be the lower (first) valid waiting time
    Let ht be the higher (last) valid waiting time
    Let {1 : distance} be {1, 2, 3, ..., distance}
    The {1 : distance} is composed as follow : {1 : lt} + {lt : ht}  + {ht : distance}
    And card({1 : x}) == card({y : distance}) (meaninf they have the same no of elements)
    So we only have the look for x.
    """
    lt = 0
    for wait in range(time+1):
        td = wait * (time-wait) # traveled distance
        d = distance #distance of the race
        if td > d:
            break
        else:
            lt += 1
    return lt

start = time.time()
lt = math_approach(times2, distances2)
end = time.time()

nb_of_possibilities = (times2 -1) - (2 * (lt-1))
print("star 2 :" , nb_of_possibilities)
print("time of exec star 2 : " ,end - start)