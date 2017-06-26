#!bin/user/python

from __future__ import print_function
import sys

for line in sys.stdin:
    line = line.strip().split('\t')
    print(line[2])