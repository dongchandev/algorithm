n=int(input())
cnt=0
a = 666

while True:
    if '666' in str(a):
        cnt+=1
    if cnt == n:
        break
    a+=1
print(a)