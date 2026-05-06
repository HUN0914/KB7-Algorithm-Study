import heapq as hq
def solution(n,t,r): # 시간, 티켓
    time = [[] for _ in range(10001)]
    for i in range(n):
        time[t[i]].append((r[i], t[i], i))
    q = []
    x = 0
    i = 0
    answer = []
    # print(time)
    while x < n:
        # print(q)
        while time[i]:
            hq.heappush(q, time[i].pop())
        if q:
            answer.append(hq.heappop(q)[2])
            i+=1
            x+=1
    
    return answer

print(solution([0,1,3,0], [0,1,2,3]))
