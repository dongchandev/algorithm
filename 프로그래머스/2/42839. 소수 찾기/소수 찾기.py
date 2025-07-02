import math
from itertools import permutations

def get_all_numbers(s):
    result = set()
    for r in range(1, len(s) + 1):
        for p in permutations(s, r):
            num = int(''.join(p))
            result.add(num)
    return result

def is_prime_number(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
    
def solution(numbers):
    cnt = 0
    nums = get_all_numbers(numbers)
    print(nums)
    for n in nums:
        if is_prime_number(n):
            print(n)
            cnt+=1
    
    return cnt