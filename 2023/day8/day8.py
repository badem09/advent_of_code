import sys
import math
from functools import reduce

intructions = 'LLRLLRLRLRRRLLRRRLRRLRLRLRLRLRLRRLRRRLRLLRRLRRLRRRLLRLLRRLLRRRLLLRLRRRLLLLRRRLLRRRLRRLRLLRLRLRRRLRRRLRRLRRLRRLRLLRRRLRRLRRRLLRRRLRLRRLLRRLLRLRLRRLRRLLRLLRRLRLLRRRLLRRRLRRLLRRLRRRLRLRRRLRRLLLRLLRLLRRRLRLRLRLRRLRRRLLLRRRLRRRLRRRLRRLRLRLRLRRRLRRLLRLRRRLRLRLRRLLLRRRR'

input_list = [e.replace('\n','').replace('(','').replace(')','').replace(' ','').split('=')  for e in open('input.txt','r').readlines()]
starts = []

for i in range(len(input_list)):
    input_list[i] = [input_list[i][0], input_list[i][1].split(',')]
    if input_list[i][0][-1] == 'A':
      starts.append(input_list[i][0])
dict_ = {e[0]:(e[1][0],e[1][1]) for e in input_list}

# part 1
j = 0
s = 'AAA'
while s != "ZZZ":
  if intructions[j % len(intructions)] == 'L':
        s = dict_[s][0]
  if intructions[j % len(intructions)] == 'R':
        s = dict_[s][1]
  j+=1


#part 2
# to do the 2nd part with reasonable time we need to find out for each
res = []
for i,s in enumerate(starts):
  j = 0
  while starts[i][-1] != "Z":
    if intructions[j % len(intructions)] == 'L':
          starts[i] = dict_[starts[i]][0]
    if intructions[j % len(intructions)] == 'R':
          starts[i] = dict_[starts[i]][1]
    j+=1
  res.append(j)


print('star 1:', j, "star 2:", reduce(lambda x,y:(x*y)//math.gcd(x,y),res))

