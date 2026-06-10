def solution(n, infection, edges, k):
    answer = [0]
    infected = [0 for _ in range(n+1)]
    infected[infection] = 1
    
    def backtrack(depth, prev):
        answer[0] = max(answer[0], sum(infected[1:]))
        if depth >= k:
            return
        
        for nt in [1,2,3]:
            temp = []
            while True:
                flag = 0
                for x,y,t in edges:
                    if nt == t:
                        if infected[x] and not infected[y]:
                            infected[y] = 1
                            flag = 1
                            temp.append(y)
                        elif infected[y] and not infected[x]:
                            infected[x] = 1
                            flag = 1
                            temp.append(x)
                if not flag:
                    break
            if temp:
                backtrack(depth if prev == nt else depth+1, nt)

            while temp:
                infected[temp.pop()] = 0
    
    backtrack(0, 0)
        
    return answer[0]