N = int(input())
l = []
for _ in range(N):
    l.append(int(input()))

l.sort(reverse=True)

res = 0
i = 0
while i < len(l):
    if i < len(l) - 1 and l[i] > 1 and l[i + 1] > 1:
        res += l[i] * l[i + 1]
        i += 2
    elif l[i] == 1: 
        res += l[i]
        i += 1
    else:
        break 

j = len(l) - 1
while j >= i:
    if j > i and l[j] <= 0 and l[j - 1] <= 0:
        res += l[j] * l[j - 1]
        j -= 2
    else:
        res += l[j]
        j -= 1

print(res)
