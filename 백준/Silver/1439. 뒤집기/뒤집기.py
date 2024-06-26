s = input()

new_s = ''
before = s[0]
cnt = 0
for i in range(1,len(s)):
    if before != s[i]:
        if s[0] != s[i]:
            cnt += 1
        before = s[i]
    else: 
        continue
print(cnt)