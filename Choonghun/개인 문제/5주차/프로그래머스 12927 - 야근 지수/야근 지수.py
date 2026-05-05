def solution(n, works):
    answer = 0
    data = [0 for _ in range(1000001)] # 시간대로 나눠서
    top = max(works) # 가장 많은 시간이 필요한 작업부터
    for i in works: # 시간별로 카운트
        data[i] += 1
    for i in range(top, 0, -1):
        # print(data[:top+1])
        if n == 0: # 끝났으면 종료
            break
        if n >= data[i]: # 해당 시간대의 작업량이 n보다 작거나 같으면 
            n -= data[i] # n시간 만큼 소모해서 1시간씩 깎는다
            data[i-1] += data[i] 
            data[i] = 0 
        else:
            data[i] -= n # n보다 크면
            data[i-1] += n # n시간을 1시간씩 소모해서
            n = 0 # 끝
        
    for i in range(0, top+1): # 야근 지수 계산
        answer += i**2 * data[i]
    return answer 