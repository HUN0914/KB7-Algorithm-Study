import sys
input = sys.stdin.readline

n, m = [int(i) for i in input().split()]
data = [[int(i) for i in input().split()] for _ in range(n)]

types = [
    [(0,0),(-1,-1),(-1,0),(-1,1)], # 5번 블록 4가지
    [(0,0),(-1,1),(0,1),(1,1)],
    [(0,0),(1,-1),(1,0),(1,1)],
    [(0,0),(-1,-1),(0,-1),(1,-1)]
]

check = [[0 for _ in range(m)] for __ in range(n)]
answer = 0
def dfs(i,j,sum,node):
    global answer
    if node == 4:
        answer = max(answer, sum)
        return
    for a,b in [(0,1),(0,-1),(1,0),(-1,0)]:
        ni,nj = i+a,j+b
        if 0 <= ni < n and 0 <= nj < m and not check[ni][nj]:
            check[ni][nj] = 1
            dfs(ni, nj, sum+data[ni][nj], node+1)
            check[ni][nj] = 0

for i in range(n):
    for j in range(m):
        check[i][j] = 1
        dfs(i,j,data[i][j],1)
        check[i][j] = 0
        for ty in types:
            res = 0
            for t in ty:
                a,b = t
                ni,nj = i+a, j+b
                if 0 <= ni < n and 0 <= nj < m:
                    res += data[ni][nj]
                else:
                    res = -1
                    break
            if res >= 0:
                answer = max(answer, res)
print(answer)