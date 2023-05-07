n=int(input())
stack=[]
for i in range(n):
    temp=int(input())
    if temp==0:
        del stack[-1]
    else:
        stack.append(temp)
print(sum(stack))