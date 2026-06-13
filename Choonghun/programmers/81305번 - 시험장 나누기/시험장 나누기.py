from collections import deque
answer = 10e9
def solution(k, num, links):
    # root를 찾아서
    # 각 노드별로 합을 구하고
    # 간선을 끊어보며 값을 구해보자
    
    # root 찾기
    root = 0
    n = len(num)
    check = [1 for _ in range(n)]
    for i in range(n):
        if check[i]:
            que = deque([i])
            check[i] = 0
            while len(que) > 0:
                cur = que.popleft()
                for next_node in links[cur]:
                    if next_node >= 0 and check[next_node]:
                        check[next_node] = 0
                        que.append(next_node)
            if not sum(check):
                root = i
                break
            
    # print(root)
    
    # 조합 구해서 최댓값 구하기
    edges = []
    for i in range(n):
        for j in links[i]:
            if j >= 0:
                edges.append((i,j)) # j가 곧 새로운 부분 트리의 root가 된다.
    edges_n = len(edges)
    # print(edges)
    # 따라서 생성된 모든 트리의 root는 제일 먼저 구한 root (원래 root)와 j의 집합이다.
    
    
    # 노드별 합 구하기
    check = [0 for _ in range(n)] # 루트 여부 확인용 check
    check[root] = 1
    score = [[0,0] for _ in range(n)]
    
    def dfs(cur):
        for i in range(2):
            if links[cur][i] >= 0 and not check[links[cur][i]]:
                score[cur][i] += dfs(links[cur][i])
        return sum(score[cur]) + num[cur]
    
    def get_comb(cur, stack):
        global answer
        if len(stack) == k:
            print(stack)
            for i in range(n):
                score[i] = [0,0]
            scores = []
            for x in stack:
                scores.append(dfs(x))
            # print(scores)
            answer = min(max(scores), answer)
            return
        
        for i in range(cur, edges_n):
            check[edges[i][1]] = 1
            get_comb(i+1, stack+[edges[i][1]])
            check[edges[i][1]] = 0
    
    get_comb(0, [root])
    # print(score)

    return answer

print(solution(3,[12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],[[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]))