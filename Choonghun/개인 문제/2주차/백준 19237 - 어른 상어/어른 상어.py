import sys
from collections import deque
input = sys.stdin.readline

n,m,k = [int(i) for i in input().split()]
sharks = [() for _ in range(m+1)] #상어 현 위치
smells = [deque([]) for _ in range(m+1)] #냄새 큐
data = [[int(i) for i in input().split()] for _ in range(n)] # 보드
temp = [int(i) for i in input().split()] #상어의 최초 방향
side = [(), (-1,0), (1,0), (0,-1), (0,1)] #위 아래 왼쪽 오른쪽
prior = [[[]] for _ in range(m+1)] #우선순위 저장용
time = 0 # 시간

def get_data(): #데이터 입력
    for i in range(n): #상어 현 위치와 방향을 저장하고, 냄새도 각각의 큐에 박아넣는다.
        for j in range(n):
            if data[i][j] > 0:
                sharks[data[i][j]] = (i,j,temp[data[i][j]-1])
                smells[data[i][j]].append((i,j,k))
                data[i][j] = -data[i][j] #현재 상어가 있는 곳은 음수로 표시
                
    for i in range(1,m+1): #방향 우선순위 가져오기
        for j in range(4):
            prior[i].append([int(x) for x in input().split()])

def check_end(): #종료 체크
    return (len(sharks[1]) > 0 and not sum([len(sharks[x]) for x in range(2,m+1)])) or time > 1000 #시간이 1000을 넘었거나 상어 1만 남았다면 끝

def check_available(sh, si, type): #진출 가능 여부 체크, type는 없는거 (0) 그리고 자기 자신의 냄새 (type)
    #sh: 상어 위치, si: 방향
    x,y,_ = sharks[sh]
    i,j = side[si]
    nx,ny = x+i, y+j
    if 0 <= nx < n and 0 <= ny < n:
        if data[nx][ny] == type:
            data[x][y] = -data[x][y] #자신이 있던 자리는 다시 양수로 전환
            sharks[sh] = (nx,ny,si)
            return True
    return False

def push_queue(): #냄새 정보 갱신 후 새로운 자리 큐에 넣기
    for i in range(m,0,-1): #각 상어들에 대해서
        temp = len(smells[i]) #현재 냄새 큐의 길이 체크
        if len(sharks[i]) > 0: #상어가 존재하는지 확인
            sx,sy,u = sharks[i]
        else: # 없으면 -1, -1
            sx,sy = -1, -1
        for _ in range(temp): #현재 시간의 모든 냄새를 체크
            x,y,t = smells[i].popleft() #냄새 위치, 남은 시간
            if sx != x or sy != y: # 현재 상어의 위치와 다른 냄새들은
                if abs(data[x][y]) != i: # 해당 냄새 위치에 다른 상어가 있다면 큐에 다시 안 넣는다.
                    continue
                if t > 1: # 남은 시간이 1을 넘으면 t-1을 하고 다시 큐에 삽입
                    smells[i].append((x,y,t-1))
                else: # 냄새가 사라졌다!
                    data[x][y] = 0
                
        if sx >= 0 and sy >= 0: #상어가 살아있다면
            if data[sx][sy] < 0: #현재 상어가 이동한 위치에 이미 존재하는 상어가 있다면 (어차피 역순으로 봐서 크기 체크 안해도 됨)
                sharks[abs(data[sx][sy])] = () #너는 나가라 ㅋㅋ
            data[sx][sy] = -i #이제 이 자리는 제 겁니다
            smells[i].append((sx,sy,k)) #냄새로 점유까지

def print_board(): #디버깅용 print 코드
    print('#',time)
    print(sharks)
    print(smells)
    for x in data: 
        print(x)

get_data() 
        
while not check_end(): #최종 풀이
    for i in range(1, m+1):
        if len(sharks[i]) == 0: #상어 위치가 비었다면 없는 것이므로 패스
            continue
        shx,shy,shs = sharks[i] # 해당 상어의 현재 위치 (x,y) 그리고 방향
        flag = False # 이동했음을 알리는 플래그
        for j in range(4):
            if flag: # 이동했으면 True이므로 멈춤
                break
            next_side = prior[i][shs][j] #다음 방향
            flag = check_available(i,next_side,0) # 1순위 : 비어있는 곳
        for j in range(4):
            if flag: # 이동했으면 True이므로 멈춤
                break
            next_side = prior[i][shs][j] #다음 방향
            flag = check_available(i,next_side,i) # 2순위 : 자기 자신이 지나간 곳
    push_queue() #
    time += 1

print(time if time <= 1000 else -1)