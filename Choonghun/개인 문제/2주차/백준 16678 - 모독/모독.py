#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16678                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: kchun0513 <boj.kr/u/kchun0513>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16678                          #+#        #+#      #+#     #
#    Solved: 2026/04/11 00:22:29 by kchun0513     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
"""
1부터 시작하는 연속된 수의 집합을 만들어야 한다.
"""
score = [0] * n
data.sort()
r = 1
for i in range(n):
    if r <= data[i]:
        score[i] = data[i] - r
        r += 1
print(sum(score))
# print(data)
