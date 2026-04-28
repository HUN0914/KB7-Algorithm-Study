import heapq as hq
def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n+1)]
    for i,j in roads:
        graph[i].append(j)
        graph[j].append(i)
    dijk = [10e9 for _ in range(n+1)]
    dijk[destination] = 0
    q = []
    hq.heappush(q, (0,destination)) # 도착지에서 역으로 다익스트라 진행
    while len(q) > 0:
        dist, cur = hq.heappop(q)
        if dijk[cur] < dist:
            continue
        for next in graph[cur]:
            if dijk[next] > dist+1:
                dijk[next] = dist+1
                hq.heappush(q, (dist+1,next))
    answer = [-1 if dijk[i] >= 10e9 else dijk[i] for i in sources]
                
    return answer