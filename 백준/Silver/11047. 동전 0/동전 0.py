n, k = map(int, input().split())
l = [int(input()) for _ in range(n)]

l.sort(reverse=True)

count = 0
for i in l:
    if k >= i:
        count += k // i
        k %= i

print(count)