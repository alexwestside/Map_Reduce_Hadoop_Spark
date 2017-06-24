#!bin/user/python

import sys
key = None

for line in sys.stdin:
    line = line.strip().split(',')
    print(line[1] + '\t' + '1')
