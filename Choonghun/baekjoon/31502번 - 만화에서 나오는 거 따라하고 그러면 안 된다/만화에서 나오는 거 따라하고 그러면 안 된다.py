import heapq as hq
from collections import deque
import sys
input = sys.stdin.readline

n,m = [int(i) for i in input().split()]
q = []
graph = [[] for _ in range(n+1)]
a,b,c = [int(i) for i in input().split()]
for _ in range(m):
    st,ed,cost = [int(i) for i in input().split()]
    graph[st].append((ed,cost))
    graph[ed].append((st,cost))

dist = [10e9 for _ in range(n+1)]

que = deque([])
que.append((c, 0))
dist[c] = 0

while len(que) > 0: # 학교로 인근 나무로부터 다른 나무들까지의 최소 거리
    cur, dis = que.popleft()
    if dist[cur] < dis:
        continue
    for next, _ in graph[cur]: # BFS 진행
        if dist[next] > dis+1:
            que.append((next,dis+1))
            dist[next] = dis+1

cur = b
route = [b]
while True: # 한별 기준으로 학교로 도달하는데 거치는 루트
    if cur == c:
        break
    nexts = [] # 다음 은행나무 후보
    for next, cost in graph[cur]: 
        if dist[next] == dist[cur]-1: # 최단거리를 찾는 방법
            nexts.append((len(graph[next]), next)) # 후보에 더한다.
    nexts.sort(reverse=True) # 정렬 후
    cur = nexts[0][1] # 맨 앞의 후보 (가장 도로가 많고, 번호가 높은)
    route.append(cur) # 추가

q = []
toka = [float("INF") for _ in range(n+1)]
toka[a] = 0
hq.heappush(q, (0, a)) # 토카 기준으로 각 은행나무로 도달하는 최단 시간을 구하기 위해 다익스트라 사용
while len(q) > 0:
    cost, cur = hq.heappop(q)
    if cost > toka[cur]:
        continue
    for next, c in graph[cur]:
        if toka[next] > cost + c: 
            toka[next] = cost+c
            hq.heappush(q, (cost+c, next))

route.sort() # 루트를 가장 작은 인덱스부터 찾도록 정렬
value = toka[route[0]] # 처음 값
answer = route[0] # 현재 인덱스
for i in route: # 순회하며
   if value > toka[i]: # 현재 나무까지 걸리는 시간이 더 낮다면
       answer = i #갱신
       value = toka[i]
print(answer) # 답 출력

