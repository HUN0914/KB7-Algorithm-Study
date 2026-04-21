def solution(number):
    answer = 0
    
    def backtracking(idx, arr):
        nonlocal answer
        
        # 종료 조건
        if len(arr) == 3:
            if sum(arr) == 0:
                answer += 1
            return
        for i in range(idx, len(number)):
            backtracking(i+1, arr + [number[i]])
            
        
    backtracking(0, [])       
        
    return answer