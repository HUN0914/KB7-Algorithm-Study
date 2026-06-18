# 돌이 5만 개까지 있어서 직접 지우는 완전탐색으로는 구할 수 없다.

def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    
    # 정답은 1~distance 사이 -> 범위 설정
    left = 1
    right = distance
    
    while left <= right:
        mid = (left+right) // 2
        
        # 지운 돌의 개수
        remove = 0
        
        # 마지막으로 남긴 돌
        prev = 0
        
        for rock in rocks:
            if rock - prev < mid:
                remove += 1
            else:
                prev = rock
        
        # 도착지점과의 거리도 비교해야함
        if distance - prev < mid:
            remove += 1
        
        if remove <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer
