def solution(n, s, a, b, fares):
    """
    n = 지점 개수
    s = 시작 지점
    a = A의 집
    b = B의 집
    """
    
    floyd = [[10e9 if i != j else 0 for j in range(n+1)] for i in range(n+1)]    
    for i,j,k in fares:
        floyd[i][j] = k
        floyd[j][i] = k
    
    for x in range(1,n+1):
        for y in range(1, n+1):
            for z in range(1, n+1):
                if floyd[y][z] > floyd[y][x] + floyd[x][z]:
                    floyd[y][z] = floyd[y][x] + floyd[x][z]
                    
    # print(floyd)
    answer = 10e9
    for i in range(1, n+1):
        answer = min(answer, floyd[s][i] + floyd[i][a] + floyd[i][b])
    
    return answer