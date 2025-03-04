def solution(clothes):
    clothes_dir={}
    for clothe in clothes:
        if clothe[-1] in clothes_dir:
            clothes_dir[clothe[-1]] += 1
        else:
            clothes_dir[clothe[-1]] = 1
    answer = 1
    for _, value in clothes_dir.items():
        answer *= value + 1
        
    return answer -1