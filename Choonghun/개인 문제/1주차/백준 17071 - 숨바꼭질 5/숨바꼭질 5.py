#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17071                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: kchun0513 <boj.kr/u/kchun0513>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17071                          #+#        #+#      #+#     #
#    Solved: 2026/04/08 04:26:56 by kchun0513     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque

data = [[10e9, 10e9] for _ in range(500001)] # 짝수 횟수 / 홀수 횟수
n,k = [int(i) for i in input().split()]
q = deque([n]) #큐
i = 0
data[n][0] = 0
res = -1
while len(q) > 0: #수빈이가 각 지점을 지나가는 시점을 구하기 위한 BFS 진행
    temp = len(q)
    i += 1  
    for _ in range(temp):
        x = q.popleft()
        # print(x, q)
        if x+1 <= 500000 and data[x+1][i%2] >= 10e9: # 1칸 앞으로
            data[x+1][i%2] = i
            q.append(x+1)
        if x-1 >= 0 and data[x-1][i%2] >= 10e9: # 1칸 뒤로
            data[x-1][i%2] = i
            q.append(x-1)
        if x*2 <= 500000 and data[2*x][i%2] >= 10e9: # 2배 앞으로
            data[2*x][i%2] = i
            q.append(2*x)
"""
수빈이가 먼저 가면 와리가리 치면서 대기가 가능하다 
그렇다면 2초 간격으로 대기를 하게 되는데 
짝수+2는 계속 짝수, 홀수+2는 계속 홀수기 때문에 
수빈이와 동생이 방문한 시간이 홀짝이 다르다면 만날 수가 없다. 
따라서 홀수 / 짝수 시간에 각각 가장 빨리 도착한 경우를 각각 저장해놓아야 한다.
"""
i = 0
while k <= 500000:
    if data[k][i%2] <= i:
        res = i
        break
    i += 1
    k += i

print(res)