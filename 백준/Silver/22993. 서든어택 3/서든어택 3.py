n=int(input())
power=list(map(int,input().split()))
junwon_power=power[0]
power = sorted(power[1:])
flag=0
for i in range(n-1):
    if junwon_power>power[i]:
        junwon_power+=power[i]
        continue
    else:
        flag=1
if flag==1:
    print("No")
if flag==0:
    print("Yes")