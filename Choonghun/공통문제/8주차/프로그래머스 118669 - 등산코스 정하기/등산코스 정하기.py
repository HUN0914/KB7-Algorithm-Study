import heapq as hq
def solution(n, paths, gates, summits):
    points = [1 for _ in range(n+1)] # 모든 지점
    graph = [[] for _ in range(n+1)] # 경로
    answer = [10e9, 10e9] # 정답
    summits.sort() # 산봉우리 정렬
    for x in gates: # 게이트는 0으로 (push 하면 안됨)
        points[x] = 0
    for y in summits: # 산봉우리
        points[y] = 2
    for i,j,k in paths: 
        graph[i].append((k,j))
        graph[j].append((k,i))
    
    def dijkstra(st): # 다익스트라
        dijk = [10e9 for _ in range(n+1)] # 다익스트라 배열
        dijk[st] = 0 # 시작은 0
        que = [] # 우선순위 큐(heapq 사용)
        hq.heappush(que, (0, st)) 
        while que: # 다익스트라 시작
            k, cur = hq.heappop(que)
            if k > dijk[cur] or k >= answer[1]: # k 또는 기존 최솟값보다 크다면 의미 x
                continue
            for tk, next in graph[cur]:
                nk = tk if tk > k else k
                if dijk[next] > nk:
                    dijk[next] = nk
                    if points[next] == 1:
                        hq.heappush(que, (nk,next))
                    elif not points[next]:
                        if answer[1] > nk or (answer[1] == nk and answer[0] > st): # 답 갱신
                            answer[0],answer[1] = st, nk
            
    for s in summits:
        dijkstra(s)
        
    return answer