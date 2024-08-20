stack = []
n = int(input())
seq = [int(input()) for _ in range(n)]
result = []
cnt = 1
possible = True

for num in seq:
    while cnt <= num: 
        stack.append(cnt)
        result.append('+')
        cnt += 1
    
    if stack[-1] == num: 
        stack.pop()
        result.append('-')
    else: 
        print("NO")
        possible = False
        break
if(possible==True):     
    print('\n'.join(result))