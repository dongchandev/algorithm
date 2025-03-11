def solution(k, tangerine):
    dict = {}
    for t in tangerine:
        if t in dict:
            dict[t] += 1
        else:
            dict[t] = 1
    tangerine.sort(key = lambda x: (-dict[x] , x))
    return len(set(tangerine[:k]))