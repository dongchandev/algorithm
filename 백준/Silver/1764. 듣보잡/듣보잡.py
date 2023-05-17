import sys

def input():
    return sys.stdin.readline().rstrip()


n, m = map(int, input().split())
no_hear=[]
no_look=[]
for _ in range(n):
    temp=input()
    no_hear.append(temp)
for _ in range(m):
    temp=input()
    no_look.append(temp)
no_hear_look=list(set(no_hear)&set(no_look))
no_hear_look.sort()
print(len(no_hear_look))
for i in no_hear_look:
    print(i)