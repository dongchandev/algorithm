def solution(priorities, location):
    answer = 0
    
    priorities = [[i,p] for i,p in enumerate(priorities)]
    
    while priorities:
        now = priorities.pop(0)
        if any(p[1] > now[1] for p in priorities):
            priorities.append(now)
        else:
            if now[0] == location: 
                return answer+1
            answer+=1
    return -1

