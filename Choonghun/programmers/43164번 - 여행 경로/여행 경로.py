answer = []
def solution(tickets):
    graph = {}
    used = [0 for _ in range(len(tickets))]
    for i in range(len(tickets)):
        dep, arr = tickets[i]
        if dep not in graph:
            graph[dep] = []
        if arr not in graph:
            graph[arr] = []
        graph[dep].append([arr, i]) # 다음 행선지, 티켓 번호
        graph[dep].sort()
    
    temp = ["ICN"]
    def dfs(cur):  
        global answer        
        if sum(used) == len(used):
            answer = list(temp)
            return 
        
        for arr, tic in graph[cur]:
            if not used[tic]:
                used[tic] = 1
                temp.append(arr)
                dfs(arr)
                if sum(used) == len(used):
                    return
                used[tic] = 0
                temp.pop()
                
    
    dfs("ICN")
    
    return answer
