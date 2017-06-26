#!bin/user/python

from __future__ import print_function
import sys

for line1 in sys.stdin:
    line1 = line1.strip().split(' ')
    for i in line1:
        T = tuple()
        for j in line1:
            if i != j:
                T += tuple((i + ',' + j).split(' '))
        count = 1
        D = dict()
        key = None
        j = None
        i = None
        for i in T:
            line = i.split(',')
            if key != line[0]:
                if key:
                    sys.stdout.write(key + '\t')
                    for k in D:
                        s = k + ':' + str(D[k])
                        print(s, end='')
                        if i != key and len(D) > 1:
                            sys.stdout.write(',')
                            i = key
                    print()
                D = dict()
                key = line[0]
                D[line[1]] = int(count)
            else:
                if line[1] not in D:
                    D[line[1]] = int(count)
                else:
                    D[line[1]] += int(1)
        print(key + '\t', end='')
        for k in D:
            s = k + ':' + str(D[k])
            print(s, end='')
            if i != key and len(D) > 1:
                sys.stdout.write(',')
                i = key
        print()