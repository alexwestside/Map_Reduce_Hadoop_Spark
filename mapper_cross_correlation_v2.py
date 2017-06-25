#!bin/user/python

import sys

T = tuple()
D = dict()
count = 1
key = None
j = None


for line in sys.stdin:
    line = line.strip().split(' ')
    for i in line:
        for j in line:
            if i != j:
                T += tuple((i + ',' + j).split(' '))
for i in T:
    line = i.split(',')
    if key != line[0]:
        if key:
            sys.stdout.write(key + '\t')
            # print(key)
            for k in D:
                s = k + ':' + str(D[k])
                sys.stdout.write(',')
            print()
        D = dict()
        key = line[0]
        D[line[1]] = int(count)
    else:
        if line[1] not in D:
            D[line[1]] = int(count)
        else:
            D[line[1]] += int(1)
sys.stdout.write(key + '\t')
for k in D:
    if j == k:
        sys.stdout.write(',')
    j = k
    sys.stdout.write(k + ':' + str(D[k]))


