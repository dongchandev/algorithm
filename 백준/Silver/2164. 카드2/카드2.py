import sys
from collections import deque

t = int(sys.stdin.readline())
queue = deque([i for i in range(1,t+1)])

while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])