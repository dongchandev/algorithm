def solution(s):
    answer = True
    stack = []
    for i in s:
        if len(stack)!= 0 and '(' != stack[-1:] and i==')':
            stack.pop()
        else:
            stack.append(i)
    print(stack)
    return len(stack) == 0