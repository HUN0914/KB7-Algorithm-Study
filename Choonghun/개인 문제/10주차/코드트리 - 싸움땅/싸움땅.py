side = [(-1,0),(0,1),(1,0),(0,-1)]

# 데이터 받기
n,m,k = [int(i) for i in input().split()]
data = [[[int(i)] if int(i) else [] for i in input().split()] for _ in range(n)]
playerLoc = [[0 for _ in range(n)] for __ in range(n)]
points = [0 for _ in range(m+1)]
player = [[]]

for p in range(1,m+1):
    player.append([int(i) for i in input().split()] + [0])
    player[-1][0] -= 1
    player[-1][1] -= 1
    x,y,d,s,g = player[-1]
    playerLoc[x][y] = p

def movePlayer(idx): # 플레이어 움직이기
    x,y,d,s,g = player[idx]
    i,j = side[d]
    nx,ny = x+i, y+j 
    playerLoc[x][y] = 0 # 현재 위치 초기화
    if not (0 <= nx < n and 0 <= ny < n): # 맵 밖으로 나가면 반대로 방향 전환후 1보 전진
        d = (d+2)%4
        i,j = side[d]
        nx,ny = x+i, y+j
    player[idx][0], player[idx][1], player[idx][2] = nx,ny,d # 위치 갱신
    # print(nx,ny)
    if playerLoc[nx][ny]: # 만약 다른 플레이어가 있다면
        oppo = playerLoc[nx][ny]
        win = playerBattle(idx, oppo) # 한판 뜨고
        player[win][0], player[win][1] = nx,ny # 이긴 사람이 이 자리를 차지한다.
        playerLoc[nx][ny] = win
        dropWeapon(win) # 무기 버리고
        getWeapon(win) # 다시 줍기!
    else:
        playerLoc[nx][ny] = idx # 다른 플레이어가 없다면
        dropWeapon(idx) # 그냥 버리고
        getWeapon(idx) # 줍기

def moveLosePlayer(idx): # 패배한 플레이어 움직이기
    x,y,d,s,g = player[idx]
    i,j = side[d]
    nx,ny = x+i, y+j
    playerLoc[x][y] = 0
    dropWeapon(idx) # 지금 자리에 무기 놓고
    while not (0 <= nx < n and 0 <= ny < n and not playerLoc[nx][ny]):
        d = (d+1)%4 # 오른쪽으로 90도씩 회전)
        i,j = side[d]
        nx,ny = x+i, y+j
    playerLoc[nx][ny] = idx # 위치 갱신
    player[idx][0], player[idx][1], player[idx][2] = nx,ny,d
    getWeapon(idx) # 무기 줍기

def dropWeapon(idx): # 무기 버리기
    x,y,d,s,g = player[idx]
    player[idx][-1] = 0
    if g:
        data[x][y].append(g)
        data[x][y].sort()

def getWeapon(idx): # 무기 줍기
    x,y,d,s,g = player[idx]
    if data[x][y]:
        player[idx][-1] = data[x][y].pop()

def playerBattle(red, blue): 
    rx,ry,rd,rs,rg = player[red]
    bx,by,bd,bs,bg = player[blue]
    if rs + rg > bs + bg: # 레드가 이긴 경우
        points[red] += (rs+rg) - (bs+bg)
        moveLosePlayer(blue)
        return red
    elif rs + rg < bs + bg: # 블루가 이긴 경우
        points[blue] += (bs+bg) - (rs+rg)
        moveLosePlayer(red)
        return blue
    else: # 동점일때
        if rs > bs: # 초기 능력치 비교해서 레드가 이긴 경우
            points[red] += (rs+rg) - (bs+bg)
            moveLosePlayer(blue)
            return red
        else: # 블루가 이긴 경우
            points[blue] += (bs+bg) - (rs+rg)
            moveLosePlayer(red)
            return blue

def printLocation():
    for line in playerLoc:
        print(' '.join(map(str, line)))
    for gun in data:
        print(gun)

for _ in range(k):
    for i in range(1,m+1):
        movePlayer(i) # 플레이어 움직이기

print(' '.join(map(str,points[1:]))) #결과 출력