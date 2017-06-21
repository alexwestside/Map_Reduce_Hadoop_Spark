#!user/bin/python

import sys

(_key, _val) = (None, 0)

for line in sys.stdin:
    (key, val) = line.strip().split('\t')
    if (_key and _key != key):
        print(_key + '\t' + str(_val))
        (_key, _val) = (key, val)
    else:
        (_key, _val) = (key, int(val) + int(_val))
print(_key + '\t' + str(_val))



