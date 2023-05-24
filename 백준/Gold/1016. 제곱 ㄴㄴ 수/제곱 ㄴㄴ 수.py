min,max=map(int,input().split())
answer = max-min+1
check = [False]*(max-min+1)
i=2
while i*i <= max:
    n=i**2
    remain = 0 if min%n==0 else 1
    mul=min//n + remain
    while n*mul<=max:
        if not check[n*mul-min]:
                check[n*mul-min]=True
                answer-=1
        mul+=1
    i+=1
print(answer)