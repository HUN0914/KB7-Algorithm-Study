import heapq as hq
import sys

input = sys.stdin.readline

n,k,x,y = [int(i) for i in input().split()]
graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]
for _ in range(x):
    s,e,d = [int(i) for i in input().split()]
    graph1[s].append([e,d])
    graph1[e].append([s,d])
for _ in range(y):
    s,e,d = [int(i) for i in input().split()]
    graph2[s].append([e,d])
    graph2[e].append([s,d])
dijk = [float("INF") for _ in range(n+1)]
dijk[1] = 0
q = [(0, 1)]
while len(q) > 0:
    t, cur = hq.heappop(q)
    if dijk[cur] < t:
        continue
    if t >= k:
        for next, cost in graph2[cur]:
            next_cost = t + cost
            if next_cost < dijk[next]:
                dijk[next] = next_cost
                hq.heappush(q, (next_cost, next))
    elif t < k:
        for next, cost in graph2[cur]:
            next_cost = k + cost
            if next_cost < dijk[next]:
                dijk[next] = next_cost
                hq.heappush(q, (next_cost, next))

    for next, cost in graph1[cur]:
        next_cost = t+cost
        if next_cost < dijk[next]:
            dijk[next] = next_cost
            hq.heappush(q, (next_cost, next))
    
# print(dijk)
print(dijk[n])
        
