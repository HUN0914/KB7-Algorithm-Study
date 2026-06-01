import sys
input = sys.stdin.readline

def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    data = [[0 for _ in range(M)] for __ in range(N)]
    for t, r1, c1, r2, c2, d in skill:
        if t==1:
            data[r1][c1] += -d
            if r2 < N-1:
                data[r2+1][c1] += d
            if c2 < M-1:
                data[r1][c2+1] += d
                if r2 < N-1:
                    data[r2+1][c2+1] += -d
        else:
            data[r1][c1] += d
            if r2 < N-1:
                data[r2+1][c1] += -d
            if c2 < M-1:
                data[r1][c2+1] += -d
                if r2 < N-1:
                    data[r2+1][c2+1] += d

    for i in range(N):
        for j in range(1, M):
            data[i][j] = data[i][j] + data[i][j-1]
            
    for j in range(M):
        for i in range(1, N):
            data[i][j] = data[i][j] + data[i-1][j]
            
    for i in range(N):
        for j in range(M):
            if data[i][j] + board[i][j] > 0:
                answer += 1
                
    return answer