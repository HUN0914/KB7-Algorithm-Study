def solution(key, lock):
    n = len(lock)
    m = len(key)
    data = [[-1 for _ in range(2*m+n)] for __ in range(2*m+n)] # 열쇠가 아예 자물쇠 범위 바깥에 있는것도 고려해서 2*m+n 크기의 2차원 배열 선언
    for i in range(m,n+m): # 자물쇠 위치 넣기 (m,m) ~ (n+m, n+m)
        for j in range(m,n+m):
            data[i][j] = lock[i-m][j-m]
    
    key1 = key # 기존 키
    key2 = [[key[i][j] for i in range(m-1,-1,-1)] for j in range(m)] # 시계방향으로 90도 회전
    key3 = [[key[i][j] for j in range(m-1,-1,-1)] for i in range(m-1,-1,-1)] # 시계 방향으로 180도 회전
    key4 = [[key[i][j] for i in range(m)] for j in range(m-1,-1,-1)] # 시계 방향으로 270도 회전
    
    def checkAnswer(x,y,w,s): # 열쇠가 맞는지 체크
        for i in range(m,n+m):
            for j in range(m, n+m):
                check = data[i][j] # 자물쇠에 대해서
                if s == 0 and x <= i < x+w and y <= j < y+w: # 키가 자물쇠 범위 안에 있으면 합산해보기
                    check += key1[i-x][j-y]
                elif s == 1 and x <= i < x+w and y <= j < y+w:
                    check += key2[i-x][j-y]
                elif s == 2 and x <= i < x+w and y <= j < y+w:
                    check += key3[i-x][j-y]
                elif s == 3 and x <= i < x+w and y <= j < y+w:
                    check += key4[i-x][j-y]  
                if check != 1: # 만약 check가 1이 아니라면 맞지 않는 것이므로 False 반환
                    return False
        return True # 아무 이상 없었다면 True 반환
                    
    
    for i in range(0, m+n): # 키는 0부터 m+n-1 까지 기준 위치를 이동 가능
        for j in range(0, m+n): 
            for k in range(4): # 4가지 회전에 대해서
                if checkAnswer(i,j,m,k): # 맞물리는지 체크
                    return True # 맞물리면 True
                
    return False # 끝까지 안 맞물리면 False