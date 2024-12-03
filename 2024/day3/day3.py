import re

#star 1
p = r"mul\((\d{1,3}),(\d{1,3})\)"
lines = open("input.txt").readlines()
res = [(int(e[0]),int(e[1])) for l in lines for e in re.findall(p, l)]
print(sum([e[0]*e[1] for e in res]))

# star 2
str = "".join(lines)

valid_matches = []
for e in str.split('do()'):
    i = len(e)-1 if "don't()" not in e else e.index("don't()")
    elem = e.split("don't()")[0]
    valid_matches.append(re.findall(p,elem))

valid_matches = [e for x in valid_matches for e in x]
print(sum([int(e[0])*int(e[1]) for e in valid_matches]))

#Part 1: 174960292
#Part 2: 56275602
         
