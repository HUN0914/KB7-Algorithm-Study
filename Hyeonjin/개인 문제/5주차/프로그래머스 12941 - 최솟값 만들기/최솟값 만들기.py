def solution(A,B):
    answer = 0
    
    A.sort()
    B.sort(reverse=True)
    
    # 값이 가장 작아지려면 (가장 작은 값) * (가장 큰 값)을 해야한다 -> 그리디
    for i in range(len(A)):
        answer += (A[i] * B[i])

    return answer