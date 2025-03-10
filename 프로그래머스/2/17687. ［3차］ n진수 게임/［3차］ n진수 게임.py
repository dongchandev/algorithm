def solution(n, t, m, p):
    answer = ''
    num = 0
    sequence = ''
    
    while len(sequence) < m * t:
        sequence += convert(n, num)
        num += 1
        
    for i in range(p - 1, m * t, m):
        answer += sequence[i]

    return answer

def convert(n, number):
    digits = "0123456789ABCDEF"
    if number == 0:
        return "0"

    result = ""
    while number > 0:
        result = digits[number % n] + result
        number //= n

    return result