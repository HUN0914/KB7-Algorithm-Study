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
from collections import deque
n,k = [i for i in input().split()]
k = int(k)
n = list(n)
check = [[0,0] for _ in range(1000001)] # 방문 노드, 짝수/홀수 횟수로 나누어 저장
q = deque([(n,0)]) # 큐
x = int(''.join(n)) # 첫 value 정수 변환
check[x][0] = 1 # 첫 value는 방문처리 0번 교환이므로 짝수 방문처리
m = len(n) # 자리수
res0 = x # 첫 value는 0번 교환이므로 결과값을 x로 초기화
res1 = -1 # 홀수 횟수는 -1로
flag = 0 # 교환 발생 여부 체크를 위한 flag
while len(q) > 0:   # 큐에 아이템이 있는 동안 진행
    cur, t = q.popleft() # 큐 pop
    if t == k: # t가 k에 도달하면 continue
        continue
    
    for i in range(m-1):    #모든 교환의 경우의 수를 이중 반복문으로 확인
        for j in range(i+1, m):
            cur[i], cur[j] = cur[j], cur[i] # 교환
            x = int(''.join(cur)) # 정수 변환
            if x >= 10**(m-1) and not check[x][(t+1)%2]: # 첫자리가 0이 아니고 방문한 경우가 아닌 경우에만
                flag = 1 # 플래그
                q.append((list(cur),t+1)) # 큐에 추가
                if (t+1) % 2: # 짝수의 경우
                    res1 = max(res1, x)
                else: # 홀수의 경우
                    res0 = max(res0, x) 
                check[x][(t+1)%2] = 1 # 방문 체크
            cur[i], cur[j] = cur[j], cur[i] # 다시 원래대로 복구

# print(res1, res0)
if flag: # 플래그
    print(res1 if k % 2 else res0) # k가 홀수면 res1, 짝수면 res0 반환
else: # 플래그가 꺼져있다 = 교환이 안 일어남
    print(-1) # -1 출력