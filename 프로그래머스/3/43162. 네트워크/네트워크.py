from collections import deque

def solution(n, computers):
    def bfs(start, computers, visited):
        queue = deque([start])
        visited[start] = True
        while queue:
            current = queue.popleft()
            for i in range(n):
                if not visited[i] and computers[current][i] == 1:
                    visited[i] = True
                    queue.append(i)
                    
    visited = [False] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            bfs(i, computers, visited)
            answer += 1
    return answer