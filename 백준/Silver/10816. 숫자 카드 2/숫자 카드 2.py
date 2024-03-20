import sys
import bisect

n=int(input())
card = list(map(int, sys.stdin.readline().rstrip().split()))
m=int(input())
test = list(map(int, sys.stdin.readline().rstrip().split()))

card.sort()


for i in test:
    l=bisect.bisect_left(card,i)
    r=bisect.bisect_right(card,i)
    print(r-l, end=' ')