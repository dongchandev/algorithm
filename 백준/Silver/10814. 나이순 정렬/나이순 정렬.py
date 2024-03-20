n = int(input())
member_lst = []

for _ in range(n):
    a, n = map(str, input().split())
    a = int(a)
    member_lst.append((a, n))

member_lst.sort(key = lambda x : x[0])

for i in member_lst:
    print(i[0], i[1])