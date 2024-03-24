import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
aSort = list(sorted(set(a)))
cnt = {aSort[i]: i for i in range(len(aSort))}
for i in a:
    print(cnt[i], end = ' ')