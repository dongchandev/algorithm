n = int(input())
l = input()
s=0
for i in range(len(l)):
    s+=(ord(l[i])-96)*(31**i)
print(s % 1234567891)
