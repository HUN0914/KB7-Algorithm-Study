import sys
from collections import deque
input = sys.stdin.readline

N, M, K = [int(i) for i in input().split()]
data = [[int(i) for i in input().split()] for _ in range(N)] # 맵 정보
atTime = [[0 for _ in range(M)] for __ in range(N)] # 최근 공격 시간
route = [(0,0) for _ in range(101)] # 공격자-타겟 최단 거리
visited = [[0 for _ in range(M)] for __ in range(N)] # 방문 배열
related = [[1 for _ in range(M)] for __ in range(N)] # 관련된 영역들 (1: 관련 X, 0: 관련)

def findAttacker(): # 공격자 찾기
    mini = 10e9
    candi = []
    for i in range(N):
        for j in range(M):
            if data[i][j]:
                if mini > data[i][j]:
                    mini = data[i][j]
                    candi.clear()
                    candi.append((atTime[i][j],i+j,j,i))
                elif mini == data[i][j]:
                    candi.append((atTime[i][j],i+j,j,i))
    candi.sort(reverse = True)
    return (candi[0][3], candi[0][2])

def findTarget(): # 타겟 찾기
    maxi = 0
    candi = []
    for i in range(N):
        for j in range(M):
            if data[i][j]:
                if maxi < data[i][j]:
                    maxi = data[i][j]
                    candi.clear()
                    candi.append((atTime[i][j],i+j,j,i))
                elif maxi == data[i][j]:
                    candi.append((atTime[i][j],i+j,j,i))
    candi.sort()
    return (candi[0][3], candi[0][2])

def findShortestRoute(attk, targ): # 최단 경로 찾기
    resetVisited() # 방문 배열 초기화
    x,y = attk
    edx,edy = targ 
    bfs(x,y,edx,edy) # BFS 시작

def lazorAttack(attk, targ): # 레이저 공격
    x,y = attk
    related[x][y] = 0
    dam = data[x][y]
    for i in range(len(route)): # 최단 경로를 따라간다.
        tx, ty = route[i]
        if (tx,ty) == targ:
            data[tx][ty] -= dam
        else:
            if (tx,ty) != attk:
                data[tx][ty] -= dam//2

        related[tx][ty] = 0 # 관련된 영역은 모두 0으로 변경

def bombAttack(attk, targ): # 폭탄 공격
    tx,ty = targ
    x,y = attk
    related[x][y] = 0
    dam = data[x][y]
    for i in [-1,0,1]: # 중심지 인근 8곳 피격
        for j in [-1,0,1]:
            nx,ny = tx+i, ty+j
            if (nx,ny) == targ:
                data[nx][ny] -= dam # 중심지는 풀뎀
            else:
                if ny < 0:
                    ny = M-1
                elif ny >= M:
                    ny = 0
                if nx < 0:
                    nx = N-1
                elif nx >= N:
                    nx = 0
                if (nx,ny) != attk: 
                    data[nx][ny] -= dam // 2 # 공격자를 제외한 인근 피격지는 반샷

            related[nx][ny] = 0 # 관련된 영역은 모두 0으로 변경

def resetVisited(): # 스택, 방문 배열 초기화
    for i in range(N):
        for j in range(M):
            visited[i][j] = 0
    route.clear()
    for _ in range(101):
        route.append((0,0))

def bfs(x,y,edX,edY): # 최단거리 찾기 위한 BFS
    global route
    que = deque([(x,y,[(x,y)])])
    visited[x][y] = 1
    while len(que) > 0:
        cur = que.popleft()
        curX, curY, rte = cur[0], cur[1], cur[2]
        for i,j in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx,ny = curX+i,curY+j

            if ny < 0: # 맵 외부로 나가게 되면 그 반대편으로 나오도록 처리
                ny = M-1
            elif ny >= M:
                ny = 0
            if nx < 0:
                nx = N-1
            elif nx >= N:
                nx = 0

            if not visited[nx][ny] and data[nx][ny]:
                visited[nx][ny] = 1
                if (nx,ny) == (edX,edY):
                    route = rte+[(nx,ny)]
                    return
                que.append((nx,ny,rte+[(nx,ny)]))
    
def destroyTurrets(): # 공격력 0 이하는 모두 파괴(0) 처리
    for i in range(N):
        for j in range(M):
            if data[i][j] <= 0:
                data[i][j] = 0

def repairTurrets():
    for i in range(N):
        for j in range(M):
            if data[i][j]: # 관련되지 않은 포탑들 공격력 1 증가
                data[i][j] += related[i][j]
            related[i][j] = 1

def checkEnd():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if data[i][j]:
                if not cnt:
                    cnt += 1
                else:
                    return False
    return cnt

for i in range(1,K+1):
    if checkEnd(): # 포탑이 하나 남았는지 확인
        break

    attk = findAttacker() # 공격자 찾기
    targ = findTarget() # 타겟 찾기
    x,y = attk
    data[x][y] += N+M # 공격력 증가
    atTime[x][y] = i # 공격 시간 갱신
    findShortestRoute(attk, targ) # 가장 짧은 루트 BFS로 탐색
    if len(route) < 101: # 루트 발견시
        lazorAttack(attk, targ) # 레이저 공격
    else: # 발견 X
        bombAttack(attk,targ) # 포탄 공격
    destroyTurrets() # 포탑 파괴 처리
    repairTurrets() # 포탑 수리

print(max([max(x) for x in data])) # 최대 공격력 포탑 출력