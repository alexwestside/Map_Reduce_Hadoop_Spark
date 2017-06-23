#!bin/user/python

import sys
D = dict()
sum = 0
count = 0


for line in sys.stdin:
    line = line.strip().split('\t')
    key = line[0]
    val = line[1]
    if line[0] in D:
        D[line[0]].append(line[1])
    else:
        D[line[0]] = [line[1]]
for key in D:
    line = D[key]
    for item in line:
        sum += int(item)
        count += 1
    # print(key + "\t" + str(float(sum) / float(count)))
    print('{:s}{:s}{:.0f}'.format(key.strip(), "\t", (sum / count)))
    sum = 0
    count = 0
