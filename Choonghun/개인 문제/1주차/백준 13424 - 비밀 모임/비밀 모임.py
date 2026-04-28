#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13424                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: kchun0513 <boj.kr/u/kchun0513>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13424                          #+#        #+#      #+#     #
#    Solved: 2026/04/06 17:48:08 by kchun0513     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m = [int(i) for i in input().split()]
    floyd = [[10e9 if i != j else 0 for j in range(n+1)] for i in range(n+1)] #이동거리 배열
    for __ in range(m): #그래프 입력
        x,y,s = [int(i) for i in input().split()]
        floyd[x][y] = s
        floyd[y][x] = s
    for i in range(1,n+1): #플로이드 워셜 알고리즘
        for j in range(1,n+1):
            for k in range(1,n+1): #각 방에서 다른 방으로 가는 최소 거리를 계산
                floyd[j][k] = min(floyd[j][k], floyd[j][i] + floyd[i][k])
    k = int(input())
    friends = [int(i) for i in input().split()]
    res = float("inf") #최단 거리
    ans = 101 #결과값(방 번호)
    for i in range(1,n+1): #모든 방 번호에 대하여
        temp = sum([floyd[f][i] for f in friends]) #친구들이 있는 방에서 각 방에 대한 총 이동 거리
        if temp < res: #현재 최단 거리보다 작으면 갱신
            res = temp
            ans = i
        elif temp == res: #현재 최단 거리랑 같은데
            if ans > i: #방 번호가 더 작으면?
                ans = i #갱신!
    print(ans)
    
    