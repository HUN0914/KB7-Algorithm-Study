n = int(input())

work = [list(map(int, input().split())) for _ in range(n)]

# True면 아침 / False면 저녁
selected = [False] * (n)

# 최솟값
answer = 1e9

def calc():
    day = []
    night = []

    # selected가 True면 아침, False면 저녁
    for i in range(n):
        if selected[i]:
            day.append(i)
        else:
            night.append(i)
    
    day_sum = 0
    night_sum = 0

    for i in range(n//2):
        for j in range(i + 1, n//2):
            a, b = day[i], day[j]
            day_sum += work[a][b] + work[b][a]
            c, d = night[i], night[j]
            night_sum += work[c][d] + work[d][c]
    
    return abs(day_sum - night_sum)


def backtracking(idx, cnt):
    global answer

    if cnt == n//2:
        answer = min(answer, calc())
        return
    
    if idx == n:
        return
    
    selected[idx] = True
    backtracking(idx + 1, cnt + 1)

    selected[idx] = False
    backtracking(idx + 1, cnt)

backtracking(0, 0)
print(answer)



    
