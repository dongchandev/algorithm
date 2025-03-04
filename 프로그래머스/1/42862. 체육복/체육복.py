def solution(n, lost, reserve):
    
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
    for student in sorted(reserve_set):  
        if student - 1 in lost_set:  
            lost_set.remove(student - 1)
        elif student + 1 in lost_set:
            lost_set.remove(student + 1)

    return n - len(lost_set)