while True:
    s = input()
    if s == "0":
        break
    s_list=list(s)
    s_list.reverse()
    r_s=''.join(s_list)
    if s == r_s:
        print("yes")
    else:
        print("no")