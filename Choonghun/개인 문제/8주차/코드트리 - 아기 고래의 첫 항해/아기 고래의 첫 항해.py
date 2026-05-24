"""
N x N 격자, 헤엄칠 수 있는 바다 (0) or 지나갈 수 없는 암초(1)
(r,c)에서 출발, d가 바라보는 방향 상(1)/하(2)/좌(3)/우(4)

#1. 인접 탐험
1. 바라보는 방향 / 2. 좌회전(90도 반시계 회전 & 직진) / 3. 우화전(90도 시계 회전 & 직진) / 4. 180도 회전 후 직진

#2. 가장 가까운 바다로 이동
최소 이동 횟수를 가지는 방문하지 않은 바다로 이동
"""
from collections import deque
import sys
input = sys.stdin.readline

direction = [(-1,0), (1,0), (0,-1), (0,1)] # 상/하/좌/우
turnLeft = [2, 3, 1, 0]
turnRight = [3, 2, 0, 1]
turnReverse = [1, 0, 3, 2]

N, r, c, d = [int(i) for i in input().split()] # 입력 받기
r -= 1
c -= 1
d -= 1 # 인덱스 맞추기

obst = [[int(i) for i in input().split()] for _ in range(N)] # 장애물 존재 여부
visited =[[0 for _ in range(N)] for __ in range(N)] # 방문 여부
visited[r][c] = 1

def checkDirection(x,y,dirIdx): # 1단계 이동 여부 체크 메서드
    # 현재 바라보는 방향
    dx,dy = direction[dirIdx]
    nx,ny = x+dx, y+dy
    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and not obst[nx][ny]:
        return [nx,ny,dirIdx]
    # 좌회전
    tx,ty = direction[turnLeft[dirIdx]]
    nx,ny = x+tx, y+ty
    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and not obst[nx][ny]:
        return [nx,ny,turnLeft[dirIdx]]
    # 우회전
    tx,ty = direction[turnRight[dirIdx]]
    nx,ny = x+tx, y+ty
    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and not obst[nx][ny]:
        return [nx,ny,turnRight[dirIdx]]
    # 180도 회전
    tx,ty = direction[turnReverse[dirIdx]]
    nx,ny = x+tx, y+ty
    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and not obst[nx][ny]:
        return [nx,ny,turnReverse[dirIdx]]
    
    return [-1,-1,-1]

def findNearestOcean(stx,sty): # BFS
    side = [2, 1, 3, 0] #좌,하,우,상
    visit = [[0 for _ in range(N)] for __ in range(N)] # 방문 체크
    queue = deque([(stx,sty,0)])
    visit[stx][sty] = 1
    answer = [10000, 10000, d, 10000] # 다음 위치 및 방향, 거리(임시)
    while len(queue):
        # print(queue)
        x,y,ndist = queue.popleft()
        for c in side: # 좌, 하, 우, 상 순서로 체크
            i,j = direction[c]
            nx,ny = x+i, y+j
            ax,ay,_,adist = answer # 현 시점 최근접 거리와 비교
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and not obst[nx][ny]:
                if adist > ndist+1: # 더 가깝고
                    if not visited[nx][ny]: # 방문하지 않은 위치면
                        answer = [nx,ny,c,ndist+1] # 갱신
                    visit[nx][ny] = 1
                    queue.append((nx,ny,ndist+1))
                elif adist == ndist+1: # 현재 최근접거리와 거리가 동일한데
                    if not visited[nx][ny]: # 방문하지 않은 곳이고
                        if nx < ax: # 더 좌상단에 위치하면 갱신
                            answer = [nx,ny,c,ndist+1]
                        elif nx == ax and ny < ay:
                            answer = [nx,ny,c,ndist+1]
    return answer[:3] # 위치, 방향만 반환

while True:
    print(r+1,c+1) # 위치 출력
    ndir = checkDirection(r,c,d) # 인접 노드 체크
    if ndir == [-1,-1,-1]: # 없으면 가장 가까운 지역 체크
        ndir = findNearestOcean(r,c)
    
    if ndir[0] == 10000: # 그마저도 없다면 모두 방문한 것이므로 종료
        break
    
    r,c,d = ndir # 위치 이동
    visited[r][c] = 1 # 방문 처리
