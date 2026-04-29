def solution(n):
    answer = 0
    
    # 체스를 기록할 보드
    board = [[0] * n for _ in range(n)]
    
    # 백트래킹 함수 (한 행씩 퀸을 두고 다시 돌아가서 다른 경우도 보는 것)
    def backtracking(row):
        nonlocal answer
        
        # 종료조건 (마지막 행까지 다 봤으면 종료)
        if row == n:
            answer += 1
            return
        
        # 같은 행의 모든 열을 순회
        for col in range(n):
            possible = True 
            
            # 1. 같은 열에 퀸이 이미 있음?
            for r in range(row):
                if board[r][col] == 1:
                    possible = False
                    break
            
            if not possible:
                continue
            
            # 2. 왼쪽 대각선 위에 퀸이 이미 있음?
            x = row - 1
            y = col - 1
            while x >= 0 and y >= 0:
                if board[x][y] == 1:
                    possible = False
                    break
                x -= 1
                y -= 1
            
            if not possible:
                continue
            
            # 3. 오른쪽 대각선 위에 퀸이 이미 있음?
            x = row - 1
            y = col + 1
            while x >= 0 and y < n:
                if board[x][y] == 1:
                    possible = False
                    break
                x -= 1
                y += 1
            
            if not possible:
                continue
            
            # 이 조건을 다 통과했다면 퀸을 둘 수 있다!
            board[row][col] = 1
            
            # 다음 행으로 넘어가자
            backtracking(row + 1)
            
            # 돌아왔으면 이미 놓은 퀸을 없애줘야해
            board[row][col] = 0
        
    
    backtracking(0)
    
    return answer