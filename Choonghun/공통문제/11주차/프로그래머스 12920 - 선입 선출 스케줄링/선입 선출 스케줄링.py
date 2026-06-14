def solution(n, cores):
    """
    이분 탐색?
    """
    l, r = 0, 10e9
    t = 0
    while l <= r: # t = 일을 모두 끝내는데 걸리는 시간 
        m = (l+r) // 2
        s = 0
        for c in cores:
            s += (m//c)+1
        if s >= n:
            r = m-1
            t = m
        else:
            l = m+1

    if t: # t > 0인 경우
        for c in cores: # 직전 시간까지 남은 일 개수 구하기
            n -= ((t-1)//c)+1

    for i in range(len(cores)): # 처음부터 하나씩 가능한 코어에 일을 배정하며 언제 끝나는지 확인하기
        if not t % cores[i]: # t % core[i]가 0이면 현재 일이 없다는 것이다.
            n -= 1
        if not n: # n이 0이 되었다는 것은 일을 모두 배정했다는 것 
            return i+1
    