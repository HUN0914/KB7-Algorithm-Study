import sys
from collections import deque
input = sys.stdin.readline

side = [(-1,0),(1,0),(0,-1),(0,1)]

# 1. 데이터 받기
N,M,K = [int(i) for i in input().split()]
maze = [[int(i) for i in input().split()] for __ in range(N)] # 미로 정보
loc = [[[] for _ in range(N)] for __ in range(N)] # 참가자 위치 정보
runner = [[]] # 참가자 정보
for j in range(M):
    runner.append([int(i)-1 for i in input().split()])
    loc[runner[-1][0]][runner[-1][1]].append(j+1)
exit = [int(i)-1 for i in input().split()]
maze[exit[0]][exit[1]] = -1
answer = [0]

# 회전 함수
def spinSquare(x1,y1,x2,y2):
    temp = []
    tempR = []
    w,h = y2-y1, x2-x1
    if x1 == y1 == 10e9:
        return
    for i in range(y1, y2): # 나중 행, 처음 열 -> 처음 행, 나중 열 순으로 복사
        temp.append([])
        tempR.append([])
        for _ in range(x2-x1):
            tempR[-1].append([])
        for j in range(x2-1, x1-1, -1):
            temp[-1].append(maze[j][i])
            while loc[j][i]:
                tempR[-1][x2-1-j].append(loc[j][i].pop())

    for i in range(x1,x2): # 그대로 붙여넣기
        for j in range(y1,y2):
            maze[i][j] = temp[i-x1][j-y1]
            while tempR[i-x1][j-y1]: # 같은 곳에 있던 사람들은 지금 위치 바꿔도 상관 X
                idx = tempR[i-x1][j-y1].pop()
                loc[i][j].append(idx)
                runner[idx] = [i,j]
            if maze[i][j] > 0:
                maze[i][j] -= 1
            if maze[i][j] == -1:
                exit[0], exit[1] = i,j
            
# 이동 여부 판별
def moveParticipant():
    flag = False
    moved = [0 for _ in range(M+1)]
    for i in range(1,M+1):
        if not runner[i]:
            continue
        if moved[i]:
            continue
        flag = True
        x,y = runner[i]
        d = abs(exit[0]-x)+abs(exit[1]-y)
        for a,b in side:
            nx,ny = x+a, y+b
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] <= 0:
                nd = abs(exit[0]-nx)+abs(exit[1]-ny)
                if nd < d:
                    temp = []
                    while loc[x][y]: # 한 번에 움직이는데
                        idx = loc[x][y].pop() 
                        if moved[idx]: # 이미 움직였던 사람은 따로 빼놓고
                            temp.append(idx)
                        else: # 움직이지 않은 사람만 이동시킨다.
                            moved[idx] = 1
                            answer[0] += 1
                            if nd:
                                loc[nx][ny].append(idx)
                                runner[idx] = [nx,ny]
                            else:
                                runner[idx].clear()
                    while temp:
                        loc[x][y].append(temp.pop())
                    break
    return flag

# 가장 작은 사각형 찾기
def findMinimumSquare():
    ex,ey = exit
    cands = []
    for a in range(1,M+1):
        if not runner[a]:
            continue
        x,y = runner[a]
        w = max(abs(x-ex)+1, abs(y-ey)+1) # 정사각형 한 변의 길이
        tx,ty = getSquare(x,y,ex,ey,w) #좌상단부터 탈출구와 해당 참가자를 모두 포함하는 정사각형 찾기
        cands.append((w,tx,ty)) # 찾았으면 후보에 추가
    cands.sort() # 정렬해서
    if not cands: # 사각형이 없으면 100,100,100,100 반환
        return [100,100,100,100]
    rw,rx,ry = cands[0] # 최선의 정사각형을 반환
    return [rx,ry,rx+rw,ry+rw]

def getSquare(x,y,ex,ey,w): # 각 참가자별 가장 적합한 사각형 찾기
    for i in range(N-w+1):
        for j in range(N-w+1):
            if i <= x < i+w and j <= y < j+w and i <= ex < i+w and j <= ey < j+w:
                return [i,j]

t = 0
while t < K and moveParticipant():
    x1,y1,x2,y2 = findMinimumSquare()
    if x1==y1==x2==y2==100: # 사각형이 없다면 모두 탈출한 것이므로 break
        break
    spinSquare(x1,y1,x2,y2)
    t += 1
print(answer[0])
print(' '.join(map(str,[i+1 for i in exit])))