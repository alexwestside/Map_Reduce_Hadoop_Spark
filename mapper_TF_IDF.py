#!bin/user/python

import sys
import re

for line in sys.stdin:
    line = re.split((r'[^\d\w]'), line.strip(''))
    for word in line:
        if word and word != line[0]:
            print(word + '#' + line[0] + '\t' + '1')