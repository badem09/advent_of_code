
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
    dict_wn[i] = wn

print(dict_wn)
queue = [i for i,e in enumerate(cards) ]
score2 = 0
while len(queue)>0:
    to_add = []
    for id in queue:
        wn = dict_wn[id]
        print("id: " , id, "wn : ",wn)
        for i in range(id+1,id+wn+1):
            to_add.append(i)
            print("add : " ,id,i)
        print("to_add ", to_add)
    print(queue)
    score2 += len(queue)
    queue = to_add
    to_add= []

print(queue,score)
"""
queue = cards.copy()
start = True
to_do = []
score2 = 0
while start or len(queue) > 0:
    start = False
    for i in range(len(queue)):
        add = 0
        card = queue[i]
        for num in card[0]:
            if num in card[1] and len(num)>0:
                add += 1
        if add > 0 and cards.index(card) < len(cards) - 1:
            for j in range(1,add+1):
                to_do.append(cards[cards.index(card)+j])

        print(add)

    score2 += len(queue)
    queue = to_do
    print(len(to_do),score2)
    to_do = []


print(score,score2)
"""