f = open("inputTest.txt","r")


def contains_duplicate(i,l):
    for j in range(i,i+4):
        print(l[i:i+4])
        if l[i:i+4].count(l[j])>1:
            return False
    return True
first_marker = []
i=0
for l in f:
    while not contains_duplicate(i,l):
        i += 1
    first_marker.append(i+3+1)
    i = 0

print(first_marker)

