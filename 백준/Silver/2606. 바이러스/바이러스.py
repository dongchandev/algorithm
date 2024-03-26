from collections import deque

n=int(input())
v=int(input())
graph = [[] for i in range(n+1)]
visited=[0]*(n+1)
for i in range(v):
    a,b=map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]
visited[1]=1
queue=deque([1])

while queue:
    v=queue.popleft()
    for i in graph[v]:
        if not (visited[i]):
            queue.append(i)
            visited[i]=1
print(visited.count(1)-1)