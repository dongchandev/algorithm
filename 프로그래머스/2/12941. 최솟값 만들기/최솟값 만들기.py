def solution(A,B):
    A.sort(reverse = True)
    B.sort()
    answer=0
    for i,j in zip(A,B):
        answer+=(i*j)
    return answer