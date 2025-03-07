from collections import deque

def solution(operations):
    answer = []
    q = deque([])
    for oper in operations:
        o,n = oper.split(' ')
        n = int(n)
        if o == 'I':
            q.append(n)
        elif o == 'D':
            if len(q)==0:
                continue
            elif n == 1:
                q.remove(max(q))
            elif n == -1:
                q.remove(min(q))
    if len(q) == 0:
        return [0,0]
    return [max(q), min(q)]