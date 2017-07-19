#!bin/user/python

import numpy
import sys

D = dict((dict()))
n = 0
# data = ("4 8", "1 2 6", "1 3 2", "1 4 10", "2 4 4", "3 1 5", "3 2 3", "3 4 8", "4 2 1", "1 4")
for line in sys.stdin:
# for line in data:
    line = line.strip().split(' ')
    if n == 0:
        nodes = int(line[0])
        connect = int(line[1])
        matrix = numpy.zeros((nodes, nodes), dtype=int)
    else:
        if n > connect:
            start = int(line[0]) - 1
            end = int(line[1]) - 1
            break
        matrix[int(line[1]) - 1][int(line[0]) - 1] = int(line[2])
    n += 1
print(matrix)
# print(start)
# print(end)
queue = list()
res = 0
while end not in queue:
    n = 0
    for i in range(nodes):
        if n == 0:
            n = matrix[i][start]
            tmp = i
        if n > matrix[i][start] and matrix[i][start] != 0 and i not in queue:
            n = matrix[i][start]
            tmp = i
    res += matrix[tmp][start]
    queue.append(start)
    start = tmp
    if start == end:
        break
    if len(queue) == nodes:
        print(-1)
        exit(0)
# print(queue)
print(res)




