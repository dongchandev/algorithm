from collections import deque
import sys

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = [0] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited)
        count += 1

print(count)