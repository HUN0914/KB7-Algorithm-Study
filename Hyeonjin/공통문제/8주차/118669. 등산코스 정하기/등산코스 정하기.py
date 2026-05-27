# 출발지 여러 개에서 동시에 다익스트라 돌리기
# 거리 합이 아니라 지나온 간선 중 가장 큰 가중치 체크

import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]

    # 빠른 탐색을 위해 set으로 변환
    gates = set(gates)
    summits = set(summits)

    for a, b, w in paths:
        graph[a].append((b, w))
        graph[b].append((a, w))

    INF = int(1e9)
    
    # intensity[노드] = 출입구에서 노드까지 가는 경로 중에서 지나온 간선의 최댓값이 가장 작은 값
    intensity = [INF] * (n + 1)

    # 우선순위 큐
    pq = []

    # 모든 출입구에서 동시에 출발
    for gate in gates:
        intensity[gate] = 0
        heapq.heappush(pq, (0, gate))

    while pq:
        # 현재까지 intensity가 가장 작은 노드부터 꺼내
        cur, node = heapq.heappop(pq)

        # 이미 이전에 더 좋은 경로를 찾았더라면 넘어가
        if cur > intensity[node]:
            continue

        # 산봉우리에 도착하면 멈추시오
        if node in summits:
            continue

        for next_node, weight in graph[node]:
            # 다른 출입구일 경우 x
            if next_node in gates:
                continue

            # max(지금까지의 최대값, 새 간선의 가중치)
            next = max(cur, weight)

            # 더 적은 intensity로 갈 수 있는 경우 값을 갱신해준다. (기존에 찾은 경로보다 더 좋은 경로인지)
            if next < intensity[next_node]:
                intensity[next_node] = next
                heapq.heappush(pq, (next, next_node))

    answer = []

    for summit in sorted(summits):
        answer.append((summit, intensity[summit]))

    answer.sort(key=lambda x: (x[1], x[0]))

    return [answer[0][0], answer[0][1]]