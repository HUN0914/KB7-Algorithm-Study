#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1039                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: kchun0513 <boj.kr/u/kchun0513>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1039                           #+#        #+#      #+#     #
#    Solved: 2026/04/11 02:45:50 by kchun0513     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import heapq as hq

n = int(input())
data = [input() for _ in range(n)]
st = (-1,-1)
ed = (-1,-1)
for i in range(n):
    for j in range(n):
        if data[i][j] == '#': 
            if st == (-1,-1):
                st = (i,j)
            else:
                ed = (i,j)

side = [(-1,0),(1,0),(0,-1),(0,1)]
check = [[[0]*2500 for __ in range(n)] for _ in range(n)]
q = []
for i in range(4):
    hq.heappush(q, (0, i, st[0], st[1]))
    
while len(q) > 0:
    mir, s, x, y = hq.heappop(q)
    if (x,y) == ed:
        print(mir)
        break
    # print((mir,s,x,y), q)
    if data[x][y] == '!':
        for i in range(4):
            a,b = side[i]
            nx,ny = x+a, y+b
            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] != '*' :
                    if i == s and not check[nx][ny][mir]:
                        hq.heappush(q, (mir, s, nx, ny))
                        check[nx][ny][mir] = 1
                    elif s // 2 != i // 2 and not check[nx][ny][mir+1]:
                        hq.heappush(q, (mir+1, i, nx, ny))
                        check[nx][ny][i] = 1
    else:
        a,b = side[s]
        nx,ny = x+a, y+b
        if 0 <= nx < n and 0 <= ny < n and data[nx][ny] != '*' and not check[nx][ny][mir]:
            hq.heappush(q, (mir, s, nx, ny))
            check[nx][ny][mir] = 1
                    
                    
    
                
                    