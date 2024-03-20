from collections import deque
import sys

queue = deque([])

t = int(input())

for i in range(t):
    x = sys.stdin.readline().rstrip().split()
    order = x[0]
    if order == 'push_front':
        queue.appendleft(x[1])

    elif order == 'push_back':
        queue.append(x[1])

    elif order=='pop_front':
        if len(queue)==0:
            print(-1)
            continue
        print(queue.popleft())

    elif order=='pop_back':
        if len(queue)==0:
            print(-1)
            continue
        print(queue.pop())

    elif order=='size':
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