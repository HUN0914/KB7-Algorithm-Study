from collections import deque
ind = 0 # 현재 발견된 유전 개수
def solution(land):
    answer = 0
    n,m = len(land),len(land[0])
    data = [0] # 유전 크기 정보
    check = [[0 for _ in range(m)] for __ in range(n)] # 유전 체크
    
    def bfs(x,y):
        global ind 
        if check[x][y]: # 이미 발견된 유전이면 그대로 크기 정보 return
            return data[check[x][y]]
        que = deque([(x,y)])
        ind += 1
        check[x][y] = ind
        res = 1
        while len(que) > 0: # BFS 진행
            x,y = que.popleft()
            for i,j in [(-1,0),(1,0),(0,1),(0,-1)]:
                nx, ny = x+i, y+j
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] and not check[nx][ny]:
                    check[nx][ny] = ind # 유전 번호 체크
                    que.append((nx,ny))
                    res += 1
        data.append(res) # 유전 크기 정보 저장
        return data[ind] # 크기 정보 반환
                
    for j in range(m):
        res = 0
        colCheck = []
        for i in range(n):
            if check[i][j] != 0 and check[i][j] in colCheck: # 이미 발견됐는데, 시추를 이미 한 곳이면 스킵
                continue
            if land[i][j]: # 유전 발견시 bfs 진행
                res += bfs(i,j)
                colCheck.append(check[i][j]) # 발견된 유전을 삽입
        answer = max(answer, res) # 최댓값 갱신

    return answer