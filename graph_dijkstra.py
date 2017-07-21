#!bin/user/python

import numpy
import heapq
import sys

# D = dict()
# L = []
# n = 0
# i = 0
# j = 0

# data = ('3 3', 'a b 3', 'b c 2', 'c d 1', 'a b')
# # for line in sys.stdin:
# for line in data:
#     line = line.strip().split(' ')
#     if n == 0:
#         nodes = int(line[0])
#         connect = int(line[1])
#         matrix = numpy.zeros((nodes, nodes), dtype=int)
#     else:
#         if n > connect:
#             start = line[0]
#             end = line[1]
#             break
#         else:
#             if line[0] not in D:
#                 D[line[0]] = i
#
#     n+=1


# data = ("4 8", "a 2 6", "a 3 2", "a 4 10", "2 4 4", "3 a 5", "3 2 3", "3 4 8", "4 2 1", "a 4")
# data = ('6 8', '1 2 4', '1 3 5', '1 4 8', '2 3 6', '3 4 7', '3 2 5', '4 3 1', '5 6 1', '1 6')
# data = ('5 0', '1 5')
# data = ('4 2', '1 2 10', '3 4 11', '1 4')
# for line in sys.stdin:
# # for line in data:
#     line = line.strip().split(' ')
#     if n == 0:
#         nodes = int(line[0])
#         connect = int(line[1])
#         matrix = numpy.zeros((nodes, nodes), dtype=int)
#     else:
#         if n > connect:
#             start = int(line[0]) - 1
#             end = int(line[1]) - 1
#             break
#         matrix[int(line[1]) - 1][int(line[0]) - 1] = int(line[2])
#     n += 1
# # print(matrix)
# # print(start)
# # print(end)
# queue = list()
# res = 0
# while end not in queue:
#     n = 0
#     for i in range(nodes):
#         if n == 0:
#             n = matrix[i][start]
#             tmp = i
#         if n > matrix[i][start] and matrix[i][start] != 0 and i not in queue:
#             n = matrix[i][start]
#             tmp = i
#     if n == 0:
#        # print(-1)
#        sys.stdout.write(str(-1))
#        exit(0)
#     res += matrix[tmp][start]
#     queue.append(start)
#     start = tmp
#     if start == end:
#         break
#     if len(queue) == nodes:
#         # print(-1)
#         sys.stdout.write(str(-1))
#         exit(0)
# # print(queue)
# # print(res)
# sys.stdout.write(str(res))


# n = 0
# i = -1
# j = 0
# x = 0
# D = dict()
# data = ('4 3', 'a b 3', 'b c 2', 'c d 1', 'a d')
# # data = ("4 8", "1 2 6", "1 3 2", "1 4 10", "2 4 4", "3 1 5", "3 2 3", "3 4 8", "4 2 1", "1 4")
# for line in data:
#     line = line.strip().split(' ')
#     if n == 0:
#         room = int(line[0])
#         connect = int(line[1])
#         matrix = numpy.zeros((room, room), dtype=int)
#         # print (matrix)
#     else:
#         if n > connect:
#             start = line[0]
#             end = line[1]
#             print (start)
#             print (end)
#         else:
#             if line[0] not in D:
#                 i+=1
#                 D[line[0]] = i
#                 j+=1
#             else:
#                 i = D.get(line[0])
#                 j += 1
#             if line[1] not in D:
#                 D[line[1]] = j
#             else:
#                 j = D.get(line[1])
#             matrix[j][i] = int(line[2])
#     n+=1
# print(D)
# print (matrix)
#
#
#

n = 0
Q = []
V = []
stack = []
L1 = []
L = []
tmp = 0
res = 0
data = ('5 10', '1 2 10', '1 3 5', '2 3 2', '2 4 1', '3 2 3', '3 4 9', '3 5 2', '4 5 4', '5 1 7', '5 4 6', '1 4')
for line in data:
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
        if int(line[0]) - 1 not in stack:
            stack.append(int(line[0]) - 1)
        if int(line[1]) - 1 not in stack:
            stack.append(int(line[1]) - 1)
    n += 1
print(matrix)
print(start)
print(end)
print(stack)
V.append(start)
while len(V) != 0:
    if len(Q) == 0 or Q[0] not in V:
        for i in range(0, nodes):
            if matrix[i][start] != 0:
                Q = list(str(i)) + Q
        if Q[0] not in V:
            V.append(Q[0])
            tmp += matrix[int(Q[0])][start]
            if str(end) in V:
                if res == 0 or res > tmp:
                    res = tmp
                    V = V[:len(V) - 1]
                    Q = Q[1:]
        else:
            V = V[:len(V) - 1]
        start = int(Q[0])
        Q = Q[1:]
    else:
        Q = Q[1:]
        start = int(Q[0])



