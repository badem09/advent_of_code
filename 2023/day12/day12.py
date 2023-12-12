input_list = [e.replace('\n', '').split() for e in open('input.txt').readlines()]
input_list = [[e[0], [int(x) for x in e[1].split(',')]] for e in input_list]


def separate_by_records(str,records):
    res = []
    i = 0
    marge = []
    for r in records:
        stop_by_h = False
        if r + i < len(str):
            e= ''
            while str[i] == '.':
                #e+=str[i]
                i+=1
            e += str[i:i+r]
            j=0
            while str[r+j+i] == '#':
                stop_by_h = True
                e += str[r+j+i]
                j+=1
            i += r+j

            e += '' if len(e)<r+1 else str[i]
            #e+=str[i]
            i+=1
            res.append(e)
        else :
            res.append(str[i:])
    if len(str) > sum(len(e) for e in res):
        marge = str[i:]
        #res.append()
    return res, marge




for l in input_list: # l = '?#?#?#?#?#?#?#? 1,3,1,6'
    #print(l, l[0].count('?'), "nb of #" ,l [0].count('#'),"tot wanted:", sum(l[1]))
    #garder les nb pas present
    wl = l[0] #wl = [?#?#?#?#?#?#?#?]
    records = l[1]
    wl, marge = separate_by_records(wl,records)
    print(l[0])

    for i in range(len(wl)):
        if wl[i].count('#') == records[i]:
            print(wl[i], 'ok', records[i])
            #n_possible == 1
        if wl[i].count('#') < records[i]:
            print(wl, records[i])
            print([x for x in wl[i] if x !='.'])
            print(len([x for x in wl[i] if x !='.']) - records[i]+1 )
        print()







