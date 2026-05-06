def solution(m, preference, coffee):
    preference.sort()
    coffee.sort()
    answer = 0
    for i in range(m):
        if coffee[i] > preference[i]:
            answer += coffee[i] - preference[i]
    return answer

print(solution(4, [3,4,5,6], [5,4,6,7]))