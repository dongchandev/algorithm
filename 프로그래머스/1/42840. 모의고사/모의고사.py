def solution(answers):
    answer = []
    person = {
        1: [1,2,3,4,5],
        2: [2,1,2,3,2,4,2,5],
        3: [3,3,1,1,2,2,4,4,5,5]
    }
    score = {
        1: 0,
        2: 0,
        3: 0
    }
    for i in range(1,4):
        nums = person[i]
        person_nums = nums*(len(answers)//len(nums)) + nums[:(len(answers)%len(nums))]
        
        for a, pn in zip(answers, person_nums):
            if a == pn:
                score[i] += 1
    max_value = max(score.values())
    max_keys = [k for k, v in score.items() if v == max_value]
    return max_keys