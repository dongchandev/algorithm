from collections import deque
import sys

n = int(input())
queue = deque([])
for _ in range(n):
    o=sys.stdin.readline().rstrip()
    order = o.split(' ')
    match order[0]:
        case 'push':
            queue.append(int(order[1]))
        case 'pop':
            if len(queue)>0:
                print(queue.popleft())
            else:
                print(-1)
        case 'size':
            print(len(queue))
        case 'empty':
            if len(queue)>0:
                print(0)
            else:
                print(1)
        case 'front':
            if len(queue)==0:
                print(-1)
            else:
                print(queue[0])
        case 'back':
            if len(queue)==0:
                print(-1)
            else:
                print(queue[len(queue)-1])