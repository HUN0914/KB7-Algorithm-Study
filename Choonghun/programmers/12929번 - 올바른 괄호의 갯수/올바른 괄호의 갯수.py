def solution(n):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-1-j]
    return dp[n]

print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))