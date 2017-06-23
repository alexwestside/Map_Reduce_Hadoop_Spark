#!user/bin/python

import sys

D = dict()

for line in sys.stdin:
    line = line.strip().split('\t')
    for token in line:
        token = token.split(' ')
        for key in token:
            exist = key in D
            if exist:
                D[str(key)] = D.get(str(key)) + 1
            else:
                D[str(key)] = 1
for i in D:
    print(i + '\t' + str(D.get(i)))


