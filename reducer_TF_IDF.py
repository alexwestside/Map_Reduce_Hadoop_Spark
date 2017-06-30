#!bin/user/python

import sys
import re

for line in sys.stdin:
    line = line.strip().split('\t')
    line1 = line[0].split('#')
