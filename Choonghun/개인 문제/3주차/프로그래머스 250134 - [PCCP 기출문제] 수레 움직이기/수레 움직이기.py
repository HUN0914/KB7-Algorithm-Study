from collections import deque
answer = 10e9
def solution(maze):
    n = len(maze)
    m = len(maze[0])
    rx,ry,bx,by = 0,0,0,0
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1: # 빨간 수레 최초 위치
                rx,ry = i, j
            elif maze[i][j] == 2: # 파란 수레 최초 위치
                bx,by = i, j
    
    redCheck = [[0 for _ in range(m)] for __ in range(n)] # 빨간 수레 방문 처리
    redCheck[rx][ry] = 1
    blueCheck = [[0 for _ in range(m)] for __ in range(n)] # 파란 수레 방문 처리
    blueCheck[bx][by] = 1
    
    def printBoard(rx,ry,bx,by): # 디버깅용 메서드
        for i in range(n):
            temp = [1 if (i,j)==(rx,ry) else 2 if (i,j)==(bx,by) else 5 if maze[i][j] == 5 else 0 for j in range(m)]
            print(' '.join(map(str,temp)))
    
    def backtrack(rx,ry,bx,by,t): # 백트랙 진해
        global answer
        # print(t,"일차")
        # printBoard(rx,ry,bx,by)
        # print()
        if maze[rx][ry] == 3 and maze[bx][by] == 4: # 둘 다 골인 했으면 정답 갱신
            answer = min(t, answer)
            return
        if maze[rx][ry] == 3: # 빨간색이 이미 골인한 경우에는 파란 수레만 움직인다
            nrx,nry = rx,ry
            for bi,bj in [(-1,0),(1,0),(0,-1),(0,1)]:
                nbx, nby = bx+bi, by+bj
                if 0 <= nbx < n and 0 <= nby < m and not blueCheck[nbx][nby] and maze[nbx][nby] < 5 and (nrx,nry) != (nbx,nby):
                    if (nrx,nry,nbx,nby) != (bx,by,rx,ry): # 서로 뒤바뀐 위치면 안되고, 둘이 위치가 겹치면 안된다.
                        blueCheck[nbx][nby] = 1
                        backtrack(nrx,nry,nbx,nby,t+1)
                        blueCheck[nbx][nby] = 0
        elif maze[bx][by] == 4: # 파란색이 이미 골인한 경우에는 빨간 수레만 움직인다
            nbx,nby = bx,by
            for ri,rj in [(-1,0),(1,0),(0,-1),(0,1)]:
                nrx, nry = rx+ri, ry+rj
                if 0 <= nrx < n and 0 <= nry < m and not redCheck[nrx][nry] and maze[nrx][nry] < 5 and (nrx,nry) != (nbx,nby):
                    if (nrx,nry,nbx,nby) != (bx,by,rx,ry): # 서로 뒤바뀐 위치면 안되고, 둘이 위치가 겹치면 안된다.
                        redCheck[nrx][nry] = 1
                        backtrack(nrx,nry,nbx,nby,t+1)
                        redCheck[nrx][nry] = 0
        else: # 둘 다 아직 골인을 못했다면
            for ri,rj in [(-1,0),(1,0),(0,-1),(0,1)]: # 빨간 수레가 움직일 수 있는 경우의 수
                nrx, nry = rx+ri, ry+rj
                if 0 <= nrx < n and 0 <= nry < m and not redCheck[nrx][nry] and maze[nrx][nry] < 5: 
                    redCheck[nrx][nry] = 1 # 격자 안에 있으면서, 벽에 부딪히지 않고, 방문하지 않는 노드
                    for bi,bj in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nbx, nby = bx+bi, by+bj
                        if 0 <= nbx < n and 0 <= nby < m and not blueCheck[nbx][nby] and maze[nbx][nby] < 5 and (nrx,nry) != (nbx,nby):
                            if (nrx,nry,nbx,nby) != (bx,by,rx,ry): # 서로 뒤바뀐 위치면 안되고, 둘이 위치가 겹치면 안된다.
                                blueCheck[nbx][nby] = 1
                                backtrack(nrx,nry,nbx,nby,t+1)
                                blueCheck[nbx][nby] = 0
                    redCheck[nrx][nry] = 0
                
                
    backtrack(rx,ry,bx,by,0) # 백트랙 진행
    
    return 0 if answer >= 10e9 else answer # 정답 반환