import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
pre = [0]
s = 0

for i in range(n):
  s += nums[i]
  pre.append(s)


for i in range(m):
  a, b = map(int, input().split())
  print(pre[b] - pre[a-1])