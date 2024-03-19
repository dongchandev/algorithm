import math

n = int(input())

fn = math.factorial(n)
cnt = 0
fn_list=list(str(fn))
fn_list.reverse()
for i in fn_list:
    if i !='0':
        break
    cnt+=1
print(cnt)