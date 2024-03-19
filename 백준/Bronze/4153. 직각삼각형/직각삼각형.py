while True:
    l = list(map(int,input().split()))
    if sum(l)==0:
        break

    l.sort()

    if (l[-1])**2 == (l[-2])**2+(l[-3])**2:
        print("right")
    else:
        print("wrong")