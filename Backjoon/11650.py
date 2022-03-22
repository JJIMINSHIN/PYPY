import sys

n = int(input()) #점 개수
li =[]

for i in range(n):
    li.append(list(map(int, input().split())))
li.sort(key = lambda x: (x[0], x[1]))

for i in range(n):
    print(li[i][0],li[i][1])