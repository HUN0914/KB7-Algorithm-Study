import heapq as hq
def solution(n, edge):
    dijk = [10e9 for _ in range(n+1)]
    dijk[1] = 0
    q = []
    maxi = 0
    graph = [[] for _ in range(n+1)]
    for i,j in edge:
        graph[i].append(j)
        graph[j].append(i)
    hq.heappush(q, (0, 1))
    while q:
        dist, cur = hq.heappop(q)
        if dist > dijk[cur]:
            continue
        for next in graph[cur]:
            if dijk[next] > dist+1:
                dijk[next] = dist+1
                hq.heappush(q,(dist+1,next))
                
    maxi = 0
    answer = 1
    for i in range(1,n+1):
        if dijk[i] < 10e9 and maxi < dijk[i]:
            maxi = dijk[i]
            answer = 1
        elif maxi == dijk[i]:
            answer += 1
                
    return answer