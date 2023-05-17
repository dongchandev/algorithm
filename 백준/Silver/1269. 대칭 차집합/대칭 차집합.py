n,m=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(len(list(set(arr1)^set(arr2))))