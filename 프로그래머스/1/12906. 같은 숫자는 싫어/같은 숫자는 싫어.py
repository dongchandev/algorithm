def solution(arr):
    answer = []
    answer.append(arr.pop(0))
    for a in arr:
        if answer[-1] == a:
            continue
        answer.append(a)
    return answer