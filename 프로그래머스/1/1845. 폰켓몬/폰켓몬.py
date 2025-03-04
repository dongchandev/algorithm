def solution(nums):
    n = len(nums)//2
    nums_set_length = (len(set(nums)))
    if (nums_set_length < n):
        return nums_set_length
    return n