def solution(participant, completion):
    sum=0
    dic={}
    for part in participant:
        dic[hash(part)]=part
        sum+=hash(part)
    for part in completion:
        sum-=hash(part)
    
    return dic[sum]