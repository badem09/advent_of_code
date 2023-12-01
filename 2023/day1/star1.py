import re
#[word for sentence in text for word in sentence]

input = open("input.txt", "r")

#s = [s for lign in input for s in lign if not s.isalpha()]
star_1 = sum([int(x[0]+x[-1]) for x in [list(re.sub('\D', '', lign)) for lign in input] if len(x)>0])
print(star_1)

input = open("input.txt", "r")
digits = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', "ten":'10'}
#star_2 = [l for l in input]

ligns_modif = []
for l in input: 
    l2 = l
    for d in digits.keys():
        while d in l2:
            i = l2.find(d)
            l2 = l2[:i+1] + digits[d] + l2[i+(len(d)-1):] 
    print(l,l2, [int(x[0]+x[-1]) for x in [list(re.sub('\D', '', l2))]] , "\n")
    ligns_modif.append(l2)
            
star_2 = sum([int(x[0]+x[-1]) for x in [list(re.sub('\D', '', lign)) for lign in ligns_modif]])

print(star_2)