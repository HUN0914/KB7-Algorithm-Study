def solution(routes):
    answer = 1
    routes.sort()
    l,r = routes[0]
    # print(routes)
    for i in range(1, len(routes)):
        if r < routes[i][0]: # 다음 차량의 진입 시점의 현재 카메라의 구간보다 나중이면 카메라를 하나 추가
            answer += 1
            l,r = routes[i]
            continue
        if l <= routes[i][0] <= r: # 다음 차량의 진입 시점이 현재 카메라의 구간 안에 있으면 갱신
            l = routes[i][0]
        if l <= routes[i][1] <= r: # 다음 차량의 진출 시점이 현재 카메라의 구간 안에 있으면 갱신
            r = routes[i][1]
    # print(l,r)    
    return answer