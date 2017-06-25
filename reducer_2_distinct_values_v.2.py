#!bin/user/python

import sys

D = dict()

for line in sys.stdin:
    line = line.strip().split('\t')
    if line[1] not in D:
        D[line[1]] = list(line[0])
    else:
        if line[0] not in D.get(line[1]):
            D[line[1]].append(line[0])
for i in D:
    print(i + '\t' + str(len(D.get(str(i)))))