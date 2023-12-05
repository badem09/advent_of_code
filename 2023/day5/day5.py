input = open('input.txt','r').readlines()
input_str = "".join(input)
list_input = input_str.split('\n\n')

seeds = [int(e) for e in list_input[0].split(":")[1].split(' ') if len(e)>0]
print(seeds)
maps = []
for e in list_input:
    e = e.split(':')
    if e[0] != 'seeds':
        x = [x.split(' ') for x in e[1].split('\n') if len(x)>0]
        maps.append(x)

res = []
min_seed1 = 100000000000000
for i,seed in enumerate(seeds):
    print(i)
    for ranges in maps:
        for range_ in ranges:
            if int(range_[1]) <= int(seed) <= int(range_[1]) + int(range_[2]) - 1:
                seed += (int(range_[0]) - int(range_[1]))
                break
    if min_seed1> seed:
        min_seed1 = seed

print(min_seed1)

seeds = [int(e) for e in list_input[0].split(":")[1].split(' ') if len(e)>0]
seeds = [range(seeds[i],seeds[i] + seeds[i+1]) for i in range(0,len(seeds),2)]
res = []
new_seeds = []
min_seed = 100000000000000
for i,r_seed in enumerate(seeds):
    for s in r_seed:
        for ranges in maps:
            for range in ranges:
                if int(range[1]) <= int(s) <= int(range[1]) + int(range[2]) - 1:
                    s += (int(range[0]) - int(range[1]))
                    break
        if min_seed > s:
            min_seed = s

print(min_seed)