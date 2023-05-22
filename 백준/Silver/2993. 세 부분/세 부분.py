import sys
word = sys.stdin.readline().rstrip()
 
lst = []
for i in range(len(word)-2):
    for j in range((i+1), len(word)-1):
        for k in range((j+1), len(word)):
            if len(word) == len(word[i:j] + word[j:k] + word[k:]):
                a = word[i:j]
                b = word[j:k]
                c = word[k:]
                lst.append([a[::-1]+b[::-1]+c[::-1]])
lst.sort()
print(''.join(lst[0]))
