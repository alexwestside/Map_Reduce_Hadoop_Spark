#!bin/user/python

import sys
key = None
val = None

for line in sys.stdin:
    line = line.strip().split('\t')
    if key != line[0]:
        if val == 'A':
            print(key)
        key = line[0]
        val = line[1]
    else:
        if line[1] == 'B':
            key = None
            val = None
if val == 'A':
    print(key)