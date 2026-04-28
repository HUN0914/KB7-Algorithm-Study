#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14890                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: kchun0513 <boj.kr/u/kchun0513>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14890                          #+#        #+#      #+#     #
#    Solved: 2026/04/12 17:28:41 by kchun0513     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n,l = [int(i) for i in input().split()]
data = [[int(i) for i in input().split()] for _ in range(n)]

ans = 0 
for i in range(n):
    temp = 1 # 동일한 높이의 연속된 칸을 집계하는 변수 temp, 처음(인덱스 0) 위치를 포함해야 하므로 1로 초기화
    flag = 2 # i번째 열/행이 지나갈 수 있는 길인지 체크하기 위한 flag
    for j in range(1,n): # 행 체크룡
        if data[i][j]-data[i][j-1] == 0: #평평함!
            temp += 1
        elif data[i][j]-data[i][j-1] == -1: #내려감!
            if temp >= 0: #아직 남아있는 경사로가 없어야 함!
                temp = -l #내리막이기 때문에 지금 이후로 여유 공간이 l만큼 있어야 한다. 따라서 l로 초기화
                temp += 1 #현재 위치도 포함해야 하므로 1 증가
            else: # 어라? 아직 내리막이 안 끝났는데 또 설치하려고 하네?
                flag -= 1 #너는 안된다
                break
        elif data[i][j]-data[i][j-1] == 1: #올라감!
            if temp >= l: #경사로를 놓기 위해 지금부터 이전에 존재하는 잉여 공간이 l만큼 있어야 함!
                temp = 0 #그 뒤로는 영향이 없기 때문에 temp는 0으로 초기화
                temp += 1 #현재 위치도 포함해야 하므로 1 증가
            else: # 어라? 내리막 안 끝났다니까? 
                flag -= 1 # 너도 안된다
                break
        else: # 너무 높아!, 너무 낮아!
            flag -= 1 # 당연히 안된다
            break
        if j == n-1 and temp < 0: # 내리막 경사로 아직 다 못 놓았는데 끝남...
            flag -= 1 # 안타깝게도 안된다
            break

    temp = 1 # 열 방향으로 체크하기 위한 temp 초기화
    for j in range(1,n): # 열 체크용, 로직은 위와 똑같다.
        if data[j][i]-data[j-1][i] == 0:
            temp += 1
        elif data[j][i]-data[j-1][i] == -1:
            if temp >= 0:
                temp = -l
                temp += 1
            else:
                flag -= 1
                break
        elif data[j][i]-data[j-1][i] == 1:
            if temp >= l:
                temp = 0
                temp += 1
            else:
                flag -= 1
                break
        else:
            flag -= 1
            break
        if j == n-1 and temp < 0:
            flag -= 1
            break
    ans += flag # 둘다 됐다면 2, 둘 중 하나가 됐다면 1, 하나도 안 됐다면 0이 더해질 것이다.

print(ans) #결과 출력!
        