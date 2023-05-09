a,b=map(int,input().split())
la,lb=a,b
while b:
    a,b=b,a%b
    gcd=a
    lcm=la*lb//gcd
print(lcm)