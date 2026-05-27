from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        visited = [[0 for _ in range(m)] for __ in range(n)]
        def bfs(stx, sty):
            if visited[stx][sty]:
                return
            que = deque([(stx,sty)])
            visited[stx][sty] = 1
            while len(que):
                x,y = que.popleft()
                for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx,ny = x+i, y+j
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 'O':
                        que.append((nx,ny))
                        visited[nx][ny] = 1
        
        for i in range(n): # 최외곽에서만 BFS를 시작한다.
            if board[i][0] == 'O':
                bfs(i,0)
            if board[i][m-1] == 'O':
                bfs(i, m-1)
        for i in range(m):
            if board[0][i] == 'O':
                bfs(0,i)
            if board[n-1][i] == 'O':
                bfs(n-1,i)
        for i in range(n): # 방문하지 않은 노드는 모두 X, 했다면 O로 바꾼다.
            for j in range(m):
                board[i][j] = 'O' if visited[i][j] else 'X'
        
        