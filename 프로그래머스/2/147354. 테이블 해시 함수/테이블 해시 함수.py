def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col-1], -x[0]))
    s_list = []
    
    for i in range(row_begin - 1, row_end):
        t = 0
        for j in range(len(data[i])):
            t += data[i][j] % (i + 1) 
        s_list.append(t)
    
    answer = s_list[0]
    for i in range(1, len(s_list)):
        answer ^= s_list[i]
    
    return answer
