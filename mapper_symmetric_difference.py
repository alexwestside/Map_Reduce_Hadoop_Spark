#!bin/user/python

import sys
key = None
val = None

for line in sys.stdin:
    line = line.strip().split('\t')
    if key != line[0]:
        if key:
            print(key)
        key = line[0]
        val = line[1]
    else:
        if val != line[1]:
            key = None
            val = None
if key:
    print(key)
