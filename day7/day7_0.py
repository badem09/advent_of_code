f = open("inputCommande.txt","r")
#p1: 1783610, p2: 4964676
input = list(f)
liste_f = [l[:-1] if '\n' in l else l for l in list(f)]
dir = []
arbre = {}


def set_arbre(i,elem):
    dir_atteint = None
    current_dir = elem
    for j in range(i,len(liste_f)):
        ligne = liste_f[j].split(" ")
        if ligne[0] == '$':
            if ligne[1] == "cd" and ligne[2] == current_dir:
                dir_atteint = True
                if ligne[2] != '..':
                    current_dir = ligne[2]
                    dir.append(current_dir)
                else:
                    current_dir = dir[dir.index(current_dir)-1]
            elif ligne[1] == 'ls' and dir_atteint != None:
                size = 0
                while j+1<len(liste_f) and liste_f[j+1][0] != "$":
                    ligne2 = liste_f[j + 1].split(" ")
                    if 'dir' in ligne2:
                        #if ligne2[1] in arbre.keys():
                        #    size+= arbre[ligne2[1]]
                        #else:
                            size += set_arbre(j + 1, ligne2[1])
                    else:
                        size += int(ligne2[0])
                    j+=1
                arbre.update({current_dir : size})
                return size

def sumSize(dir,arbre):
    size = 0
    for val in arbre[dir]:
        if val[1] == 'dir':
            size += sumSize(val[0],arbre)
        else:
            size += int(val[1])
    return size




liste_input = list(input)
def findPath(dir,path,i):

    for j in range(i,len(liste_input)):
        if liste_input[j][0] == "$":
            if "cd" in liste_input[j]:
                current_dir = liste_input[j].split(' ')[2]
                path += " " + current_dir
                findPath(current_dir,path,j+1)
        else:
            return path(liste_input[j].split(' ')[1])





findPath('/','/',0)