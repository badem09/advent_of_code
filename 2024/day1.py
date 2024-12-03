liste = list(open("input.txt", "r"))
l = sorted([int(e.replace('\n','').split('   ')[0]) for e in liste])
r = sorted([int(e.replace('\n','').split('   ')[1]) for e in liste])
diff = [abs(l[i]-r[i]) for i in range(len(l))]
print(sum(diff))

#star 2:

res = [l[i] * r.count(l[i]) for i in range(len(l))]
print(sum(res))