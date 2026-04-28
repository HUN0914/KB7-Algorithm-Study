import sys
input = sys.stdin.readline

n = int(input())
data = [[int(i) for i in input().split()] for _ in range(n)]
# 조합 문제이고 결과는 순서가 상관이 없다
res = 10e9
morn = [] # 아침 스택
morn_score = 0
afte = [] # 저녁 스택
afte_score = 0
def backtrack(i):
    global res
    global morn_score
    global afte_score
    if i == n: #index가 n에 도달하면 결과를 도출하고 갱신한다.
        res = min(abs(morn_score-afte_score), res)
        return
    if len(morn) < n//2: # 아침 스택이 n//2보다 적으면 추가하고 재귀 실행, 백트랙이므로 pop 필수
        temp = sum([data[x][i]+data[i][x] for x in morn]) #오전 스택에 들어 있던 값과 현재 들어가는 값에 대한 점수
        morn.append(i)
        morn_score += temp # 더했다가
        backtrack(i+1) # 백트랙하고
        morn.pop()
        morn_score -= temp # pop할때 다시 빼기
    if len(afte) < n//2: # 저녁 스택이 n//2보다 적으면 추가하고 재귀 실행, 백트랙이므로 pop 필수
        temp = sum([data[x][i]+data[i][x] for x in afte]) #오후 스택에 들어 있던 값과 현재 들어가는 값에 대한 점수
        afte.append(i)
        afte_score += temp # 더했다가
        backtrack(i+1) # 백트랙하고
        afte.pop()
        afte_score -= temp # pop할때 다시 빼기
        
backtrack(0) # index 0부터 시작한다.
print(res)