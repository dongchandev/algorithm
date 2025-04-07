import heapq 

def solution(n, k, enemy):
    answer = 0
    invinc = [0]*k

    for i in range(len(enemy)):
        if enemy[i] > invinc[0]:
            n -= heapq.heapreplace(invinc,enemy[i])
        else:
            n -= enemy[i]
        if n < 0:
            return i
    return len(enemy)

