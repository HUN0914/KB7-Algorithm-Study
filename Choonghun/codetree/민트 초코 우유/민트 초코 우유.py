"""
n x n 책상 배열
최초에는 민트(T), 초코(C), 우유(M) 중 하나의 음식만을 신봉 => [0,0,0] 2진수로 관리하자 -> 약전파는 각 자리마다 OR연산
민트: 1, 초코 : 2, 우유 : 4
초코우유: 6, 민트우유: 5, 민트초코: 3,
민트초코우유: 7

1. 아침 : 모든 학생의 신앙심 +1
2. 점심 :
    같은 음식을 신봉하는 인접한 학생들이 그룹 형성 => BFS 진행, 진행하면서 대표 선출
        - 대표 선출 기준
        - 신앙심이 제일 큰 사람
        - 같다면 제일 좌상단에 위치한 사람
    대표 선출 후 대표를 제외한 나머지 그룹원은 대표에게 신앙심 1씩 넘김
3. 저녁 :
    단일 음식 (민,초,우) -> 이중 조합 (초우, 민우, 민초) -> 삼중 조합 (민초우)
    동일 그룹 내에서는 대표자의 신앙심이 높은쪽이 먼저 전파 진행
        여기도 신앙심이 같다면 가장 좌상단에 위치한 사람이 먼저 진행
    
    전파자(대표자)는 신앙심 B 중 1만 남기고 나머지를 간절함 x = B - 1로 바꿔 전파에 사용한다. (ex. 신앙심이 24라면 간절함이 23이 되고 신앙심은 1이 된다.)
    전파 방향은 B를 4로 나눈 나머지에 따라 결정된다. 나머지가 0,1,2,3인 경우 각각 순서대로 위, 아래, 왼쪽, 오른쪽 방향으로 전파한다.
    
    전파 대상의 신앙심이 y이고 전파자(대표자)의 간절함이 x일때
    x > y일때 강전파 => 전파자는 간절함이 y+1만큼 깎이고, 전파 대상의 신앙심은 1이 증가한다. 전파자의 간절함이 0이 되면 전파자는 더 이상 전파 X
    x <= y이면 약전파 => 전파자는 간절함이 바로 0이 되고 더 이상 전파를 진행하지 않지만, 대상의 신앙심은 x만큼 증가한다.
    
    다른 대표자로부터 전파를 당했다면 해당 학생은 당일에는 전파를 하지 않는다. 하지만 추가로 전파 받는 것은 가능하다. -> 이게 왜 방어?
"""
import sys
from collections import deque

input = sys.stdin.readline

side = [(-1,0),(1,0),(0,-1),(0,1)] #위 아래 왼쪽 오른쪽
groups_order = [
    [1,2,4], #민트 (1,0,0), 초코 (0,1,0), 우유 (0,0,1)
    [6,5,3], #초코우유 (1,1,0), 민트우유 (1,0,1), 민트초코 (0,1,1)
    [7] #민트초코우유 (1,1,1)
]

groups_president = [[] for _ in range(3)] # 단일, 이중, 삼중 그룹 대표들을 저장하기 위한 이차원 배열
check = [] # BFS용 체크 배열
n,t = 0,0  # 책상 크기, 기간
table = [] # 책상
info = [] # 각 인원별 신앙심 정보

def bfs(x,y): # 멤버 리스트 정리 및 대표자 선출을 위한 BFS
    que = deque([(x,y)])
    typeId = table[x][y] # 현재 영역의 신앙
    check[x][y] = 1 
    typeNumber = binTodec(table[x][y]) # 이진수로 된 신앙을 십진수로 변환
    members = [(x,y)] #현재 영역의 구성원
    president = [info[x][y], x, y] # 현재 대표
    while len(que) > 0:
        x,y = que.popleft()
        for i, j in side:
            nx,ny = x+i, y+j
            if 0 <= nx < n and 0 <= ny < n and typeId == table[nx][ny] and not check[nx][ny]:
                if president[0] < info[nx][ny]: # 해당 인원의 신앙심이 현재 대표의 신앙심보다 높다면
                    president = [info[nx][ny], nx, ny] # 교체
                elif president[0] == info[nx][ny]: # 신앙심이 같다면?
                    if nx < president[1]: # 해당 인원의 행이 현재 대표보다 높이 위치
                        president = [info[nx][ny], nx, ny] # 교체
                    elif nx == president[1] and ny < president[2]: # 해당 인원의 열이 현재 대표보다 좌측에 위치
                        president = [info[nx][ny], nx, ny] # 교체
                check[nx][ny] = 1
                members.append((nx,ny)) # 구성원 추가
                que.append((nx,ny))
    # print(president)
    for x,y in members: # 구성원을 순회하며
        if president[1] != x or president[2] != y: #대표가 아닌 인원이면
            info[x][y] -= 1 # 당신의 신앙심을
            president[0] += 1 # 여러분의 대표에게
            info[president[1]][president[2]] += 1 # 바치세용!
    president[1], president[2] = -president[1], -president[2] # 대표의 좌표는 음수로 바꿔서 삽입
    
    """
        음수로 삽입하는 이유는 night() 메서드 참고
    """

    for i in range(len(groups_order)):
        if typeNumber in groups_order[i]: # 해당 신앙이 속한 대표 그룹에 삽입
            groups_president[i].append(president)
            break
    

def getData(): #데이터 입력
    global table, info, n, t, check
    n,t = [int(i) for i in input().split()]
    for i in range(n): # 책상 인원 입력
        table.append([])
        for x in input().rstrip():
            if x == 'T':  # 민트는 1
                table[i].append([1,0,0])
            elif x == 'C': # 초코는 2
                table[i].append([0,1,0])
            elif x == 'M': # 우유는 4
                table[i].append([0,0,1])
    
    for i in range(n): # 인원별 신앙심 입력
        info.append([int(j) for j in input().split()])

def init(): # check 초기화
    global check
    check = [[0 for _ in range(n)] for __ in range(n)]
                
def morning():
    for i in range(n):
        for j in range(n):
            info[i][j] += 1
            
def afternoon(): # 오후에는 순회하면서 BFS를 활용한 영역체크 + 대표 선출
    for i in range(n):
        for j in range(n):
            if not check[i][j]: # 체크가 안된 영역이면
                bfs(i,j) # BFS 진행
    

def night(): # 밤이 되었습니다.
    for i in range(3):
        # sort를 할때 좌표를 음수로 했기에 신앙심이 높을수록 뒤로, 
        # (양수 기준) x좌표, y좌표가 0에 가까울수록 뒤로 간다.
        groups_president[i].sort() 
        while groups_president[i]:
            spread(groups_president[i].pop())
                
def getResult(): # 한 번 쭉 돌면서 각 신앙별 인원 체크
    res = [0 for _ in range(8)]
    for i in range(n):
        for j in range(n):
            res[binTodec(table[i][j])] += info[i][j] 

    # 민트초코우유, 민트초코, 민트우유, 초코우유, 우유, 초코, 민트
    result = [res[7],res[3],res[5],res[6],res[4],res[2],res[1]] 
    return ' '.join(map(str,result))

def binTodec(bin): # 이진수를 십진수로 
    return sum([bin[i]* 2**i for i in range(3)])

def spread(presi): #전파
    B, x, y = presi
    x,y = -x,-y # 좌표가 음수로 되어 있기 때문에 반드시 변환해줘야 한다.
    if B != info[x][y]: #해당 대표가 이미 전파를 받았다면 신앙심이 바뀌었을것
        return
    i,j = side[info[x][y] % 4] # 방향
    nx,ny = x+i, y+j # 첫 번째 손님
    ganjeol = B - 1 # 간절함
    info[x][y] = 1 # 대표의 신앙심은 1로
    while 0 <= nx < n and 0 <= ny < n and ganjeol > 0: # 범위 바깥으로 나가거나 간절함이 0 이하면 정지
        # printBoard()
        # printState()   
        if table[nx][ny] != table[x][y]: #둘이 좋아하는게 다르네?
            # print(ganjeol, info[nx][ny])
            if ganjeol > info[nx][ny]: 
                # print("from",(x,y),"to",(nx,ny),"강전파!")
                info[nx][ny] += 1 # 피전파자는 1 증가
                ganjeol -= info[nx][ny] # 전파자는 피전파자의 현재 신앙심만큼 간절함 감소
                table[nx][ny] = strongSpread(table[x][y], table[nx][ny]) # 강전파
            else: 
                # print("from",(x,y),"to",(nx,ny),"약전파!")
                info[nx][ny] += ganjeol # 피전파자는 전파자의 잔여 간절함만큼 신앙심 증가
                ganjeol = 0 # 간절함 고갈!
                table[nx][ny] = weakSpread(table[x][y], table[nx][ny]) # 약전파
        nx,ny = nx+i, ny+j # 다음 순서로 이동
                
    

def weakSpread(a,b): #a에서 b로 약전파
    return [a[i] or b[i] for i in range(3)] # 각 인덱스별로 or 연산 진행

def strongSpread(a,b): #a에서 b로 강전파
    return [a[i] for i in range(3)] # 전파자의 신앙을 그대로 반환

def printBoard(): # 디버깅용 보드 print
    for x in table:
        print(x)
        
def printState(): # 디버깅용 신앙심 print
    for x in info:
        print(x)

getData()
for _ in range(t):
    init() # check 초기화
    morning() #아침
    afternoon() #오후
    night() #저녁
    print(getResult()) #현재 인원 반환