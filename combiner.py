#!user/bin/python

import sys

key = None
D = dict()

for line in sys.stdin:
    key = line.strip().split('\t')
    exist = str(key) in D
    if exist:
        D[str(key)] = D.get(str(key)) + 1
    else:
        D[str(key)] = 1
print(D)