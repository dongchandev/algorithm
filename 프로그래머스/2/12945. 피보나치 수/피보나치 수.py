def solution(n):
    b, a, s = 0, 1, 0
    for i in range(n-1):
        s = b + a
        b = a
        a = s

    return s % 1234567