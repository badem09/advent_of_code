f = open("input.txt",'r')
input = list(f)

dir_file = {} #nom file,type,level
ligne_dir = [] #dir : sa ligne
i=0

def set_dir(level,i,dir):
    if level == 1:
        ligne_dir.append(('racine',1))
        set_dir(level+1, i + 1, dir)
    else:
        if i < len(input):
            ligne = input[i].split(" ")
            tiret = ligne.index("-")
            level = tiret // 2 + 1
            if 'dir' in ligne[tiret + 2]:
                ligne_dir.append((ligne[tiret + 1],i))
            if 'file' in ligne[tiret + 2]:
                if level not in dir.keys():
                    dir.update({level:[[ligne[tiret + 1] , ligne[tiret + 2] , i]]})
                elif level in dir.keys():
                    dir[level].append([ligne[tiret+1] ,ligne[tiret+2], i])
            i+=1
            set_dir(level,i,dir)



def set_arbre(dir):
    for key in dir.key():
        pass

set_dir(1, 0, dir_file)
print(dir_file)
print(ligne_dir[::-1])
