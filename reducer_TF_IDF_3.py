#!bin/user/python

import sys
doc = None
D = dict()
L = list()

for line in sys.stdin:
    line = line.strip().split('\t')
    line1 = line[1].strip().split(';')
    if doc is None:
        D[line[0]] = [line1[1]]
        doc = line[0]
    else:
        if doc == line[0]:
            D.get(line[0]).append(line1[1])
        else:
            for i in range(1, len(D.values()[0])):
                pass
            D[line[0]] = [line1[1]]
    print(D)