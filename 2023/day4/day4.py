
list_input = [e.replace('\n', '') for e in list(open('input.txt', 'r'))]
cards = [[e.split(":")[1].split('|')] for e in list_input]
cards = [[e[0].split(' '),e[1].split(' ')] for x in cards for e in x]
score = 0
scratch = cards.copy()
dict_wn = dict()
for i,card in enumerate(cards):
    wn = 0
    for num in card[0]:
        if num in card[1] and len(num)>0:
            wn += 1
    if wn > 0 :
        score += 2**(wn-1)
    dict_wn[i+1] = wn

queue = [i+1 for i,e in enumerate(cards) ]
score2 = 0
while len(queue)>0:
    to_add = []
    for id in queue:
        wn = dict_wn[id]
        for i in range(id+1,id+wn+1):
            to_add.append(i)

    score2 += len(queue)
    queue = to_add
    to_add= []

print(score2,score)
