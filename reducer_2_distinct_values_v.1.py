#!bin/user/python

import sys
d = dict()

for line in sys.stdin:
    line = line.strip().split('\t')
    if line[1] in d:
        d[line[1]] = int(d.get(str(line[1]))) + int ('1')
    else:
        d[line[1]] = 1
for i in d:
    print(i + '\t' + str(d.get(str(i))))
