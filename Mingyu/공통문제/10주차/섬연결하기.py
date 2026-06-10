def solution(n, costs):
    answer = 0

    # 비용 기준 오름차순 정렬
    costs.sort(key=lambda x: x[2])

    parent = [i for i in range(n)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        root_a = find(a)
        root_b = find(b)

        if root_a == root_b:
            return False

        parent[root_b] = root_a
        return True

    for a, b, cost in costs:
        if union(a, b):
            answer += cost

    return answer
