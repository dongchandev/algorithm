n,m=map(int,input().split())
check=[]
s=[]
for i in range(n):
    temp=input()
    s.append(temp)
for i in range(m):
    temp=input()
    check.append(temp)
cnt=0
for i in range(m):
    if check[i] in s:
        cnt+=1
print(cnt)