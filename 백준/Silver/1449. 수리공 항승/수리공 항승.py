n,l=map(int,input().split())
data=list(map(int,input().split()))
data.sort()
first=data[0]
cnt=1
for i in data[1:]:
    if i in range(first,first+l):
        continue
    else:
        cnt+=1
        first=i
print(cnt)