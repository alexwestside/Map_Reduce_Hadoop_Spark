#!bin/user/python

import sys

D = dict()
T = tuple()

for line in sys.stdin:
    line = line.strip().split(' ')
    for i in line:
        for j in line:
            if i != j:
                s = (i + ',' + j).split(' ')
                T = T + tuple(s)
for i in T:
    print(i + '\t' + str(1))





