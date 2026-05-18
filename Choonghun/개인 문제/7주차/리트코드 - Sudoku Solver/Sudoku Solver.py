class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [[0 for _ in range(10)] for __ in range(9)] # 행
        col = [[0 for _ in range(10)] for __ in range(9)] # 열
        data = [] # 2차원 배열을 1차원으로 바꾼다. <- 핵심!
        sector = {}
        for i in range(3):
            for j in range(3):
                sector[str(i)+str(j)] = [0 for _ in range(10)] # 구역
        
        for i in range(9): # 각 행/열/구역 별로 존재하는 숫자는 체크
            for j in range(9):
                if board[i][j] == '.':
                    data.append(0)
                else:
                    data.append(int(board[i][j]))
                    row[i][data[9*i+j]] = 1
                    col[j][data[9*i+j]] = 1
                    sector[str(i//3)+str(j//3)][data[9*i+j]] = 1
        
        flag = [False]
        def backtrack(ind):
            if ind >= 81: # 마지막까지 도달했다는 것은 모든 숫자를 배치했다는 뜻
                for i in range(9):
                    for j in range(9):
                        board[i][j] = str(data[i*9+j])
                flag[0] = True # 불필요한 재귀 방지를 위한 플래그
                return

            if data[ind]:
                backtrack(ind+1)
            else:
                nx,ny = ind//9, ind%9
                for k in range(1,10):
                    if not row[nx][k] and not col[ny][k] and not sector[str(nx//3)+str(ny//3)][k]:
                        data[ind] = k
                        row[nx][k], col[ny][k], sector[str(nx//3)+str(ny//3)][k] = 1,1,1
                        backtrack(ind+1)
                        if flag[0]:
                            return
                        data[ind] = 0
                        row[nx][k], col[ny][k], sector[str(nx//3)+str(ny//3)][k] = 0,0,0
        
        backtrack(0) # 백트래킹!