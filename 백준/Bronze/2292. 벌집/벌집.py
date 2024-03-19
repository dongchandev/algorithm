n = int(input())

s = 1 
cnt = 1
while n > s :
    s += 6 * cnt  
    cnt += 1  
print(cnt)