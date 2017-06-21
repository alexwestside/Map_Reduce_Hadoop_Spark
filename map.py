#!user/bin/python

import sys

for line in sys.stdin:
    for key in line.strip().split(" "):
        print(str(key) + "\t" + str(1))
