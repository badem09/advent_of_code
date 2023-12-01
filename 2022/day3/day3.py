#part1
min = "abcdefghijklmnopqrstuvwxyz"
lettres = "_" + min + min.upper()

f = open("input.txt","r")
sum1 = sum2 = c = 0
trois = []
for l in f:
    c+=1
    #partie 1
    l1 = l[:len(l)//2]
    l2 = l[len(l)//2:]
    while len(l1) > 0:
        if l1[0] in l2:
            sum1+=lettres.index(l1[0])
            break
        else:
            l1 = l1[1:]
            l2.replace(l1[0],"")
    trois.append(l)
    #partie 2 :
    if c % 3 == 0:
        while len(trois[0]) > 0:
            if trois[0][0] in trois[1] and trois[0][0] in trois[2]:
                sum2 += lettres.index(trois[0][0])
                print(trois[0][0])
                trois = []
                break
            else:
                trois[0] = trois[0][1:]
                trois[1].replace(trois[0][0],"")
                trois[2].replace(trois[0][0], "")
print(sum1,sum2)

sum2