"""
N x N 정사각형
점프력 올리기 (k -> k+1 , (k+1)^2 초 소요, 1 <= k <= 4)
점프력 내리기 (k -> [1,k-1], 1초 소요)
짬푸! (1초 소요)
"""
import heapq as hq
import sys
input = sys.stdin.readline

def initDijk(): # 다익스트라 배열 초기화
    for i in range(n):
        for j in range(n):
            for k in range(6):
                dijk[i][j][k] = 10e9

def dijkstra(st,ed): # 다익스트라
    stx,sty = st
    que = []
    side = [(1,0),(-1,0),(0,1),(0,-1)]
    hq.heappush(que, (0, stx, sty, 1)) # 시간, 위치, 점프력
    dijk[stx][sty][1] = 0
    while len(que) > 0:
        t, x, y, jump = hq.heappop(que)
        if (x,y) == ed:
            return t
        if dijk[x][y][jump] < t:
            continue
        for to in side:
            if checkJumpable((x,y),to,jump): # 점프 가능 여부 체크
                a,b = to
                nx,ny = x+a*jump, y+b*jump 
                if dijk[nx][ny][jump] > t+1:
                    dijk[nx][ny][jump] = t+1
                    hq.heappush(que, (t+1, nx, ny, jump))
        if jump < 5: # 점프력 상승은 목표 점프력의 제곱만큼의 시간이 소요된다.
            if dijk[x][y][jump+1] > t + (jump+1)**2:
                dijk[x][y][jump+1] = t + (jump+1)**2
                hq.heappush(que, (t + (jump+1)**2, x, y, jump+1))
        if jump > 1: # 점프력 감소...
            for i in range(jump-1, 0, -1): # 점프력 감소는 1초만에 현재 점프력 미만, 1 이상의 아무 수치나 가능하다.
                if dijk[x][y][i] > t + 1: 
                    dijk[x][y][i] = t + 1
                    hq.heappush(que, (t + 1, x, y, i))
    return -1

def checkJumpable(now, to, jump): #현재 위치, 방향, 점프력
    a,b = to
    x,y = now
    nx,ny = x+a*jump, y+b*jump # 다음 위치
    if 0 <= nx < n and 0 <= ny < n: # 이동 가능 여부 체크
        if data[nx][ny] == 'S': # 도착 지점이 미끄러운 돌이면 False
            return False
        for i in range(jump+1): # 가는 길에 천적이 살면 False
            if data[x+i*a][y+i*b] == '#':
                return False
        return True
    return False

n = int(input())
dijk = [[[10e9, 10e9, 10e9, 10e9, 10e9, 10e9] for j in range(n)] for i in range(n)] # 다익스트라 배열
data = [input().rstrip() for _ in range(n)] # 지도
q = int(input()) # 우선순위 큐

for _ in range(q):
    initDijk() # 다익스트라 배열 초기화
    stx,sty,edx,edy = [int(i)-1 for i in input().split()] # 시작지점, 끝지점
    print(dijkstra((stx,sty),(edx,edy))) 