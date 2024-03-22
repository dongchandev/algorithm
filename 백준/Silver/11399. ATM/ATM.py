import sys

n = int(input())
people = list(map(int, sys.stdin.readline().split()))

people.sort()
s=0
for x in range(1, n+1):
    s += sum(people[0:x])
print(s)