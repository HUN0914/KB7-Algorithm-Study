from collections import deque
def solution(n, m, hole):
    visit = [[[0,0] for _ in range(m+1)] for __ in range(n+1)]
    data = [[1 for _ in range(m+1)] for __ in range(n+1)] 
    for i, j in hole:
        data[i][j] = 0
    que = deque([(1,1,1,0)])
    visit[1][1][1] = 1
    while len(que) > 0:
        x,y,shoe,t = que.popleft()
        if shoe:
            for i, j in [(-2,0),(2,0),(0,-2),(0,2)]:
                nx,ny = x+i, y+j
                if 1 <= nx <= n and 1 <= ny <= m and not visit[nx][ny][0] and data[nx][ny]:
                    # print(nx,ny,shoe-1,t)
                    if [nx,ny] == [n,m]:
                        return t+1
                    que.append((nx,ny,0,t+1))
                    visit[nx][ny][0] = 1
        for i, j in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x+i, y+j
            if 1 <= nx <= n and 1 <= ny <= m and not visit[nx][ny][shoe] and data[nx][ny]:
                # print(nx,ny,shoe,t)
                if [nx,ny] == [n,m]:
                    return t+1  
                que.append((nx,ny,shoe,t+1))
                visit[nx][ny][shoe] = 1
        
    return -1