from itertools import product

f = open("input.txt","r")

tab = [list(i[:-1]) if i[-1] == '\n' else list(i) for i in f]
liste = [[] for i in range(len(tab))]
carte = [liste.copy() for i in range(len(tab))]

def isBorder(ligne,col,elem):
    if elem in tab[ligne]:
        if ligne == 0 or ligne == len(tab)-1:
            return True
        if col == 0 or col == len(tab)-1:
            return True
    return False

def isVisible(ligne,col):
    carte1 = carte
    elem = tab[ligne][col]
    print('debut fonction : ' , ligne,col,elem)
    if not isBorder(ligne,col,elem):
        for i in [0,1,-1]:
            if i == 0:
                for j in [-1,1]:
                    ni,ncol = i+ligne,j+col
                    new_elem = tab[ni][ncol]
                    print("comp : ", ni, ncol, new_elem)

                    if new_elem < elem:
                        if carte1[ni][ncol] == True:
                            return True
                        prochain = isVisible(ni,ncol)
                        if prochain:
                            print('fin fonction',new_elem,prochain)
                            carte1[i][j] = prochain
                            return prochain

            else:
                j = 0
                ni, ncol = i + ligne, j + col
                new_elem = tab[ni][ncol]
                print("comp : ", ni, ncol, new_elem)
                if new_elem < elem:
                    if carte1[ni][ncol] == True:
                        return True
                    prochain = isVisible(ni, ncol)
                    if prochain:
                        print('fin fonction', new_elem, prochain)
                        carte1[i][j] = prochain
                        return prochain
        return False
    return True



res = 0
for i in range(len(tab)):
    for j in range(len(tab[i])):
        print("\n\nSOURCE : " , i,j)
        visible = isVisible(i,j)
        carte[i][j] = visible
        if visible:
            res+=1
    print()

print(res)
print(98*98)

# rep : 1835 274176