import heapq
import sys

heap = []

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        try : print(heapq.heappop(heap))
        except IndexError : print(0)
        continue
    heapq.heappush(heap,x)