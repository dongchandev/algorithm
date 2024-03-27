import sys
from collections import deque

m,n = map(int,sys.stdin.readline().rstrip().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
l = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

queue = deque([])
for i in range(n):
    for j in range(m):
        if l[i][j] == 1:
            queue.append([i, j])
cnt =0
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and l[nx][ny] == 0:
            l[nx][ny] = l[x][y] + 1
            queue.append([nx, ny])
for i in l:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    cnt = max(cnt, max(i))
print(cnt - 1)