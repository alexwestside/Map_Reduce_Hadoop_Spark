#!bin/user/python

# import sys
#
# data = list()
# # D = {None, dict()}
# D = dict()
#
# n = 0
#
# data = input().split(' ')
# print(data)
# # matrix = list([data[1]][data[1]])
# for line in sys.stdin:
#     line = line.strip().split(' ')
#     if D.get(line[0]) is None:
#         D[line[0]] = list({line[1]: line[2]})
#     else:
#         D[line[0]].append({line[1]: line[2]})
#
#
# print(D)
# for line in sys.stdin:
#     line = line.strip().split(' ')



data = list()
# D = dict()
# D = {None: list(dict())}
D = dict((dict()))
n = 0
data = "4 8"
data2 = \
("1 2 6",
"1 3 2",
"1 4 10",
"2 4 4",
"3 1 5",
"3 2 3",
"3 4 8",
"4 2 1")

data = data.split(' ')
print(data)
for line in data2:
    line = line.split(' ')
    if D.get(line[0]) is None:
        D[line[0]] = dict()
        D.get(line[0])[line[1]] = line[2]
    else:
        D.get(line[0])[line[1]].append(line[2])
    if D.get(line[1]) is None:
        D[line[1]] = dict()
        D.get(line[1])[line[0]] = line[2]
