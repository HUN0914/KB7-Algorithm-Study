"""
비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 
그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
"""
import sys
input = sys.stdin.readline

n = int(input())
data = [[int(i) for i in input().split()] for _ in range(n**2)]
classRoom = [[0 for _ in range(n)] for __ in range(n)]
side = [(-1,0),(0,1),(1,0),(0,-1)]

def findSeat(student):
    obj = student[0]
    friends = student[1:]
    candidate = []
    for i in range(n):
        for j in range(n):
            if classRoom[i][j]:
                continue
            candidate.append([0, 0, i, j])
            for a,b in side:
                ni,nj = i+a, j+b
                if 0 <= ni < n and 0 <= nj < n:
                    if classRoom[ni][nj] and classRoom[ni][nj] in friends:
                        candidate[-1][0] -= 1
                    elif not classRoom[ni][nj]:
                        candidate[-1][1] -= 1
    candidate.sort(reverse=True)
    a,b,x,y = candidate.pop()
    classRoom[x][y] = obj

def getResult():
    data.sort()
    answer = 0
    for i in range(n):
        for j in range(n):
            t = 0
            k = classRoom[i][j] - 1
            for a,b in side:
                ni,nj = i+a, j+b
                if 0 <= ni < n and 0 <= nj < n and classRoom[ni][nj] in data[k][1:]:
                    t += 1
            if t > 0:
                answer += 10**(t-1)
    return answer
                    
for stu in data:
    findSeat(stu)

print(getResult())