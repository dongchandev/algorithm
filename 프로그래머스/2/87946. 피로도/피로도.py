from itertools import permutations

def solution(k, dungeons):
    max_cnt = 0
    for p in permutations(dungeons):
        stemina = k
        term_cnt = 0
        for r,s in p:
            if stemina < r or stemina < s: break
            stemina -= s
            term_cnt += 1
        if max_cnt<term_cnt:
            max_cnt = term_cnt
    return max_cnt