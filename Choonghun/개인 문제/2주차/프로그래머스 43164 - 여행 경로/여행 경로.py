answer = []
def solution(tickets):
    graph = {}
    used = [0 for _ in range(len(tickets))]
    for i in range(len(tickets)): #티켓정보를 그래프에 입력
        dep, arr = tickets[i]
        if dep not in graph:
            graph[dep] = []
        if arr not in graph:
            graph[arr] = []
        graph[dep].append([arr, i]) # 다음 행선지, 티켓 번호
        graph[dep].sort() #문자열순으로 정렬
    
    temp = ["ICN"] #시작은 인천에서
    def dfs(cur):  #DFS 시작
        global answer        
        if sum(used) == len(used): #모두 방문했으면 종료
            answer = list(temp)
            return 
        
        for arr, tic in graph[cur]: #각 노드의 다음 행선지에 대해서
            if not used[tic]: # 사용하지 않은 티켓이면
                used[tic] = 1 # 티켓 체크하고
                temp.append(arr) # 경로 저장용 임시 배열에 넣고
                dfs(arr) # 재귀
                if sum(used) == len(used): #모두 방문했으면 종료
                    return
                used[tic] = 0 # 해제하고
                temp.pop() # 경로도 pop
                
    
    dfs("ICN") # DFS 시작은 인천
    
    return answer
