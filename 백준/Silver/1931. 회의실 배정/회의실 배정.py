n = int(input())

l=[]

ep=0
answer=0

for i in range(n):
    s,e = map(int,input().split())
    l.append([s,e])
l.sort(key=lambda x: (x[1], x[0]))

for s,e in l:
    if s>=ep:
        answer+=1
        ep=e
print(answer)