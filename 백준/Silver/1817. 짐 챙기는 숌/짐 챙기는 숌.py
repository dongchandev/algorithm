n,m=map(int,input().split())
if n!=0:
    data=list(map(int,input().split()))
    box=1
    weight=0
    for i in range(n):
        weight += data[i]
        if weight > m :
            box += 1
            weight = data[i]
    print(box)
else:
    print(0)