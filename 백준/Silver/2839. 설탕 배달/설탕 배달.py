cnt=0
n=int(input())
while True:
    if n % 5 == 0:
        cnt += n // 5
        break
    n -= 3
    cnt+=1
    if n<=0:
        break
if n<0:
    print(-1)
else:
    print(cnt)