import heapq as hq

def solution(n, s, a, b, fares):
    """
    n = 지점 개수
    s = 시작 지점
    a = A의 집
    b = B의 집
    """
    
    graph = [[] for _ in range(n+1)]
    for i,j,k in fares:
        graph[i].append((k, j))
        graph[j].append((k, i))
    
    def dijk(st, ed):
        q = []
        dijk = [10e9 for _ in range(n+1)]
        dijk[st] = 0
        for f, to in graph[st]:
            hq.heappush(q, (f, to))
            dijk[to] = f
            
        while len(q) > 0:
            f, cur = hq.heappop(q)
            if dijk[cur] < f:
                continue
            for fe, next in graph[cur]:
                if fe + f <= dijk[next]:
                    dijk[next] = fe+f
                    hq.heappush(q, (fe+f, next))
        # print(dijk)
        return dijk[ed]
    
    sToa = dijk(s,a) # s에서 a로
    sTob = dijk(s,b) # s에서 b로
    aTob = dijk(a,b) # a에서 b로
    print(sToa, sTob, aTob)
    answer = min(sToa+sTob, sToa+aTob, sTob+aTob)
    return answer