from collections import deque

def solution(n, edge):
    answer = 0
    
    # 간선 정보 리스트 한 사이즈 더 크게 만들기
    graph = [[] for _ in range(n+1)]
    
    # 간선 정보 저장하기
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # 거리를 저장할 그래프
    dist = [-1] * (n+1)
    
    visited = [False] * (n+1)
        
    q = deque()
    q.append(1)
    dist[1] = 0
    visited[1] = True
    
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            if visited[i] == False:
                dist[i] = dist[now] + 1
                visited[i] = True
                q.append(i)
    
    max_dist = max(dist)

    for i in dist:
        if i == max_dist:
            answer += 1
    
    return answer