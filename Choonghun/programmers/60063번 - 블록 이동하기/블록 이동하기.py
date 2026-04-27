from collections import deque
def solution(board):
    n = len(board)
    side = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)] # 회전순서 (반시계 방향)
    que = deque([(0,0,6,0,1,2,0)]) #첫번째축 위치(x1,y1) 및 바라보는 방향 (s1) 두번째축 위치(x2,y2) 및 바라보는 방향 (s2)
    check = [[[0,0,0,0] for _ in range(n)] for __ in range(n)] # 축이 다른 축을 바라보는 방향을 visited로 삼는다.
    check[0][0][3] = 1 #처음에는 0,0에서 0,1을 바라보므로 (0,0,3) 을 방문처리
    check[0][1][1] = 1 #0,1에서 0,0을 바라보므로 (0,1,1) 방문처리
    while len(que) > 0:
        x1,y1,s1, x2,y2,s2, t = que.popleft()
        # print(t, "일 차")
        # for k in check:
        #     print(k)
        if x1 == y1 == n-1 or x2 == y2 == n-1: # 도착했으면 끝
            return t
        
        for k in range(0, 8, 2): # 평행이동 (모든 방향으로 평행이동 가능)
            i,j = side[k]
            nx1,ny1,nx2,ny2 = x1+i, y1+j, x2+i, y2+j
            if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n and not board[nx1][ny1]+board[nx2][ny2] and not check[nx1][ny1][s1//2]:
                que.append((nx1,ny1,s1,nx2,ny2,s2,t+1))
                check[nx1][ny1][s1//2] = t+1
                check[nx2][ny2][s2//2] = t+1
            
        next_s1 = s1+1 if s1 < 7 else 0  # 1번째 축 기준 역방향 회전
        for _ in range(2): 
            i,j = side[next_s1] 
            nx2,ny2 = x1+i, y1+j
            if 0 <= nx2 < n and 0 <= ny2 < n: # 격자 밖으로 나가면 X
                if board[nx2][ny2]: # 벽으로 막혀 있으면 X
                    break
                if not next_s1 % 2 and not check[x1][y1][next_s1//2]: #visited 체크를 위해서는 몫을 인덱스로 넣어야 한다.
                    que.append((x1,y1,next_s1, nx2,ny2,(next_s1+4)%8, t+1)) # (next_s1+4)%8은 마주보는 방향이다 (0,1)<=>(0,-1) / (1,0)<=>(-1,0)
                    check[x1][y1][next_s1//2] = t+1 
                    check[nx2][ny2][((next_s1+4)%8)//2] = t+1
            else:
                break
            next_s1 = next_s1 + 1 if next_s1 < 7 else 0
        
        next_s1 = s1-1 if s1 > 0 else 7  # 1번째 축 기준 순방향 회전, 로직은 위와 동일
        for _ in range(2):
            i,j = side[next_s1]
            nx2,ny2 = x1+i, y1+j
            if 0 <= nx2 < n and 0 <= ny2 < n:
                if board[nx2][ny2]:
                    break
                if not next_s1 % 2 and not check[x1][y1][next_s1//2]:
                    que.append((x1,y1,next_s1, nx2,ny2,(next_s1+4)%8, t+1))
                    check[x1][y1][next_s1//2] = t+1
                    check[nx2][ny2][((next_s1+4)%8)//2] = t+1
            else:
                break
            next_s1 = next_s1 - 1 if next_s1 > 0 else 7
        
        next_s2 = s2+1 if s2 < 7 else 0  # 2번째 축 기준 역방향 회전, 로직은 위와 동일
        for _ in range(2):
            i,j = side[next_s2]
            nx1,ny1 = x2+i, y2+j
            if 0 <= nx1 < n and 0 <= ny1 < n:
                if board[nx1][ny1]:
                    break
                if not next_s2 % 2 and not check[x2][y2][next_s2//2]:
                    que.append((nx1,ny1,(next_s2+4)%8, x2,y2,next_s2, t+1))
                    check[nx1][ny1][((next_s2+4)%8)//2] = t+1
                    check[x2][y2][next_s2//2] = t+1
            else:
                break
            next_s2 = next_s2 + 1 if next_s2 < 7 else 0
            
        next_s2 = s2-1 if s2 > 0 else 7  # 2번째 축 기준 순방향 회전, 로직은 위와 동일
        for _ in range(2):
            i,j = side[next_s2]
            nx1,ny1 = x2+i, y2+j
            if 0 <= nx1 < n and 0 <= ny1 < n:
                if board[nx1][ny1]:
                    break
                if not next_s2 % 2 and not check[x2][y2][next_s2//2]:
                    que.append((nx1,ny1,(next_s2+4)%8, x2,y2, next_s2, t+1))
                    check[nx1][ny1][((next_s2+4)%8)//2] = t+1
                    check[x2][y2][next_s2//2] = t+1
            else:
                break
            next_s2 = next_s2 - 1 if next_s2 > 0 else 7
        
    answer = 0
    return answer
