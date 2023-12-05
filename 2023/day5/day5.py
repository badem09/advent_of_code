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

"""seeds = [int(e) for e in list_input[0].split(":")[1].split(' ') if len(e)>0]
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
"""

print(maps)
for map in maps[::-1]:
    for range_ in map:
        print(range_)

