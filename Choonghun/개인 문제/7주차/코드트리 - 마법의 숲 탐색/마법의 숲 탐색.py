"""
십자 모양 블록이 떨어지고 (중력 작용)
서쪽으로 구를 수 있으면 서쪽으로 구르고
오른쪽으로 구를 수 있으면 오른쪽으로 구른다.
블록 상태 저장 스택
출구 방향 (0,1,2,3) => (북,동,남,서) 시계 방향
"""
from collections import deque
import sys
input = sys.stdin.readline

side = [(-1,0),(0,1),(1,0),(0,-1)] # 탐색/출구방향
stack = [(-1,-1,-1)] # 골렘 위치, 방향 저장용ㅅ 스택
R,C,K = [int(i) for i in input().split()] # 행, 열, 정령 수
forest = [[0 for _ in range(C+2)] for __ in range(R+4)] # 숲 상태 저장용 배열
visited = [[0 for _ in range(C+2)] for __ in range(R+4)] # BFS용 visited 배열
answer = [0]

for i in range(C+2): # 벽 배치
    forest[R+3][i] = -1
for i in range(R+4):
    forest[i][0] = -1
    forest[i][-1] = -1
# print(forest)
def fallDownGolem(r, c, d): #행, 열, 방향
    if checkDown(r, c): # 바로 내려갈 수 있는가?
        fallDownGolem(r+1, c, d) # 재귀 실행
    elif checkTurnLeft(r, c) and checkDown(r,c-1): # 왼쪽 아래로 구를 수 있는가?
        nd = (d+3)%4 # 왼쪽 회전!
        fallDownGolem(r-1, c-1, nd)
    elif checkTurnRight(r, c) and checkDown(r,c+1): # 우측 아래로 구를 수 있는가?
        nd = (d+1)%4 # 오른쪽 회전!
        fallDownGolem(r-1, c+1, nd) 
    else: # 아예 갈 수가 없으면 위치 적용...
        if r < 4: #근데 골렘 일부가 외부네?
            clearStatus() # 싹 다 정리
        else:
            setGolemPosition(r, c, d) # 숲 내부에 있다면 위치 저장하고
            answer[0] += bfs(r, c) # 현재 상태에서 BFS 진행하여 가장 아래 위치 확인
        return

def setGolemPosition(r, c, d): # 위치 저장
    idx = len(stack)
    stack.append((r,c,d)) # 스택에 위치 저장
    forest[r][c] = idx # Forest 배열에 골렘의 위치 저장
    for i,j in side: 
        forest[r+i][c+j] = idx

def checkDown(r, c): # 아래칸 확인
    return not forest[r+2][c] and not forest[r+1][c-1] and not forest[r+1][c+1]
    
def checkTurnLeft(r, c): # 좌측칸 확인
    return not forest[r+1][c-1] and not forest[r][c-2] and not forest[r-1][c-1]

def checkTurnRight(r, c): # 우측칸 확인
    return not forest[r+1][c+1] and not forest[r][c+2] and not forest[r-1][c+1]

def bfs(r,c):
    que = deque([(r,c)])
    visited = [[0 for _ in range(C+2)] for __ in range(R+4)]
    visited[r][c] = 1
    result = 0
    while len(que):
        r,c = que.popleft() # 현 위치
        idx = forest[r][c] # 골렘 번호
        cX, cY, d = stack[idx] # 해당 골렘의 중심 위치, 방향
        i,j = side[d] 
        ext = (cX+i, cY+j) # 해당 골렘의 출구 방향
        result = max(r,result) # 결과 갱신
        for i, j in side: # 방향
            nr,nc = r+i, c+j # 다음 방향
            if (r,c) == ext and forest[nr][nc] > 0 and not visited[nr][nc]:
                que.append((nr,nc)) # 현재 위치가 출구이고, 다음 방향이 이동 가능한 위치인지
                visited[nr][nc] = 1
            elif (r,c) != ext and forest[nr][nc] == idx and not visited[nr][nc]:
                que.append((nr,nc)) # 현재 위치가 출구가 아니고, 현재 골렘의 내부인지
                visited[nr][nc] = 1
    return result-2

def clearStatus():
    while stack:
        r,c,d = stack.pop()
        if r == c == d == -1:
            continue
        forest[r][c] = 0
        for i,j in side:
            forest[r+i][c+j] = 0
    stack.append((-1,-1,-1))

def printForest():
    for line in forest:
        print(' '.join(map(str,line)))

def getResult():
    for _ in range(K):
        c, d = [int(i) for i in input().split()]
        fallDownGolem(1, c, d)
        # print("#",_)
        # printForest()
    return answer[0]

print(getResult())