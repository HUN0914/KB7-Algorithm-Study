#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9079                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: kchun0513 <boj.kr/u/kchun0513>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9079                           #+#        #+#      #+#     #
#    Solved: 2026/04/09 23:58:43 by kchun0513     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
input = sys.stdin.readline

#뒤집는 방식은 3개의 행 3개의 열 2개의 대각선
types = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
# 2진수를 10진수로
def binToDec(bin):
    return sum([2**i * int(bin[i]) for i in range(8)])
        
# 테스트 케이스 개수
t = int(input())
for _ in range(t):
    data = []
    check = [0] * 2**8 #뒤집는 방식 체크
    for __ in range(3): #T를 1로 H를 0으로 치환
        data.append([1 if x == 'T' else 0 for x in input().rstrip().split()])
    q = deque(['00000000']) #처음은 하나도 안 뒤집은 것부터
    check[0] = 1
    flag = 1
    while len(q) > 0:
        cur = q.popleft() #큐이므로 왼쪽부터 pop
        """ 
         여기부터 전체 동일 여부 체크 코드
        """
        flips = [0]*9 
        for i in range(8):
            if cur[i] == '1':
                for a in types[i]:
                    flips[a] += 1 #각 동전별로 뒤집힌 횟수 집계

        flag = 1 # 종료 플래그 설정
        for i in range(9): #뒤집힌 횟수와 최초의 수를 합산하여 직전 값과 비교
            if i > 0 and (data[(i-1)//3][(i-1)%3] + flips[i-1]) % 2 != (data[i//3][i%3] + flips[i]) % 2:
                flag = 0 # 다르면 정답이 아니므로 flag 0
                break

        if flag: # 모두 통과했으면 플래그가 1이므로 정답 출력
            print(sum([int(i) for i in cur]))
            break
                
        for i in range(8): # cur에 대하여 각 경우의 수 체크
            n_cur = cur[:i] + '1' + cur[i+1:] # 문자열 슬라이싱을 통해 하나를 1로 전환
            n_cur_dec = binToDec(n_cur) # 10진수로 전환해서
            if not check[n_cur_dec]: # 방문하지 않은 경우라면 큐에 푸시
                check[n_cur_dec] = 1
                q.append(n_cur)
                
    if not flag: # 끝까지 정답이 안 나왔다면 flag는 0이므로 -1 출력
        print(-1)