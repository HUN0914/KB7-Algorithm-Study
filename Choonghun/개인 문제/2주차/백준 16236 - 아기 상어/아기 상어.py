#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16236                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: kchun0513 <boj.kr/u/kchun0513>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16236                          #+#        #+#      #+#     #
#    Solved: 2026/04/14 00:28:30 by kchun0513     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
import heapq as hq
from collections import deque
input = sys.stdin.readline
"""
    BFS + 우선순위 큐 문제이다.
"""
n = int(input())
data = [[int(i) for i in input().split()] for _ in range(n)]
q = []

#아기 상어의 현재 위치 가져오기
x,y = 0, 0
for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            x,y = i,j
            data[i][j] = 0
            
def bfs(st): #BFS
    check = [[0 for _ in range(n)] for __ in range(n)]
    que = deque([(st,0)])
    check[st[0]][st[1]] = 1
    eatable = []
    while len(que) > 0:
        cur, t = que.popleft()
        x,y = cur
        for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx,ny = x+i, y+j #방문 가능 여부 체크
            if 0 <= nx < n and 0 <= ny < n and not check[nx][ny] and data[nx][ny] <= shark:
                que.append(((nx,ny), t+1))
                check[nx][ny] = 1
                if 0 < data[nx][ny] < shark: # 상어보다 작은 물고기는 식사 후보
                    hq.heappush(eatable, (t+1,nx,ny))
    return eatable

shark = 2 # 현재 상어 크기
feed = 0 # 상어가 지금까지 잡순 물고기 양
ans = 0 # 정답
while True:
    q = []
    eatables = bfs((x,y)) #BFS로 먹을 수 있는 물고기들을 우선순위 큐로 받는다.
    if len(eatables) == 0: #먹을 수 있는게 없으면 엄마를 불러야 한다.
        break
    dist, fx, fy = hq.heappop(eatables) #1순위 친구를 불러온다
    data[fx][fy] = 0 #먹었음 처리를 해준다.
    feed += 1 #하나 잡솼고
    ans += dist #거리 더해주고
    
    if feed == shark: #크기 만큼 먹었으면 레벨 올라가고
        shark += 1
        feed = 0
    
    x,y = fx,fy #상어 위치 갱신
print(ans)
