import re

input = open("input.txt", "r")
star_1 = sum([int(x[0]+x[-1]) for x in [list(re.sub('\D', '', lign)) for lign in input] if len(x)>0])

input = open("input.txt", "r")
digits = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', "ten":'10'}

ligns_modif = []
for l in input: 
    l2 = l
    for d in digits.keys():
        while d in l2:
            i = l2.find(d)
            l2 = l2[:i+1] + digits[d] + l2[i+(len(d)-1):]
    ligns_modif.append(l2)
            
star_2 = sum([int(x[0]+x[-1]) for x in [list(re.sub('\D', '', lign)) for lign in ligns_modif]])

print(star_2, star_1)