from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n  
    
    for i in range(n):
        if not visited[i]:
            q = deque([i])
            while q:
                node = q.popleft()
                visited[node] = True
                for j in range(n):
                    if computers[node][j] == 1 and not visited[j]:
                        visited[j] = True
                        q.append(j)
            answer += 1 

    return answer
