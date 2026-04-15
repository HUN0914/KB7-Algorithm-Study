import sys
input = sys.stdin.readline

n,m = [int(i) for i in input().split()]
k = int(input())
data = [input().rstrip() for _ in range(n)]
count = [[[0,0,0] for _ in range(m)] for __ in range(n)]

def check_idx(char):
    return 0 if char == 'J' else 1 if char == 'O' else 2

for i in range(n):
    for j in range(m):
        if i > 0 and j > 0:
            count[i][j][0] = count[i-1][j][0] + count[i][j-1][0] - count[i-1][j-1][0]
            count[i][j][1] = count[i-1][j][1] + count[i][j-1][1] - count[i-1][j-1][1]
            count[i][j][2] = count[i-1][j][2] + count[i][j-1][2] - count[i-1][j-1][2]
        elif i > 0:
            count[i][j] = list(count[i-1][j])
        elif j > 0:
            count[i][j] = list(count[i][j-1])
        idx = check_idx(data[i][j])
        count[i][j][idx] += 1

for _ in range(k):
    lx,ly,rx,ry = [int(i)-1 for i in input().split()]
    if lx > 0 and ly > 0:
        res = [str(count[rx][ry][i]-count[lx-1][ry][i]-count[rx][ly-1][i]+count[lx-1][ly-1][i]) for i in range(3)]
    elif lx > 0:
        res = [str(count[rx][ry][i]-count[lx-1][ry][i]) for i in range(3)]
    elif ly > 0:
        res = [str(count[rx][ry][i]-count[rx][ly-1][i]) for i in range(3)]
    else:
        res = [str(count[rx][ry][i]) for i in range(3)]
    print(' '.join(res))