import sys
from collections import deque
input = sys.stdin.readline

side = [(-1,0),(0,-1),(0,1),(1,0)] 

# 데이터 받기
N, K, L = [int(i) for i in input().split()] 
data = [[int(i) for i in input().split()] for __ in range(N)]
cleanLoc = [[0 for _ in range(N)] for __ in range(N)]
cleaner = [[]] + [[int(i)-1 for i in input().split()] for _ in range(K)]

for i in range(1, K+1):
    x,y = cleaner[i]
    cleanLoc[x][y] = i

# 1. 청소기 이동 (BFS 활용)
def moveCleaners():
    for i in range(1,K+1):
        stx,sty = cleaner[i]
        que = deque([(stx,sty,0)])
        visited = [[0 for _ in range(N)] for __ in range(N)]
        visited[stx][sty] = 1
        cands = []
        u = 10e9
        while len(que):
            x,y,t = que.popleft()
            if data[x][y] > 0:
                if t <= u:
                    if t < u:
                        u = t
                    cands.append((x,y))
                continue
            for a,b in side:
                nx,ny = x+a,y+b
                if 0 <= nx < N and 0 <= ny < N and data[nx][ny] != -1 and not visited[nx][ny] and not cleanLoc[nx][ny]:
                    visited[nx][ny] = 1
                    que.append((nx,ny,t+1))
        if cands: # 이동 위치 후보를 행-열 순으로 정렬하고 위치 이동
            cands.sort()
            x,y = cands[0]
            cleanLoc[stx][sty] = 0
            cleanLoc[x][y] = i
            cleaner[i] = [x,y]

# 2. 청소
def operateCleaners():
    cleanSide = [ # 청소 방향
        [(0,1),(-1,0),(1,0)], # 우
        [(1,0),(0,-1),(0,1)], # 하
        [(0,-1),(1,0),(-1,0)], # 좌
        [(-1,0),(0,-1),(0,1)] # 상
    ]
    for i in range(1,K+1):
        x,y = cleaner[i]
        cands = []
        for j in range(4):
            t = 0
            for a,b in cleanSide[j]:
                nx,ny = x+a,y+b
                if 0 <= nx < N and 0 <= ny < N and data[nx][ny] >= 0:
                    t += 20 if data[nx][ny] >= 20 else data[nx][ny]
            cands.append((-t, j))
        cands.sort()
        _, s = cands[0]
        data[x][y] -= 20 if data[x][y] >= 20 else data[x][y] # 먼지 제거
        for a,b in cleanSide[s]: 
            nx,ny = x+a,y+b
            if 0 <= nx < N and 0 <= ny < N and data[nx][ny] >= 0:
                data[nx][ny] -= 20 if data[nx][ny] >= 20 else data[nx][ny]

# 3. 먼지 축적
def dumpDust():
    for i in range(N):
        for j in range(N):
            if data[i][j] > 0:
                data[i][j] += 5

# 4. 먼지 확산
def expandDust():
    result = []
    for i in range(N):
        for j in range(N):
            if data[i][j] == 0:
                s = 0
                for a,b in side:
                    nx,ny = i+a, j+b
                    if 0 <= nx < N and 0 <= ny < N and data[nx][ny] > 0:
                        s += data[nx][ny]
                result.append((i,j,s//10))
    while result:
        x,y,d = result.pop()
        data[x][y] = d

# 5. 출력
def printResult():
    result = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] > 0:
                result += data[i][j]
    print(result)

def printData():
    for x in data:
        print(x)

for _ in range(L):
    moveCleaners()
    operateCleaners()
    dumpDust()
    expandDust()
    printResult()