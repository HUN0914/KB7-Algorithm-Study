def solution(n, lost, reserve):
    answer = 0
    
    # 체육복 현황
    students = [1] * (n+1)
    students[0] = 0
    
    # 도난 당하기
    for i in lost:
        students[i] -= 1
    
    # 여벌 옷 준비하기
    for i in reserve:
        students[i] += 1
        
    for i in range(1, n+1):
        # 0이면 전후로 2가 있는지 확인 후, 전에 있는 거부터 빌리기
        if students[i] == 0:
            if students[i-1] == 2:
                students[i], students[i-1] = 1, 1
            elif i < n and students[i+1] == 2:
                students[i], students[i+1] = 1, 1
    
    for i in students:
        if i == 1 or i == 2:
            answer += 1
    
    return answer