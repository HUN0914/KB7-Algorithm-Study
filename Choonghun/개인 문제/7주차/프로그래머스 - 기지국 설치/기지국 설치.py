def solution(n, stations, w):
    answer = 0
    station = []
    for mid in stations:
        l,r = mid-w, mid+w
        if l <= 0:
            l = 1
        station.append([l,r])
    station.sort()
    ran = 2*w+1
    l,r = 0,0
    answer = 0
    for x,y in station:
        if r >= x:
            r = y
        elif r < x:
            gap = x-r-1
            if gap % ran:
                answer += gap//ran + 1
            else:
                answer += gap//ran
            l, r = x,y
    gap = n-r
    if gap > 0:
        if gap % ran:
            answer += gap//ran + 1
        else:
            answer += gap//ran
    # 투포인터

    return answer