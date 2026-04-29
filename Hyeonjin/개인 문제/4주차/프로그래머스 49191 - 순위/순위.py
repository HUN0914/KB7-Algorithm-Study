# 플로이드워셜을 사용하자

def solution(n, results):
    answer = 0
    
    win = [[False] * (n+1) for _ in range(n+1)]
    
    for a, b in results:
        win[a][b] = True
        
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if win[a][k] and win[k][b]:
                    win[a][b] = True
    
    for i in range(1, n+1):
        count = 0
        
        for j in range(1, n+1):
            if win[i][j] or win[j][i]:
                count += 1
        
        if count == n-1:
            answer += 1
    
    return answer