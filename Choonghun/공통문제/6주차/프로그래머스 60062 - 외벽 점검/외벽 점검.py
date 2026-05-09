flag = 0 # 플래그
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
        if sum(f_check) > num: # 현재 선택된 인원이 제한보다 크면 종료
            return
        if sum(check) == w: # 모든 구역을 탐색했다면 조합을 발견한 것이므로 flag를 1로 변경
            flag = 1
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
                            backtrack(next, 0, i, num) # 새로운 인원 투입하여 신규 백트래킹
                            f_check[i] = 0
                    check[next] = 0
    
    
    def findCollections(): # 조합 찾는 메서드
        answer = -1 
        for num in range(1,f+1):
            for i in range(w):
                check[i] = 1
                for j in range(f):
                    f_check[j] = 1
                    backtrack(i, 0, j, num) 
                    f_check[j] = 0
                    if flag: # 발견했다면 해당 인원수를 그대로 반환
                        answer = num
                        return answer
                check[i] = 0
                
        return answer # 발견 못했다면 초기값 -1이 유지되므로 -1 반환
    
    return findCollections()
        
    # answer = 0
    # return answer
print(solution(12, [1,5,6,10], [1,2,3,4]))