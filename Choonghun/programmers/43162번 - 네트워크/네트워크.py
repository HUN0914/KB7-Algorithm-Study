from collections import deque

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    check = [0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j]:
                graph[i].append(j)
    
    for i in range(n):
        if not check[i]:
            answer += 1
            que = deque([i])
            while len(que) > 0:
                cur = que.popleft()
                for next in graph[cur]:
                    if not check[next]:
                        que.append(next)
                        check[next] = 1 
              
    return answer