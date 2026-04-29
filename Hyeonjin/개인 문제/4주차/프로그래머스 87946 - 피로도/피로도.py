# 1. 항상 좋은 선택 기준이 있는가? -> 없음 (그리디, 우선순위 큐 사용할 수 x)
# 2. 던전의 수가 많은가? -> 8개로 적음 (완전 탐색 가능)
# => 완전 탐색, 백트래킹, 순열을 사용하자

def solution(k, dungeons):
    answer = 0
    
    n = len(dungeons)
    
    visited = [False] * n
    
    # 백트래킹 함수의 파라미터 선택법 -> 지금 이 시점에서 내가 알고 있어야 다음 선택을 할 수 있는 정보
    def backtracking(now, count):
        nonlocal answer
        
        # 정답 갱신
        answer = max(answer, count)
        
        for i in range(n):
            if not visited[i] and now >= dungeons[i][0]:
                visited[i] = True
                backtracking(now - dungeons[i][1], count + 1)
                visited[i] = False
                 
    backtracking(k, 0)

    return answer