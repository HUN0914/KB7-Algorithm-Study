from collections import deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        que = deque([])
        que.append(click)
        n, m = len(board), len(board[-1])
        visited = [[0 for _ in range(m)] for __ in range(n)]
    
        while len(que) > 0:
            x,y = que.popleft()
            count = 0
            temp = []
            if board[x][y] == 'M':
                board[x][y] = 'X'
                return board
            for i,j in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
                nx,ny = x+i, y+j
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny] == "M":
                        count += 1
                    temp.append((nx,ny))
                
            if not count:
                board[x][y] = 'B'
                while temp:
                    nx,ny = temp.pop()
                    if not visited[nx][ny]:
                        visited[nx][ny] = 1
                        que.append([nx,ny])
            else:
                board[x][y] = str(count)
                
        
        return board