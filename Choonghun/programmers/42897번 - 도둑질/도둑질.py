def solution(money):
    answer = 0
    dp = [[0, 0] for _ in range(len(money))] #0번을 포함하느냐 하지 않느냐
    dp[0], dp[1] = [money[0],0], [0,money[1]]
    for i in range(2, len(money)): # DP 시작
        if i == len(money)-1: # 맨 뒷집이면 0을 포함하면 안된다.
            dp[i][1] = max(dp[i-3][1], dp[i-2][1]) + money[i] 
        elif i == 2: # 2번째 집이면 0번째 집의 경우만 고려한다.
            dp[i][0] = dp[i-2][0] + money[i]
            dp[i][1] = dp[i-2][1] + money[i]
        else: # 현재 인덱스에서 2칸 뒤, 3칸 뒤의 경우에서
            # 0을 포함하는 경우, 그렇지 않은 경우를 고려하여 연산
            dp[i][0] = max(dp[i-3][0], dp[i-2][0]) + money[i]
            dp[i][1] = max(dp[i-3][1], dp[i-2][1]) + money[i]
            
    answer = max(max(dp[-1]), max(dp[-2]), max(dp[-3])) 
    # 최댓값은 맨 뒤 3개의 배열에서 가지고 온다. 
    # 2개가 아니고 3개를 가져오는 이유는 아래를 참고...
    return answer

print(solution([3,2,1])) #입력 길이가 3이고 최댓값이 맨 앞에 있다면 뒤에 두 개만 가져왔을때 오답이 발생한다.