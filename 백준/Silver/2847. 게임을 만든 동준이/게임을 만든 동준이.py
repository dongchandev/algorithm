n=int(input())
score=[ int(input()) for i in range(n)]
cnt = 0
for i in range(n-2, -1, -1):
    if score[i] >= score[i+1]:
        cnt += score[i] - score[i+1] + 1
        score[i] = score[i+1]-1
print(cnt)