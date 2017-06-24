#!bin/user/python

import sys
key = None
val = None

for line in sys.stdin:
    line = line.strip().split('\t')
    sub = line[0].split(',')
    if (key != sub[0] and val != sub[1]):
        key = sub[0]
        val = sub[1]
    else:
        print(key + ',' + val)
        key = sub[0]
        val = sub[1]
print(key + ',' + val)


