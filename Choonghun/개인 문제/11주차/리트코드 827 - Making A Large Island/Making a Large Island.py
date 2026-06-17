from collections import deque
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[0 for _ in range(n)] for __ in range(n)] # 방문 배열
        team = set() # 0을 1로 바꿔서 생기는 연결망
        area = [[0,1]] # 영역 넓이 / 주변에 잉여칸(0) 여부
        num = [0] # 섬의 개수
        def bfs(x,y): # BFS (각 섬의 넓이 구하기)
            que = deque([(x,y)])
            area.append([0,0])
            num[0] += 1
            visited[x][y] = num[0]
            while len(que):
                # print(que)
                x,y = que.popleft()
                dfs(visited[x][y],x,y,0) # 섬의 모든 지점에서 depth 짜리 DFS 진행
                area[num[0]][0] += 1
                for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:
                    nx,ny = x+i, y+j
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] and not visited[nx][ny]:
                        visited[nx][ny] = num[0]
                        que.append((nx,ny))
        
        def dfs(st,x,y,depth):
            if depth: # depth 1이면
                temp = set() # 임시 set 선언
                temp.add(st) # 시작 위치의 섬 번호 삽입
                for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:
                    nx,ny = x+i, y+j
                    if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] and visited[nx][ny] != st:
                        temp.add(visited[nx][ny]) # 끝에 다다른 섬의 번호가 시작 번호와 다르면 삽입
                team.add(tuple(temp)) # temp를 튜플로 바꾸어 팀 명단에 추가
                return
            
            for i,j in [(-1,0),(0,-1),(1,0),(0,1)]: # depth 0일때는 기존 dfs
                nx,ny = x+i, y+j
                if 0 <= nx < n and 0 <= ny < n:
                    if not grid[nx][ny] and not depth: # grid[nx][ny]가 0일때
                        area[st][1] = 1
                        dfs(st,nx,ny,depth+1)
        
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and grid[i][j]:
                    bfs(i,j) # 방문하지 않은 1인 노드에서 BFS 시작
    
        answer = 1
        for d in team: # 모든 팀 명단에 대해서
            t = 1 # 0에서 1로 바꾼 칸 하나
            for i in d: 
                t += area[i][0] # 팀을 구성하는 모든 영역의 넓이 더하기
            answer = max(answer, t) # 최댓값
        if answer == 1: # 근데 정답이 1이면 팀이 없다는 의미이므로
            answer = max([ar[0]+ar[1] for ar in area]) 
            # 현존하는 모든 섬에 대해서 주변에 잉여 영역이 있는지 체크하고 있다면 +1 없다면 +0 해서 최대 넓이 구하가
        return answer # 정답 반환

            
