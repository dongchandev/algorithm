def solution(s):
    answer = True
    stack = []
    for r in s:
        if r == '(':
            stack.append(r)
        elif r == ')': 
            if not stack: 
                return False
            stack.pop()  
    return len(stack) == 0 
