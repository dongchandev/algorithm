import sys
import statistics

input = sys.stdin.readline
n = int(input())

l=[]
for i in range(n):
    l.append(int(input()))

print(round(statistics.mean(l)))
print(statistics.median(l))
a = statistics.multimode(l)
a.sort()
m = a[1] if len(a) > 1 else a[0]
print(m)
print(max(l)-min(l))
