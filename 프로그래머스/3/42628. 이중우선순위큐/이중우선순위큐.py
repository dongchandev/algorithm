from collections import deque

def solution(operations):
    q = deque([])
    for i in operations:
        oper, num = i.split(' ')
        if oper == 'I':
            q.append(int(num))
        elif oper == 'D':
            if len(q)==0:
                continue
            elif num == '1':
                q.remove(max(q))
            elif num == '-1':
                q.remove(min(q))
    if len(q) == 0:
        return [0,0]
    else:
        return [max(q), min(q)]
    