def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])

    cnt = 0
    camera_position = -30001  

    for route in routes:
        if camera_position < route[0]:
            cnt += 1
            camera_position = route[1] 

    return cnt
