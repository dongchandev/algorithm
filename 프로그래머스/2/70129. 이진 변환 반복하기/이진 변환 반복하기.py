def solution(s):
    answer = 0
    count = 0
    while s != '1':
        zero_count = s.count('0')
        s = s.replace('0', '') 
        s = str(bin(len(s)))[2:]
        answer += zero_count
        count += 1
    return [count, answer]

print(solution('110010101001'))
