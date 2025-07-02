def solution(sizes):
    #항상 가로가 더 크도록 구성할 것.
    width=0
    height=0
    answer = 0
    for w,h in sizes:
        if w<h:
            w,h=h,w
        width = max(width,w)
        height = max(height,h)
    return width*height