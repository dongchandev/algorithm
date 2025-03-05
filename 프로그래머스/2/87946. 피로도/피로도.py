from itertools import permutations

def solution(k, dungeons):
    max_dungeons = 0
    
    for perm in permutations(dungeons, len(dungeons)):  # 모든 순열 탐색
        fatigue = k
        count = 0
        
        for min_fatigue, consume_fatigue in perm:
            if fatigue >= min_fatigue:
                fatigue -= consume_fatigue
                count += 1
            else:
                break
        
        max_dungeons = max(max_dungeons, count)
    
    return max_dungeons
