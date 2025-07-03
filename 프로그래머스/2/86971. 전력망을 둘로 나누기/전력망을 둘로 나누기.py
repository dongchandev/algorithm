from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    cnt = 1

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt

def solution(n, wires):
    answer = float('inf')
    for i in range(len(wires)):
        temp = wires[:i] + wires[i+1:]

        graph = [[] for _ in range(n+1)]
        for a, b in temp:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * (n+1)
        cnt = bfs(graph, 1, visited)
        diff = abs(cnt - (n - cnt))
        answer = min(answer, diff)

    return answer
