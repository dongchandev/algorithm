def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = list()
        for l in leaves:
            tmp.append(l+num)
            tmp.append(l-num)
        leaves=tmp
    for l in leaves:
        if l == target:
            answer += 1
    return answer