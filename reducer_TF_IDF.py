#!bin/user/python

import sys
count = 0
doc = None
num = None


for line in sys.stdin:
    line = line.strip().split('\t')
    if doc is None:
        doc = line[0].split('#')[0]
        num = line[0].split('#')[1]
        count += int(1)
    else:
        if doc == line[0].split('#')[0] and num == line[0].split('#')[1]:
            count += int(1)
        else:
            print(doc + '\t' + num + '\t' + str(count))
            count = 0
            doc = line[0].split('#')[0]
            num = line[0].split('#')[1]
            count += int(1)
