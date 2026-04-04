import sys
input = sys.stdin.readline

n = int(input())
data = [[int(i) for i in input().split()] for _ in range(n)]
# 조합 문제이고 결과는 순서가 상관이 없다
res = 10e9
morn = [] # 아침 스택
afte = [] # 저녁 스택
def backtrack(i):
    if i == n: #index가 n에 도달하면 결과를 도출하고 갱신한다.
        getResult()
        return
    if len(morn) < n//2: # 아침 스택이 n//2보다 적으면 추가하고 재귀 실행, 백트랙이므로 pop 필수
        morn.append(i)
        backtrack(i+1)
        morn.pop()
    if len(afte) < n//2: # 저녁 스택이 n//2보다 적으면 추가하고 재귀 실행, 백트랙이므로 pop 필수
        afte.append(i)
        backtrack(i+1)
        afte.pop()

def getResult(): 
    global res
    morning = []
    afternoon = []
    for i in range(n//2-1): #2중 포문으로 오전, 오후 업무 강도 계산
        for j in range(i+1,n//2):
            morning.append(data[morn[i]][morn[j]]+data[morn[j]][morn[i]]) 
            afternoon.append(data[afte[i]][afte[j]]+data[afte[j]][afte[i]])
    res = min(abs(sum(morning)-sum(afternoon)), res)
backtrack(0) # index 0부터 시작한다.
print(res)