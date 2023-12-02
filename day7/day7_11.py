file = open("input.txt")

liste_file = list(file)
dict_dir = {}
current_dir = []
niveau = 0

for i in range(len(liste_file)):
    dir_content = []
    if "cd" in liste_file[i] and "$" in liste_file[i]:
        if ".." in liste_file[i]:
            current_dir.remove(current_dir[-1])
            niveau -=1
        else:
            current_dir.append((niveau,liste_file[i].split(" ")[2]))
            niveau +=1

    elif "ls" in liste_file[i] and "$" in liste_file[i]:
        j = i + 1
        while j < len(liste_file) and "$" not in liste_file[j]:
            if "dir" in liste_file[j]:
                dir_content.append((niveau,liste_file[j].split(" ")[1]))
            else:
                dir_content.append((niveau,liste_file[j]))
            j += 1
        name = current_dir[-1]
        dict_dir.update({name : dir_content})

dict_size = {}

def sizeOfDir(name,liste_dir):
    size = 0
    for enfant in liste_dir:
        name_e = enfant[1].split(" ")

        if name_e[0].isdigit():
            size+= int(name_e[0])
        else:
            size += sizeOfDir(enfant,dict_dir[enfant])
    dict_size.update({name : size})
    return size


sizeOfDir("0, '/\n')",dict_dir[(0, '/\n')])

sum = s2 = 0
for key,val in dict_size.items():
    print(key)
    if val <= 1e5:
        sum += val
print(sum)

# Vraie réponse : 1783610
#Ma réponse : 958081