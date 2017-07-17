#!bin/user/python

import sys
doc = None
D = dict()
n = 0

for line in sys.stdin:
    line = line.strip().split('\t')
    line1 = line[1].strip().split(';')
    if doc is None:
        D = dict()
        D[line[0]] = [line1[1]]
        doc = line[0]
        n = line1[0]
    else:
        if doc == line[0]:
            D.get(line[0]).append(line1[1])
        else:
            val = D.values()
            ln = len(list(D.values())[0])
            for i in range(0, ln if ln > 1 else 1):
                print(list(D.keys())[0] + '#' + (str(n) if ln < 2 else str(i + 1)) + '\t' + list(val[0][i]) + '\t' + str(ln))
            D = dict()
            D[line[0]] = [line1[1]]
            doc = line[0]
            n = line1[0]
val = D.values()
ln = len(list(D.values())[0])
for i in range(0, ln if ln > 1 else 1):
    print(list(D.keys())[0] + '#' + (str(n) if ln < 2 else str(i + 1)) + '\t' + list(val[0][i] + '\t' + str(ln)))