def solution(distance, rocks, n):
    rocks.sort() # 오름차순 정렬
    l,r = 1, distance # 이분 탐색
    rocks.append(r) # 도착지점을 바위에 포함
    numR = len(rocks) # 바위의 개수
    answer = 0
    
    def getRemovedRocks(gap):
        last = 0 # 직전 바위
        removed = 0 # 제거된 바위의 개수
        for i in range(0, numR):
            if rocks[i] - last < gap: # 이전 바위와 현재 바위의 간격이 gap보다 작다면 현재 바위를 제거 대상에 추가
                removed += 1
            else: # 아니라면 이전 바위를 현재 바위로 갱신
                last = rocks[i] 
        return removed
    
    while l <= r:
        m = (l+r) // 2
        removed = getRemovedRocks(m) # 간격 m을 최소로 두고 제거된 바위의 개수를 구해서
        if removed > n: # 제거된 바위의 개수가 n보다 크면
            r = m-1 # r을 m-1로 변경후 루프
        else: # n보다 작거나 같으면
            answer = m # 답을 m으로 갱신하고
            l = m+1 # l을 m+1로 바꾸어 루프 => m을 계속 증가시켜서 최소 간격중 최댓값을 구하기 위함
        
    return answer