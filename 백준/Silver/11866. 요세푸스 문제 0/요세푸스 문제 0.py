from collections import deque

n,k=map(int,input().split())

people = deque(range(1, n+1))
result = []

while people:
    for _ in range(k-1):
        people.append(people.popleft())
    result.append(people.popleft())

print("<"+", ".join(map(str,result))+">")