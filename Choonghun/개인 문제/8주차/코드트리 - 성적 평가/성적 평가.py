N = int(input())
scores = [list(map(int, input().split())) for _ in range(3)]
score = [[[0,i] for i in range(N)] for _ in range(4)]
rank = [[0 for i in range(N)] for _ in range(4)]
# Please write your code here.
for s in range(3):
    sc = scores[s]
    temp = []
    for i in range(N):
        score[s][i][0] += sc[i]
        score[3][i][0] += sc[i]
for s in range(4):
    score[s].sort(reverse=True)
    r = 1
    a = 1
    for i in range(N):
        k,idx = score[s][i]
        if i > 0:
            if k != score[s][i-1][0]:
                r += a
                a = 1
            else:
                a += 1
        rank[s][idx] = r
    print(' '.join(map(str,rank[s])))
