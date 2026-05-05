"""

N x N 정사각형 형태의 배양 용기

(1) 미생물 투입
좌측 하단 (r1,c1), 우측 상단 (r2,c2) 직사각형 영역 미생물 투입
-> 새로 투입된 미생물이 우선적으로 살아 남음 (인덱스 1 ~ n)
-> 미생물 무리가 다른 무리에 의해 차지한 영역이 둘 이상으로 나눠지면, 해당 무리는 배양 용기에서 사라짐
    (BFS로 영역 체크)

(2) 배양 용기 이동
모든 미생물을 새로운 배양용기로 이동 (크기 동일)
기존 배양 용기에 있는 무리 중 가장 차지한 영역이 넓은 무리를 하나 선택, 
무리가 둘 이상이라면 가장 먼저 투입된 미생물 선택 -> (인덱스가 가장 낮은)
기존 용기에서의 형태를 유지하되, 미생물 무리가 차지한 영역이 배양 용기의 범위를 벗어나면 X
다른 미생물의 영역과 겹치면 X, 최대한 x좌표, y좌표가 낮은 곳으로 오도록 옮김
-> 어떤 곳에도 둘 수 없는 미생물 무리가 있으면 해당 미생물은 옮겨지지 않고 사라진다.

(3) 실험 결과 기록
상하좌우로 맞닿은 면이 있는 무리는 '인접한 무리'
모든 '인접한 무리' 쌍 확인
쌍을 이루는 A,B가 있다면 A의 넓이 X B의 넓이 = 성과
모든 쌍의 성과를 더한 값이 실험의 결과이다.

"""
import sys
from collections import deque
input = sys.stdin.readline

n,q = [int(i) for i in input().split()]
data = [[[0 for _ in range(n)] for __ in range(n)] for ___ in range(q+2)]
check = [[0 for _ in range(n)] for __ in range(n)]
orgs = [[] for _ in range(q+1)]

def orgsInput(idx): # 미생물 투입
    r1,c1,r2,c2 = [int(i) for i in input().split()]
    for i in range(r1, r2):
        for j in range(c1, c2):
            data[idx][i][j] = idx
    orgs[idx] = [-(r2-r1)*(c2-c1),idx,r1,c1,r2,c2] # 넓이, 번호, 좌표

def getRealArea(idx): # 실제 넓이 측정 및 사망 처리
    real = [0 for _ in range(q+1)]
    for i in range(n):
        for j in range(n):
            if data[idx][i][j]:
                real[data[idx][i][j]] += 1
    for i in range(q+1):
        if real[i] > 0 and real[i] != abs(orgs[i][0]): #BFS로 측정한 넓이와 실제 넓이가 다르면?
            clearDeath(idx,i)
            orgs[i].clear() # 정보 말소(사망 처리)
        if real[i] == 0:
            clearDeath(idx,i)
            orgs[i].clear()

def clearDeath(idx,num):
    for i in range(n):
        for j in range(n):
            if data[idx][i][j] == num:
                data[idx][i][j] = 0
    
def updateInfo(idx): # BFS를 활용한 좌하단, 우상단 좌표, 넓이 정보 갱신
    for i in range(n):
        for j in range(n):
            if not check[i][j] and data[idx][i][j]:
                num = data[idx][i][j]
                bfs(idx, num, i, j)
                    
def bfs(idx, num, x, y):
    que = deque([(x,y)]) 
    check[x][y] = 1
    r1,c1,r2,c2 = n, n, 0, 0
    ex = 0
    while len(que) > 0:
        x,y = que.popleft()
        r1,c1,r2,c2 = min(r1, x), min(c1, y), max(r2, x+1), max(c2, y+1)
        ex += 1
        for i, j in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x+i, y+j
            if 0 <= nx < n and 0 <= ny < n and not check[nx][ny] and data[idx][nx][ny] == num:
                que.append((nx,ny))
                check[nx][ny] = 1
                
    orgs[num] = [-ex, num, r1, c1, r2, c2]

def moveToNewData(idx): # 다음 인덱스로 옮기기
    alives = []
    for x in orgs:
        if len(x) > 0:
            alives.append(x)
    alives.sort()
    # print(alives)
    for alive in alives:
        findAreaForAlive(idx, alive)

def findAreaForAlive(idx, alive):
    for i in range(n):
        for j in range(n):
            # if not data[idx][i][j] and findArea(idx,i,j,alive): 이거 하나 때문에 며칠을....
            if findArea(idx,i,j,alive):
                drawOrg(idx, i, j, alive)
                return
    _, num, r1,c1,r2,c2 = alive
    orgs[num] = []
 
def findArea(idx,x,y,alive): # 배치 가능한 영역인지 체크
    _, num, r1, c1, r2, c2 = alive
    wid, hei = r2-r1, c2-c1
    if x+wid > n or y+hei > n:
        return False
    
    for i in range(wid):
        for j in range(hei):
            if data[idx-1][r1+i][c1+j] == num:
                if data[idx][x+i][y+j] and data[idx][x+i][y+j] != num:
                    return False
    return True
                             

def drawOrg(idx, x, y, alive): # 미생물 배치
    _, num, r1, c1, r2, c2 = alive
    # print(alive)
    for i in range(r2-r1):
        for j in range(c2-c1):
            if data[idx-1][r1+i][c1+j] == num:
                data[idx][x+i][y+j] = num
                
def getResult(idx):
    resCheck = [[0 for _ in range(n)] for __ in range(n)]
    duoCheck = [[0 for _ in range(q+1)] for __ in range(q+1)]
    res = 0
    for i in range(n):
        for j in range(n):
            if data[idx][i][j] and not resCheck[i][j]:
                que = deque([(i,j)])
                resCheck[i][j] = 1
                while len(que) > 0:
                    x,y = que.popleft()
                    o = data[idx][x][y]
                    for a,b in [(0,1),(0,-1),(1,0),(-1,0)]:
                        nx,ny = x+a, y+b
                        if 0 <= nx < n and 0 <= ny < n:
                            p = data[idx][nx][ny]
                            if p and o != p and not duoCheck[o][p]:
                                duoCheck[o][p] = 1
                                duoCheck[p][o] = 1
                                res += orgs[o][0] * orgs[p][0]
                            if data[idx][nx][ny] and not resCheck[nx][ny]:
                                que.append((nx,ny))
                                resCheck[nx][ny] = 1
    return res
                
                
def initCheck(): # 방문 초기화
    for i in range(n):
        for j in range(n):
            check[i][j] = 0

def printData(idx, a):
    if idx >= a:        
        for x in data[idx]:
            print(' '.join(map(str,x)))
                    

for i in range(1,q+1):
    initCheck()
    orgsInput(i)
    updateInfo(i)
    getRealArea(i)
    # print("#",i," 미생물 투입")
    # printData(i,26)  
    moveToNewData(i+1)
    initCheck()
    updateInfo(i+1)
    getRealArea(i+1)
    # print("#",i,"미생물 옮기기")
    # printData(i+1,26)
    print(getResult(i+1))