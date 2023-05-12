n=int(input())
score=[]
for _ in range(n):
    arr=list(map(int,input().split()))
    m=0
    for i in range(5):
        for j in range(i+1,5):
            for k in range(j + 1, 5):
                if (arr[i]+arr[j]+arr[k])%10>=m:
                    m=(arr[i]+arr[j]+arr[k])%10
    score.append(m)
for i in range(n - 1, -1, -1):
  if score[i] == max(score):
    print(i + 1)
    break