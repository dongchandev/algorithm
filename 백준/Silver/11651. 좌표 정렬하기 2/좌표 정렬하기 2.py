import sys

input = sys.stdin.readline
n = int(input())
l=[]
for i in range(n):
    x, y = map(int,input().split())
    l.append((x,y))
l.sort(key = lambda p:(p[1],p[0]))
for i in range(n):
    print(l[i][0],l[i][1])