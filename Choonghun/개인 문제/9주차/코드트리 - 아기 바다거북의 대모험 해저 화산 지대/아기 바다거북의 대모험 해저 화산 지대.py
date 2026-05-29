from collections import deque
import sys 
input = sys.stdin.readline

side = [(0,1),(1,0),(0,-1),(-1,0)] # 우,하,좌,상 우선순위

# 데이터 받기
N,M,K = [int(i) for i in input().split()]
ocean = [[int(i) for i in input().split()] for _ in range(N)]
volLoc = [[0 for _ in range(N)] for __ in range(N)]
volExp = [0 for _ in range(K+1)]
turLoc = [[0 for _ in range(N)] for __ in range(N)]
fever = [[0 for _ in range(N)] for __ in range(N)]
turtles = [[]]
for m in range(1, M+1):
    turtles.append([int(i) for i in input().split()] + [0])
    x,y,d = turtles[-1]
    turLoc[x][y] = m
vol = [[]]
for k in range(1,K+1):
    vol.append([int(i) for i in input().split()] + [0]) # 위치, 한계치, 압력 
    x,y,l,p = vol[k]
    volLoc[x][y] = k 

# 거북이 움직이기
def moveTurtles(turn):
    for i in range(1, M+1):
        if turtles[i][-1] != 0:
            continue
        to = bfs(turtles[i])
        # print(turtles[i],to)
        if to >= 0:
            a,b = side[to]
            x,y,_ = turtles[i]
            nx,ny = x+a,y+b
            turLoc[x][y] = 0 
            if [nx,ny] == [N-1,N-1]:
                turtles[i] = [nx,ny,turn]
            else:
                turLoc[nx][ny] = i
                turtles[i] = [nx,ny,0]
# 최단거리 탐색
def bfs(turtle):
    x,y,t = turtle
    visited = [[0 for _ in range(N)] for __ in range(N)]
    visited[x][y] = 1
    que = deque([(x,y,0,0)])
    
    while len(que):
        x,y,s,t = que.popleft()
        if [x,y] == [N-1,N-1]:
            return s
        for j in range(4):
            a,b = side[j]
            nx,ny = x+a, y+b
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and not ocean[nx][ny] and not turLoc[nx][ny]:
                visited[nx][ny] = 1
                if not t:
                    que.append((nx,ny,j,t+1))
                else:
                    que.append((nx,ny,s,t+1))
    return -1

# 화산 압력 증가
def volPressureIncrement():
    for i in range(1,K+1):
        vol[i][3] += 10

# 화산 폭발
def volExplosion():
    for i in range(1,K+1):
        volExplosionSingle(i) # 단일 화산 폭발

def volExplosionSingle(idx):
    x,y,lim,pre = vol[idx]
    # print(vol[idx])
    if pre+fever[x][y] < lim or volExp[idx]: # 이 친구가 폭발을 해야 한다면
        return
    volExp[idx] = 1 # 폭발!
    fever[x][y] += lim # 열 발생!
    for i in range(4): # 4 방향으로 뻗어가기
        a,b = side[i]
        nx,ny = x+a,y+b
        volExplosionSerial(nx,ny,idx,lim//2,i)

def volExplosionSerial(x, y, idx, fev, s): 
    if not (0 <= x < N and 0 <= y < N and not ocean[x][y] and fev): # 막히거나 열이 0이 되면 return
        return
    fever[x][y] += fev # 열 더하고
    if volLoc[x][y]: # 화산이 있으면 일단 체크
        volExplosionSingle(volLoc[x][y]) 
    a,b = side[s] 
    nx,ny = x+a, y+b 
    volExplosionSerial(nx,ny,idx,fev//2,s) # 다음 폭발 ㄱㄱ

def turtleDead(): # 거북이 화석 처리
    for i in range(1,M+1):
        if turtles[i][-1] != 0: # 이미 죽었거나 도착한 거북이는 패스
            continue
        x,y,d = turtles[i]
        if fever[x][y] >= 20: # 해당 위치의 열이 20을 넘어가면
            turtles[i][-1] = -1 # 화석이 되었슴다 ㅡㅡ

def resetAllStatus(): # 열, 폭발 상태 초기화
    for i in range(N):
        for j in range(N):
            if volLoc[i][j]:
                idx = volLoc[i][j]
                if volExp[idx]:
                    vol[idx][3] = 0
                    volExp[idx] = 0
            fever[i][j] = 0

def checkFinished(): # 모든 거북이들이 죽었거나 도착했는지 체크
    for i in range(1,M+1):
        if turtles[i][-1] == 0:
            return False
    return True

turn = 1
while turn <= 100 and not checkFinished():
    moveTurtles(turn)
    volPressureIncrement()
    volExplosion()
    turtleDead()
    resetAllStatus()
    turn += 1

for i in range(1,M+1):
    if turtles[i][-1] == 0: # 도착 못한것이면 -1 출력
        print(-1)
    else:
        print(turtles[i][-1])