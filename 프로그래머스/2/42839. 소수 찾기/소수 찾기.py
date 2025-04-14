import itertools

def solution(numbers):
    number_chars = list(numbers)
    unique_numbers = set()
    
    for length in range(1, len(numbers) + 1):
        for perm in itertools.permutations(number_chars, length):
            unique_numbers.add(int(''.join(perm)))
    
    answer = 0
    for num in unique_numbers:
        if check_prime(num):
            answer += 1
            
    return answer

def check_prime(n):
    if n <= 1: return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True