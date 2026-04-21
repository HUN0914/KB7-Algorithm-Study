def solution(tickets):
    answer = []
    
    # 사전순으로 정렬 (어차피 dfs를 ICN부터 시작할거니까 그냥 사전순으로 정렬만 하면된다.)
    tickets.sort()
    
    visited = [False] * len(tickets)
    path = ['ICN']
    
    def dfs(current, used_count):
        if used_count == len(tickets):
            answer[:] = path
            return True
        
        for i in range(len(tickets)):
            if visited[i] == False and tickets[i][0] == current:
                visited[i] = True
                path.append(tickets[i][1])
                if dfs(tickets[i][1], used_count + 1):
                    return True
                visited[i] = False
                path.pop()
        return False
                
    
    dfs('ICN', 0)
     
    return answer