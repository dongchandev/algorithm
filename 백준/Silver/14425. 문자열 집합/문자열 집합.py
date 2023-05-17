import sys

n,m=map(int,input().split())
check=[]
s=[]
for i in range(n):
    temp=sys.stdin.readline().split()
    s.append(temp)
for i in range(m):
    temp=sys.stdin.readline().split()
    check.append(temp)
cnt=0
for i in range(m):
    if check[i] in s:
        cnt+=1
print(cnt)
