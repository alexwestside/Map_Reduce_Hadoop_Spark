#!bin/user/python

import sys
import re

for line in sys.stdin:
    line = filter(bool, re.split((r'[^\d\w]'), line.strip('')))
        for word in line:
            print(word + '#' + line[0] + '\t' + '1')