#!bin/user/python

from __future__ import print_function
import sys
key = None
val = None

for line in sys.stdin:
    line = line.strip().split('\t')
    if key != line[0] and (line[1] == 'A' or line[1] == 'B'):
        print(line[0])
        key = line[0]


