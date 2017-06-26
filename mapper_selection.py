#!bin/user/python

from __future__ import print_function
import sys
s = "user10"

for line in sys.stdin:
    line1 = line.strip().split('\t')
    if s in line1:
        print(line, end='')