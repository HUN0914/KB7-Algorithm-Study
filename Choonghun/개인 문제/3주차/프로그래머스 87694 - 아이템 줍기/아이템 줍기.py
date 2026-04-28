from collections import deque

def solution(rectangle, cX, cY, itemX, itemY):
    """
        길이 1짜리 선분이 모든 영역에 대해 딱 한 곳의 부분 선분이어야 한다.
        절대로 다른 영역의 일부이면 안된다.
    """
    que = deque([(cX,cY,0)]) # 큐
    visit = [[0 for _ in range(52)] for __ in range(52)] # 방문 체크
    
    def onLine(sx, sy, ex, ey, a,b,c,d): # 해당 영역의 부분선분인지 체크
        line = [[c,b,c,d],[a,d,c,d],[a,b,a,d],[a,b,c,b]]
        
        for x1,y1,x2,y2 in line:
            if x1 == x2 and sx == ex == x1:
                if y1 <= ey <= y2 and y1 <= sy <= y2:
                    return 1
            if y1 == y2 and sy == ey == y1:
                if x1 <= ex <= x2 and x1 <= sx <= x2:
                    return 1
        return 0
        
    visit[cX][cY] = 1
    while len(que) > 0:
        x,y,t = que.popleft()
        for i, j in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx,ny = x+i, y+j
            if visit[nx][ny]:
                continue
            for k in range(len(rectangle)): # 모든 직사각형에 대하여
                a,b,c,d = rectangle[k] 
                if onLine(x,y,nx,ny,a,b,c,d): # 어떤 직사각형의 부분 선분이라면
                    flag = 1
                    for z in range(len(rectangle)): # 나머지 영역에 대해
                        if k!=z:
                            a1,b1,c1,d1 = rectangle[z]
                            if a1 <= x <= c1 and a1 <= nx <= c1 and b1 <= y <= d1 and b1 <= ny <= d1:
                                flag = 0 # 영역의 일부라면 제외
                                break
                    if flag == 1: # 소속이 유일하면 큐에 넣는다.
                        visit[nx][ny] = 1
                        if nx == itemX and ny == itemY:
                            return t+1
                        que.append((nx,ny,t+1))
    answer = 0
    return answer

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
print(solution(	[[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))
print(solution(	[[2, 2, 3, 3]], 2, 2, 3, 3))