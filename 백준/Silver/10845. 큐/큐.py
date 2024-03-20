from collections import deque
import sys

t = int(input())
queue = deque([])

for _ in range(t):
    x = sys.stdin.readline().rstrip().split()
    order = x[0]

    if order == 'push':
        queue.append(int(x[1]))
    elif order == 'pop':
        if len(queue)==0:
            print(-1)
            continue
        print(queue.popleft())
    elif order == 'size':
        print(len(queue))
    elif order=='empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif order=='front':
        if len(queue)==0:
            print(-1)
            continue
        print(queue[0])
    elif order=='back':
        if len(queue)==0:
            print(-1)
            continue
        print(queue[-1])