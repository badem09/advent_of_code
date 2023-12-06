import time

input = open('input.txt','r').readlines()
input_str = "".join(input)
list_input = input_str.split('\n\n')

seeds = [int(e) for e in list_input[0].split(":")[1].split(' ') if len(e)>0]
maps = []
for e in list_input:
    e = e.split(':')
    if e[0] != 'seeds':
        x = [x.split(' ') for x in e[1].split('\n') if len(x)>0]
        maps.append([list(map(int, e)) for e in x ])

start = time.time()
min_seed1 = 100000000000000
for i,seed in enumerate(seeds):
    for ranges in maps:
        for range_ in ranges:
            if range_[1] <= seed <= range_[1] + range_[2] - 1:
                seed += range_[0] - range_[1]
                break
    if min_seed1> seed:
        min_seed1 = seed
end = time.time()
print("min_seed1",min_seed1, end-start)
"""
seeds = [int(e) for e in list_input[0].split(":")[1].split(' ') if len(e)>0]
seeds = [range(seeds[i],seeds[i] + seeds[i+1]) for i in range(0,len(seeds),2)]
res = []
new_seeds = []
min_seed = 100000000000000
for i,r_seed in enumerate(seeds):
    print(i,r_seed)
    for s in r_seed:
        print(s)
        for ranges in maps:
            for range in ranges:
                if int(range[1]) <= int(s) <= int(range[1]) + int(range[2]) - 1:
                    s += (int(range[0]) - int(range[1]))
                    break
        if min_seed > s:
            min_seed = s
        print(min_seed)
        print()
print(min_seed)

bas en haut
print(seeds)
print(maps)
min_loc = -1
val = min_loc
#seeds = list(range(79,79+14))+list(range(55,55+13))
print('seeds')
while val not in seeds:
    print(min_loc,val)
    min_loc+=1
    val = min_loc
    for ranges in maps[::-1]:
        for range_ in ranges:
            print(min_loc, val, int(range_[1]), int(range_[1]) + int(range_[2]) - 1,range_)
            if int(range_[1]) <= val <= int(range_[1]) + int(range_[2]) - 1:
                print(min_loc,val, int(range_[1]) , int(range_[1]) + int(range_[2])-1 ,int(range_[1]) - int(range_[0]), range_, "ok")
                val += (int(range_[1]) - int(range_[0]))
                break
    print()
print(min_loc,val)
print(seeds)
# autre idee: couper les intervalles selon passages des regles et prendre loc de borne inferieure
def get_location(range_seed, level):
    for range in maps[level]:
        print(range)
        if range_seed[0] >= int(range[1] and


print(seeds)
range_seeds = [range(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
for range_seed in range_seeds:


min_loc = -1 # = -1
val = min_loc
min_found = False
while not min_found:
    min_loc+=1
    val = min_loc
    for ranges in maps[::-1]:
        for range_ in ranges:
            prev_val = val + range_[1] - range_[0]
            if range_[1] <= prev_val <= range_[1] + range_[2] -1:
                val=prev_val
                break

    for i in range(0,len(seeds),2):
        if seeds[i] <= prev_val <= seeds[i] + seeds[i+1] - 1:
            print(prev_val)
            min_found = True
    print(prev_val)
print()
print(min_loc,val)
print(seeds)
"""

#range(82, 83) 7 [79, 81, 81, 81, 74, 74, 78, 78, 82]
# [79, 81, 81, 81, 74, 74, 78, 78, 82] should be [79, 81, 81, 81, 74, 78, 78, 82]
def get_location(range_seed, level,deroule,l,og_interval):
    print("start get_location", range_seed, "level:" ,level,deroule,l)
    mapped = False
    if level > 6:
        #print()
        print(range_seed, level,deroule)
        return range_seed[0]
    for range_ in maps[level]:
        liste_range = [] # liste range left to explore
        #print(range_, range_seed)
        if range_[1] <= range_seed[0] and range_seed[-1] <= range_[2]+range_[1]-1  : #if all range_seed fits into the interval
            to_add = range_[0] - range_[1]
            g = range_seed[0]
            d = range_seed[-1] + 1
            deroule.append(g + to_add)
            #print('range chosen:',range_)
            #print('next range before conversion :', range(g, d), "to_add:",to_add )
            l.append(get_location(range(g + to_add, d + to_add), level + 1,deroule.copy(), l.copy(), og_interval))
            #l.remove(l[-1])
            deroule.remove(deroule[-1])
            mapped = True

        elif range_seed[-1] - range_[1]  > 0 and  (range_[1]+ range_[2] -1) - range_seed[0]  >0 : # if they overlap # some of it fits
            g = max(range_[1],range_seed[0])
            d = min(range_[2]+range_[1] -1, range_seed[-1]) +1
            to_add = range_[0] - range_[1]
            deroule.append(g + to_add)
            #print('range chosen:',range_)
            #print('next range before conversion :', range(g, d), "to_add:",to_add )
            l.append(get_location(range(g+to_add, d+to_add), level + 1, deroule.copy(),
                                  l.copy(), og_interval))
            #l.remove(l[-1])
            deroule.remove(deroule[-1])
            mapped = True




    if not mapped:
        deroule.append(range_seed[0])
        #print('range chosen: no range')
        #print('next range before conversion :', range_seed, "to_add:", 0)
        l.append(get_location(range_seed,level+1,deroule.copy(), l.copy(),og_interval))
        #l.remove(l[-1])
        deroule.remove(deroule[-1])

    return l

print(seeds)
range_seeds = [range(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
locs = []
for range_seed in range_seeds:
    locs.append(get_location(range_seed,level=0, deroule=[range_seed[0]], l=list(), og_interval=range_seed))

print(range_seeds)
print(locs)
#print(min(locs, key=lambda x:x[0])[0])
#print(min(locs, key = lambda x: x[0]))

"""
if range_seed[-1] < range_[2] + range_[1] - 1: # "tout envoyé"
                l.append(get_location(range(range_seed[0] + to_add, range_seed[-1] + to_add), level + 1))
                break
            else:
                l.append(get_location((range(range_seed[0]+ to_add, range_[2]+range_[1]-1 + to_add)),level+1))
                range_seed = range(range_[2] + range_[1], range_[1])
            g = max(range_seed[0], range_[1])
            d = min(range_seed[1], range_[2])
            l.append(get_location(range(g,d),level+1))"""



