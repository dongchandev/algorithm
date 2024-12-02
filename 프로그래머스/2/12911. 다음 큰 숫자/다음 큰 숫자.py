def solution(n):
    binary_n = bin(n)[2:]
    while True:
        n+=1
        next_binary_n = bin(n)[2:]
        if (next_binary_n.count('1') == binary_n.count('1')):
            break            
    return n