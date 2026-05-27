import heapq as hq
def solution(n, paths, gates, summits):
    points = [1 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    summits.sort()
    for y in summits:
        points[y] = 0
    for i,j,k in paths:
        graph[i].append((k,j))
        graph[j].append((k,i))
    answers = []
    def dijkstra():
        que = []
        dijk = [10e9 for _ in range(n+1)]
        for gate in gates:
            dijk[gate] = 0
            hq.heappush(que, (0, gate))
        
        while que:
            k, cur = hq.heappop(que)
            if k > dijk[cur]:
                continue
            for tk, next in graph[cur]:
                nk = tk if tk > k else k
                if dijk[next] > nk:
                    dijk[next] = nk
                    if points[next] == 1:
                        hq.heappush(que, (nk,next))
                    elif not points[next]:
                        answers.append([nk,next])
            
    dijkstra()
    answers.sort()
    return [answers[0][1],answers[0][0]]