#!bin/user/python

import sys

D = dict()

for line in sys.stdin:
    line = line.strip().split('\t')
    if line[1] is not D:
        D[line[1]] = line[0]
    else:
        if D.get(str(line[1])) != line[0]:
            D[line[1]] = D.get(str(line[1])) + 1
print(D)
# for i in D:
#     print(i + '\t' + str(D.get(str(i))))