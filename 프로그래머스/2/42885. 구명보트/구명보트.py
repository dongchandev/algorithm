def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    for i in people:
        total = i
        if total + people[-1] <= limit : 
            people.pop()
        answer += 1
            
    return answer