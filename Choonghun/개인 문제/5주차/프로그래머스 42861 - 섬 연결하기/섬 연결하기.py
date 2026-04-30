def solution(n, costs):
    # 크루스칼 알고리즘 (최소 스패닝 트리 -> 각 노드를 모두 잇는 최소한의 간선 비용 구하기 문제)
    # 유사 알고리즘은 프림 알고리즘 (우선순위 큐 활용)이 있다.
    
    costs = [[c[2],c[0],c[1]] for c in costs] # 정렬을 위해 비용을 맨 앞으로 이동
    parents = [i for i in range(n+1)] # 부모 노드를 자신으로 등록
    
    def find(node):
        if parents[node] == node: #만약 node의 부모가 자기 자신이면 자신을 반환
            return node
        parents[node] = find(parents[node]) # 최상위 노드 찾기
        return parents[node]
        
    def union_node(x,y): # 트리 합치기
        px = find(x) # x와 y의 부모를 찾아서
        py = find(y)
         
        if px < py: # px가 더 작으면 py의 부모가 px
            parents[py] = px
        else: # py가 더 작으면 px의 부모가 py이다.
            parents[px] = py
    
    costs.sort() # 간선 배열 정렬
    answer = 0
    for c, x, y in costs:
        if find(x) != find(y): # 둘의 부모가 같다는 것은 속한 트리가 같다는 것이다.
            union_node(x,y)
            answer += c
    # print(parents)
    
    return answer