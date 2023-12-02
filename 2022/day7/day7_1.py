f = open("input.txt",'r')
input = [l[:-1] if '\n' in l else l for l in list(f)]

dict = {}

for i in range(len(input)):
    if 'dir' in input[i]:
        level_dir = input[i].index("-")+1 // 2
        index_name = input[i].index("-") + 2
        name = input[i][index_name]
        size_dir = 0
        for j in range(i,len(input)):
            if 'file' in input[j]:
                level_file = input[j].index("-")+1 // 2
                if level_dir == level_file:
                    break
                size_file = int(input[j].split(' ')[-1].split("=")[1][:-1])
                size_dir += size_file
        dict.update({name: size_dir})

reste = [i[1] for i in dict.items() if int(i[1])<=100000]
print(sum(reste))
