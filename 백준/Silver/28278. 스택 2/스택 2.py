import sys

stack=[]
n = int(sys.stdin.readline())
for _ in range(n):
    order=list(map(int,sys.stdin.readline().split(' ')))
    match order[0]:
        case 1:
            stack.append(order[1])
        case 2:
            if len(stack)>0: 
                print(stack.pop())
            else: 
                print(-1)
        case 3:
            print(len(stack))
        case 4:
            if len(stack)==0:
                print(1)
            else:
                print(0)
        case 5:
            if len(stack)>0: 
                print(stack[len(stack)-1])
            else:
                print(-1)
        case _:
            pass