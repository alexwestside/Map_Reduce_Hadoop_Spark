#!bin/user/python

import sys
key = None
i = 0

for line in sys.stdin:
    line = line.strip().split('\t')
    # print(line)
    sub_line = line[1].split(',')
    # print(sub)
    for key in sub_line:
        print(line[0] + ',' + key + '\t' + '1')


