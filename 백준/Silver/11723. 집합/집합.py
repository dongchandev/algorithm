import sys

s = [0 for _ in range (21)]
t = int(input())
for i in range(t):
    x = sys.stdin.readline().rstrip().split()
    order = x[0]

    if order == 'add':
        s[int(x[1])] = 1
    elif order == 'remove':
        s[int(x[1])] = 0
    elif order == 'check':
        print(s[int(x[1])])
    elif order == 'toggle':
        if s[int(x[1])]==0:
            s[int(x[1])]=1
        else:
            s[int(x[1])]=0
    elif order=='all':
        s=[1 for i in range(21)]
    elif order=='empty':
        s = [0 for _ in range(21)]