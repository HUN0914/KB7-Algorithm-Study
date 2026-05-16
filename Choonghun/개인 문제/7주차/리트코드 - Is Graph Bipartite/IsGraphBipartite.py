from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        n = len(graph)
        group = [0 for _ in range(n)]
        for i in range(n):
            if not group[i]:
                que = deque([(i, 0)])
                group[i] = 1
                while len(que):
                    cur, t = que.popleft()
                    for next in graph[cur]:
                        if not group[next]:
                            group[next] = (t+1)%2 + 1
                            que.append((next,t+1))
                        elif group[next] == group[cur]:
                            return False
        return True