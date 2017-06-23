#!bin/user/python

import sys
key = None
sum = 0
count = 0

for line in sys.stdin:
    line = line.strip().split('\t')
    subline = line[1].strip().split(';')
    if (key != line[0]):
        if key:
            print(key + '\t' + str(sum) + ';' + str(count))
        key = line[0]
        sum = int(subline[0])
        count = int(subline[1])
    else:
        sum += int(subline[0])
        count += int(subline[1])
print(key + '\t' + str(sum) + ';' + str(count))