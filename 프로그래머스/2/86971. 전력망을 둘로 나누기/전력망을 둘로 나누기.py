from collections import deque
import sys

def solution(n, wires):
    answer = sys.maxsize
    for i in range(len(wires)):
        graph = {i: [] for i in range(1, n + 1)}
        
        for j, (v1, v2) in enumerate(wires):
            if i == j: 
                continue
            graph[v1].append(v2)
            graph[v2].append(v1)
        
        visited = [False] * (n + 1) 
        count_1 = bfs(1, graph, visited) 
        count_2 = n - count_1  
        
        answer = min(answer, abs(count_1 - count_2)) 
        
    return answer

def bfs(start_node, graph, visited):
    queue = deque([start_node])
    count = 0
    visited[start_node] = True

    while queue:
        curr_node = queue.popleft()
        count += 1

        for next_node in graph[curr_node]:
            if not visited[next_node]: 
                visited[next_node] = True
                queue.append(next_node)
    return count
