n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
points = []
for i in range(m):
    x, y = map(int, input().split())
    points.append((x - 1, y - 1))

# Please write your code here.
result = [0]
visited = [[0 for _ in range(n)] for __ in range(n)]
def dfs(x, y, idx): # dfs 진행
    # print(x,y,idx)
    if idx >= m+1: # 모든 체크포인트를 순서대로 진행했다면 카운트
        result[0] += 1
        return

    for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx,ny = x+i, y+j
        if 0 <= nx < n and 0 <= ny < n and not grid[nx][ny]:
            if points[idx-1] == (nx,ny): # 다음 체크포인트인데
                if visited[nx][ny]: # 이미 방문을 했다면 순서가 꼬인 것이므로 return
                    return
                else: # 아니라면 정상적인 순서이므로 방문처리
                    visited[nx][ny] = 1
                    dfs(nx,ny,idx+1)
                    visited[nx][ny] = 0
            elif not visited[nx][ny]: # 그 외의 경우에는 dfs 진행
                visited[nx][ny] = 1
                dfs(nx,ny,idx)
                visited[nx][ny] = 0

stx,sty = points[0] # 맨 처음 시작 지점은 고정
visited[stx][sty] = 1 # 방문 처리
dfs(stx,sty,2) # idx는 2부터
print(result[0])