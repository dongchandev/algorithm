import sys
from collections import deque

def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)

    dq = deque(B)
    cnt = 0
    for i in range(len(A)):
        if A[i] >= dq[0]:
            dq.pop()
        else:
            dq.popleft()
            cnt += 1
    return cnt