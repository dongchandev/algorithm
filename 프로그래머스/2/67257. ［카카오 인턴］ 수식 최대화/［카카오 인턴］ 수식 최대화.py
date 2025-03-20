import itertools
from collections import deque

def cal(after_operation, op):
    b = after_operation.pop()
    a = after_operation.pop()
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    else:
        return a * b

def solution(expression: str):
    stk = []
    answer_list = []
    for rank in itertools.permutations(["*", "+", "-"], 3):
        num = ""

        after_operation = []

        que = deque(expression)

        while len(que) != 0:
            s = que.popleft()
            if s not in rank:
                num += s
                continue

            after_operation.append(int(num))
            num = ""

            while len(stk) != 0 and rank.index(stk[-1]) <= rank.index(s):
                after_operation.append(cal(after_operation, stk.pop()))

            stk.append(s)

        after_operation.append(int(num))

        while len(stk) != 0:
            after_operation.append(cal(after_operation, stk.pop()))

        answer_list.append(abs(after_operation[0]))

    answer_list.sort()
    return answer_list[-1]