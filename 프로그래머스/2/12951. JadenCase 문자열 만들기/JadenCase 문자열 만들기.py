def solution(s):
    answer = ''
    s_l = s.split(' ')
    for word in s_l:
        answer += word[:1].upper() + word[1:].lower() + ' '
    return answer[:-1]
