flag = 0 # 플래그
answer = 10e9 # 정답
def solution(n, weak, dist):
    """
        n (1 <= n <= 200) : 둘레
        weak (1 <= len(weak) <= 15, 0 <= weak[i] <= n-1): 취약 지점
        dist (1 <= len(dist) <= 8, 1 <= dist[i] <= 100) : 각 친구들이 이동할 수 있는 거리
    """
    weak.sort() # 취약 범위 정렬 
    graph = {} # 그래프 생성
    w = len(weak) # 취약 위치 개수
    f = len(dist) # 친구 인원
    for i in range(w):
        graph[i] = [[],[]]
        
    for i in range(w):
        if i == w - 1: # 맨 끝의 위치는 처음 위치와 연결됨
            graph[i][1] = [0, n-weak[i]+weak[0]]
            graph[0][0] = [i, n-weak[i]+weak[0]]
        else: # 나머지
            graph[i][1] = [i+1, weak[i+1]-weak[i]] # 이전 위치와, 거리
            graph[i+1][0] = [i, weak[i+1]-weak[i]] # 다음 위치와, 거리
            
    check = [0 for _ in range(w)] # 방문여부 체크
    f_check = [0 for _ in range(f)] # 인원 조합 체크
    def backtrack(ind, dis, lim_idx, num):
        global flag
        # print(check, sum(check), w, lim_idx)
        if num > answer: # 현재 선택된 인원이 지금까지 구한 최선의 결과보다 크면 종료
            return
        if sum(check) == w: # 모든 구역을 탐색했다면 조합을 발견한 것이므로 flag를 현재 선택된 인원 수로 변경
            flag = num
            return
        for next, p in graph[ind]: # 현재 위치에 대해서
            if not check[next]: # 다음 또는 이전 위치가 방문하지 않은 곳이라면
                if dis + p <= dist[lim_idx]: # 아직 거리 제한에 도달하지 않았을시
                    check[next] = 1 # 방문처리
                    backtrack(next, dis+p, lim_idx, num) # 백트래킹
                    check[next] = 0 
                else: # 거리 제한을 초과했을시
                    check[next] = 1 # 방문처리
                    for i in range(f): 
                        if not f_check[i]: # 아직 선택되지 않은 인원에 대하여
                            f_check[i] = 1 # 선택 처리
                            backtrack(next, 0, i, num+1) # 새로운 인원 투입하여 신규 백트래킹
                            f_check[i] = 0
                    check[next] = 0
    
    
    def findCollections(): # 조합 찾는 메서드
        global answer
        for i in range(w):
            check[i] = 1
            for j in range(f):
                f_check[j] = 1
                backtrack(i, 0, j, 1) 
                f_check[j] = 0
                if flag: 
                    answer = min(flag, answer) # 갱신
            check[i] = 0
                
        return answer if answer < 10e9 else -1 # 발견 못했다면 -1 반환
    
    return findCollections()