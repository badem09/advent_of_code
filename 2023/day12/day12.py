input_list = [e.replace('\n', '').split() for e in open('input.txt').readlines()]
input_list = [[e[0], [int(x) for x in e[1].split(',')]] for e in input_list]

def is_separated(str):
    for e in str:
        if str.count(e[0]) != len(str):
            return False
    return True

def separate_by_records(str,records):
    res = []
    i = 0
    for r in records:
        if r + i < len(str):
            e= ''
            while str[i] == '.':
                e+=str[i]
                i+=1
            e += str[i:i+r]
            j=0
            while str[r+j+i] == '#':
                e += str[r+j+i]
                j+=1
            i += r+j

            e += str[i]
            i+=1
            res.append(e)
        else :
            res.append(str[i:])
    if len(str) > sum(len(e) for e in res):
        print(i)
        res += str[i:]
    return res




for l in input_list: # l = '?#?#?#?#?#?#?#? 1,3,1,6'
    #print(l, l[0].count('?'), "nb of #" ,l [0].count('#'),"tot wanted:", sum(l[1]))
    #garder les nb pas present
    wl = l[0] #wl = [?#?#?#?#?#?#?#?]
    records = l[1]
    wl = separate_by_records(wl,records)
    print(sum(len(e) for e in wl), len(l[0]))
    print(records,wl,l[0])
    #print(records,wl)
    #print([len([e for e in s if e in '?'])-r+1 for s,r in zip(wl,records)])





