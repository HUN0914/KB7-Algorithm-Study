def solution(n, cores):

    # 만약 n이 코어 개수 이하면 n번째 코어에서 마지막 작업을 진행
    if n <= len(cores):
        return n
    
    # 이분 탐색을 위한 left, right 잡기
    left = 0
    right = min(cores) * n # 가장 빠른 코어 하나만 일해도 n개의 작업을 처리할 수 있기 때문
    
    while left <= right:
        mid = (left + right) // 2
        
        # 0초에 모든 코어가 작업을 하나씩 받음
        count = len(cores)
        
        # mid초까지 코어가 추가로 받을 수 있는 작업 수
        for core in cores:
            count += mid // core
            
        if count >= n:
            time = mid
            right = mid - 1
        else:
            left = mid + 1
    
    # time - 1초 까지 진행한 작업 수
    count = len(cores)
    
    for core in cores:
            count += (time - 1) // core
    
    # time초에 비는 코어들을 탐색하며 count 늘리기
    for i in range(len(cores)):
        if time % cores[i] == 0:
            count += 1
            
            # 작업을 n개 했을 경우 i+1번째 코어에서 마지막 작업을 진행한 것임
            if count == n:
                return i + 1
