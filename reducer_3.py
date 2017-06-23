#!bin/user/python

import sys
count = 0
sum = 0
key = None

for line in sys.stdin:
    line = line.strip().split('\t')
    if key != line[0]:
        if key:
            print('{:s}{:s}{:d}'.format(key, '\t', int(sum / count)))
        key = line[0]
        count = 1
        sum = int(line[1])
    else:
        sum += int(line[1])
        count += 1
print('{:s}{:s}{:d}'.format(key, '\t', int(sum / count)))