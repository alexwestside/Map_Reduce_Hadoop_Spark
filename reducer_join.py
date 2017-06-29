# encoding=utf-8




# a = """user1	query:gugol
#     user1	url:google.ru
#     user2	query:stepic
#     user2	query:stepic kursi
#     user2	url:stepic.org
#     user2	url:stepic.org/explore/courses
#     user3	query:contact"""
# a = a.strip().split('\n')

import sys

def mapper():
    D = dict()
    for line in sys.stdin:
        line = line.strip().split('\t')
        line1 = line[1].split(':')
        if line[0] not in D:
            D[line[0]] = dict()
            D.get(line[0])[line1[0]] = list()
            D.get(line[0])[line1[0]].append(line1[1])
        else:
            if line1[0] not in D.get(line[0]):
                D.get(line[0])[line1[0]] = list()
                D.get(line[0])[line1[0]].append(line1[1])
            else:
                D.get(line[0])[line1[0]].append(line1[1])
    return D

def reducer(D):
    L = list()
    for key in D:
        if (D.get(key).get('query')):
            for key2 in D.get(key).get('query'):
                if (D.get(key).get('url')):
                    for key3 in D.get(key).get('url'):
                        print(key + '\t' + key2 + '\t' + key3)

reducer(mapper())
