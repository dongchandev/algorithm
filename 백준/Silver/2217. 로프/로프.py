n=int(input())
arr=[]
for i in range(n):
    temp=int(input())
    arr.append(temp)
arr.sort(reverse=True)
result=[]
for i in range(n):
    result.append(arr[i]*(i+1))
print(max(result))