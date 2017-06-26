#!bin/user/python

from __future__ import print_function
import sys
key = None
val = None

for line in sys.stdin:
    line = line.strip().split('\t')
    if key != line[0]:
        val = line[1]
        key = line[0]
    else:
        if (val == 'A' and line[1] == 'B') or (val == 'B' and line[1] == 'A'):
            print(key)
