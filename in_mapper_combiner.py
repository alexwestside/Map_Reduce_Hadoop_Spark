#!user/bin/python

import sys

for line in sys.stdin:
    key = line.strip().split('\t')
    for key2 in key:
        key2 = key2.split(' ')
        D = dict()
        for key3 in key2:
            exist = key3 in D
            if exist:
                D[str(key3)] = D.get(str(key3)) + 1
            else:
                D[str(key3)] = 1
        for i in D:
            print(i + '\t' + str(D.get(i)))