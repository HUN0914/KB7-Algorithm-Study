import sys
sys.setrecursionlimit(10000)
answer = "impossible"
def solution(n, m, x, y, r, c, k):
    side = {'d': (1,0), 'l': (0,-1), 'r': (0,1), 'u': (-1,0)}
    stack = []
    def backtrack(u,v):
        global answer
        dist = abs(r-u) + abs(c-v)
        if dist + len(stack) > k or (dist-(k-len(stack)))%2:
            return
        if len(stack) >= k:
            if (u,v) == (r,c) and answer == "impossible":
                answer = ''.join(stack)
            return
        for a in ['d','l','r','u']:
            i,j = side[a]
            nx,ny = u+i, v+j
            if 0 < nx < n+1 and 0 < ny < m+1:
                stack.append(a)
                backtrack(nx,ny)
                if answer != "impossible":
                    return
                stack.pop()
    backtrack(x,y)
    return answer
