#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9061                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: kchun0513 <boj.kr/u/kchun0513>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9061                           #+#        #+#      #+#     #
#    Solved: 2026/04/05 18:20:16 by kchun0513     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
"""
X축과 Y축을 기준으로
구간을 2개로 나눈 다음 두 구간에서 가장 바깥에 있는 점들을 기준으로 직사각형의 넓이를 구한다
"""
import sys
input = sys.stdin.readline
t = int(input())
    
def getResult(data):
    if n <= 2:
        return 0
    left_minY = [0] * n #왼쪽 영역에서 구간별 최소 Y
    right_minY = [0] * n #오른쪽 영역에서 구간별 최소 Y
    left_maxY = [0] * n #왼쪽 영역에서 구간별 최대 Y
    right_maxY = [0] * n #오른쪽 영역에서 구간별 최대 Y
    left_minY[0] = data[0][1]
    left_maxY[0] = data[0][1]
    right_minY[-1] = data[-1][1]
    right_maxY[-1] = data[-1][1]
    
    for i in range(1,n): # 왼쪽 영역은 순차적으로 
        left_minY[i] = min(left_minY[i-1], data[i][1])
        left_maxY[i] = max(left_maxY[i-1], data[i][1])

    for i in range(n-2,-1,-1): # 오른쪽 영역은 역순으로
        right_minY[i] = min(right_minY[i+1], data[i][1])
        right_maxY[i] = max(right_maxY[i+1], data[i][1])
    
    
    res = 60000*60000
    for i in range(n-1): #구분선은 점 n개 사이이므로 n-1
        leftD = (data[i][0] - data[0][0]) * (left_maxY[i]-left_minY[i]) #왼쪽 직사각형 넓이
        rightD = (data[-1][0] - data[i+1][0]) * (right_maxY[i+1]-right_minY[i+1]) #오른쪽 직사각형
        res = min(res, max(leftD,rightD)) #결과 갱신
        
    return res
    
for _ in range(t):
    n = int(input())
    dataX = []
    dataY = []
    for __ in range(n):
        x,y = [int(i) for i in input().split()]
        dataX.append((x,y)) # x 기준
        dataY.append((y,x)) # y 기준
        
    dataX.sort() #정렬
    dataY.sort()
    
    print(min(getResult(dataX), getResult(dataY))) #두 기준으로 도출한 결과 중 최솟값 출력
        