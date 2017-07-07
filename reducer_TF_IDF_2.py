#!bin/user/python

import sys

for line in sys.stdin:
    line = line.strip().split('\t')
    print(line[0] + '\t' + line[1] + ';'+ line[2] + ';'+ '1')