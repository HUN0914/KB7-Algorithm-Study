"""
체스판 L x L
빈칸 0 / 함정 1 / 벽 2

기사 위치 기준 좌상단 (r,c) 높이 h, 너비 w => (r,c) ~ (r+h, c+w)
체력 k

(1) 기사 이동 -> 상하좌우 [(-1,0),(0,1),(1,0),(0,-1)]
            -> 옆에 또 다른 기사가 있다면 연쇄적으로 이동
            -> 맨 끝이 벽에 부딪히면 모두 정지
            -> 죽은거 반드시 체크ㅡㅡㅡㅡㅡ!!!!
            
(2) 대결 데미지 -> 다른 기사를 밀치면 밀려난 기사들은 데미지를 입는다.
                -> 기사가 이동한 곳의 범위 내에 있는 함정의 수만큼 피해 적용
                
                
기사 기준 위치, 체력은 따로 관리 => List<knights>
밀쳐지는 것 관리 -> 재귀 적용 (BFS) 이동하는 방향의 1칸 범위를 탐색 후 충돌한
                    기사들을 리스트에 넣고, 리스트를 순서대로 넣고
                    충돌이 없을때까지 반복하는데 끝에 벽이 있다면 취소
                    BFS로 해야할듯, 맨 끝에 벽을 만나면 취소해야 함
맵 관리 : 맨 바깥은 전부 벽으로 하고, 함정 맵이랑 기사 맵 따로 관리
"""
from collections import deque


game = [] # 게임 맵 상태 (함정이랑 벽만)
states = [] # 현재 기사들 영역 상태
L,N,Q = 0,0,0 # 맵 크기, 기사 수, 명령 수
knights = [] # 기사 목록
check = [] # check
orders = [] # 명령 목록
side = [(-1,0),(0,1),(1,0),(0,-1)]

def getData(): #데이터 입력
    global L, N, Q, game, states, knights, check, damage
    L,N,Q = [int(i) for i in input().split()] # 맵 크기, 기사 수, 명령 수
    game = [[2 for _ in range(L+2)] for __ in range(L+2)] # 함정+벽 맵
    states = [[0 for _ in range(L+2)] for __ in range(L+2)] # 기사 맵
    knights = [[] for _ in range(N+1)] # 기사 정보
    damage = [0 for _ in range(N+1)] # 데미지 저장용
    check = [0 for _ in range(N+1)] # check
    for i in range(1,L+1): # 맵 정보 가져오기
        temp = [int(j) for j in input().split()]
        for z in range(1, L+1):
            game[i][z] = temp[z-1]
    
    for i in range(1,N+1):
        knights[i] = [int(j) for j in input().split()] + [0] # 기사 정보, 데미지

    for _ in range(Q): # 명령 입력
        orders.append([int(i) for i in input().split()])
    
    for i in range(1, N+1): # 최초 드로잉
        r,c,h,w,k,d = knights[i]
        for x in range(r,r+h):
            for y in range(c, c+w):
                states[x][y] = i

def checkMove(ind, num): # 방향 인덱스, 기사 번호
    if knights[num][4]-knights[num][5] <= 0: # 명령 받은 기사가 죽었으면 바로 False
        return False
    que = deque([num])
    check[num] = 1
    a,b = side[ind]
    while len(que) > 0: # BFS 진행
        cur = que.popleft()
        r, c, h, w, k, d = knights[cur]
        if ind == 0: # 위쪽!
            for i in range(c, c+w):
                if game[r+a][i] == 2: #벽을 만났다면 밀릴 수가 없으므로 False 반환
                    return False
                elif states[r+a][i] and not check[states[r+a][i]]: # 이동하는 위치에 다른 기사가 있고 방문하지 않았다면 방문 처리 후 큐에 삽입
                    check[states[r+a][i]] = 1
                    que.append(states[r+a][i])
        elif ind == 1: # 오른쪽!
            for i in range(r, r+h):
                if game[i][c+w] == 2:
                    return False
                elif states[i][c+w] and not check[states[i][c+w]]:
                    check[states[i][c+w]] = 1
                    que.append(states[i][c+w])
        elif ind == 2: # 아래쪽!
            for i in range(c, c+w):
                if game[r+h][i] == 2: 
                    return False
                elif states[r+h][i] and not check[states[r+h][i]]:
                    check[states[r+h][i]] = 1
                    que.append(states[r+h][i])
        elif ind == 3: # 왼쪽!
            for i in range(r, r+h):
                if game[i][c+b] == 2: 
                    return False
                elif states[i][c+b] and not check[states[i][c+b]]:
                    check[states[i][c+b]] = 1
                    que.append(states[i][c+b])
    return True # 정상 수행시 True 반환

def eraseKnights(): # 기사 지우기
    for i in range(1, N+1):
        if check[i]: # 명령에 영향을 받은 모든 기사들 위치 갱신 전 states에서 지우기
            eraseKnight(i)

def eraseKnight(ind): # 단일 기사 지우기
    r,c,h,w,k,d = knights[ind]
    for x in range(r,r+h):
        for y in range(c, c+w):
            states[x][y] = 0

def drawKnights(): # 기사 그리기
    for i in range(1, N+1):
        if check[i]: # 명령에 영향을 받은 모든 기사들 위치 반영해서 그리기
            drawKnight(i)

def drawKnight(ind): # 단일 기사 그리기
    r,c,h,w,k,d = knights[ind]
    for x in range(r,r+h):
        for y in range(c, c+w):
            states[x][y] = ind


def initCheck(): # 방문 배열 초기화
    for i in range(N+1):
        check[i] = 0

def refreshKnightInfo(ind): # 기사 위치 정보 수정
    a,b = side[ind]
    for i in range(1,N+1):
        if check[i]:
            knights[i][0] += a
            knights[i][1] += b

def refreshDamageInfo(ind): # 기사 번호
    for i in range(1,N+1):
        if check[i] and ind != i:
            r,c,h,w,k,d = knights[i]
            for x in range(r,r+h): # 현재 영역에 함정이 있는지 체크
                for y in range(c,c+w):
                    if game[x][y] == 1: # 있다면 데미지 누적
                        knights[i][5] += 1
            # knights[i][5] += damage[i]
            if knights[i][4] - knights[i][5] <= 0: # 죽었다면 states에서 지우기 => 이제 감지 불가
                eraseKnight(i)

def getResult():
    res = 0
    for i in range(1,N+1):
        if knights[i][4] - knights[i][5] > 0: # 살아있는 기사들만 데미지 합산
            res += knights[i][5]
    return res

def printBoard(i): # 디버깅용
    print("#", i)
    for x in states:
        print(' '.join(map(str,x)))

getData() # 정보 입력

for kni, way in orders:
    if checkMove(way, kni): # 명령 수행 가능여부 체크
        eraseKnights() # 수행 가능한 명령이라면 현재 영향을 받은 모든 기사들은 check에서 참조해서 지우고
        refreshKnightInfo(way) # 위치 정보를 갱신 후
        drawKnights() # 갱신된 정보를 토대로 다시 그리기
        refreshDamageInfo(kni) # 명령을 받은 kni를 제외한 밀쳐진 기사들 영역 내 함정 개수만큼 데미지 적용 후 게임판에서 제거
    initCheck() # 방문 배열 초기화

# print(knights)
print(getResult()) #정답 출력
