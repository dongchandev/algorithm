import sys
from collections import deque

n,k = map(int,sys.stdin.readline().rstrip().split())
queue=deque([])
visited=[0]*(100000+1)
queue.append(n)
while True:
    x=queue.popleft()
    if x==k:
        print(visited[x])
        break
    for i in (x-1,x+1,x*2):
        if 0<=i<=100000 and not visited[i]:
            visited[i]=visited[x]+1
            queue.append(i)