import sys
sys.setrecursionlimit(10**6)
def solution(a, edges):
    answer = -1
    if sum(a):
        return answer
    answer = [0]
    stack = []
    n = len(a)
    graph = [[] for _ in range(n)]
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
    
    def dfs(cur, prev):
        for next in graph[cur]:
            if prev != next:
                a[cur] += dfs(next, cur)
                answer[0] += abs(a[next])
                a[next] = 0
        return a[cur]
    
    dfs(0, -1)
    return answer[0]