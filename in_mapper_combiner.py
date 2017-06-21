#!user/bin/python

import sys

D = dict()

for line in sys.stdin:
    key = line.strip().split('\t')
    for key2 in key:
        key2 = key2.strip().split(' ')
        print(key2)
        exist = str(key2) in D
        if exist:
            D[str(key2)] = D.get(str(key2)) + 1
        else:
            D[str(key2)] = 1
print(D)