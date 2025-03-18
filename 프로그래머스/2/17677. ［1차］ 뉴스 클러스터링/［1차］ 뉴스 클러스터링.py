def solution(str1, str2):
    answer = []
    list_str1 = list()
    list_str2 = list()
    
    for i in range(len(str1)-1):
        new_str = str1[i]+str1[i+1]
        if new_str.isalpha():
            list_str1.append(new_str.lower())
    for i in range(len(str2)-1):
        new_str = str2[i]+str2[i+1]
        if new_str.isalpha():
            list_str2.append(new_str.lower())
    
    if (len(list_str1) == 0 and len(list_str2) == 0):
        return 65536
    
    for e in list_str1:
        if e in list_str2 : answer.append(e); list_str2.remove(e)
    list_str1.extend(list_str2)
    
    return int((len(answer)/len(list_str1)) * 65536)