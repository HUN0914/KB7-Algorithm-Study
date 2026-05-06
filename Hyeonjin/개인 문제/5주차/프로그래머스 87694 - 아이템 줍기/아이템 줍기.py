'''
1. 보드에 모든 사각형 칠하기 (좌표 2배해서)
2. 내부 비우기
3. bfs 돌리기
4. 거리 구하기 (나누기 2 꼭 하기)
'''
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 101 for _ in range(101)]
    
    for x1, y1, x2, y2 in rectangle:
        # 좌표 2배
        x1, y1, x2, y2 = 2*x1, 2*y1, 2*x2, 2*y2
        
        # 보드에 사각형 칠하기
        for r in range(y1, y2+1):
            for c in range(x1, x2+1):
                board[r][c] = 1
        
        
    # 한번에 내부 비우기
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = 2*x1, 2*y1, 2*x2, 2*y2

        for r in range(y1 + 1, y2):
            for c in range(x1 + 1, x2):
                board[r][c] = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # bfs 함수
    def bfs(sx, sy):
        q = deque()
        q.append((sx, sy))
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx > 100 or ny < 0 or ny > 100:
                    continue
                
                if board[nx][ny] == 1:
                    board[nx][ny] = board[x][y] + 1
                    q.append((nx, ny))
    
    bfs(characterY*2, characterX*2)
    
    answer = board[itemY*2][itemX*2] // 2
    
    return answer