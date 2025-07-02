def solution(answers):
    answer = []
    answer_len = len(answers) 

    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]

    a1 = p1 * (answer_len // len(p1))+ p1[0:answer_len%len(p1)]
    a2 = p2 * (answer_len // len(p2))+ p2[0:answer_len%len(p2)]
    a3 = p3 * (answer_len // len(p3))+ p3[0:answer_len%len(p3)]
    
    c1,c2,c3 = 0,0,0
    
    for i in range(answer_len):
        if answers[i] == a1[i]:
            c1 += 1
        if answers[i] == a2[i]:
            c2 += 1
        if answers[i] == a3[i]:
            c3 += 1
    max_score = max(c1,c2,c3)
    
    if max_score == c1:
        answer.append(1)
    if max_score == c2:
        answer.append(2)
    if max_score == c3:
        answer.append(3)
    return answer