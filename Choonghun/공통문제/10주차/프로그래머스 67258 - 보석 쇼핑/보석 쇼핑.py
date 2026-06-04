def solution(gems):
    n = len(gems)
    gemIdx = {} # 각 보석별 개수
    idx = 0 # 보석 종류의 개수
    for t in gems:
        if t not in gemIdx:
            gemIdx[t] = 0
            idx += 1 
    answer = [1, n] # 정답 구간
    l,r = 0,1
    gemIdx[gems[l]] += 1 
    gemCheck = 1 # 맨 처음 보석 포함!
    while l < r:
        if gemCheck == idx: # 현재 갖고 있는 보석 종류의 개수랑 전체 보석 종류의 개수랑 같다면
            if answer[1] - answer[0] + 1 > r-l: # 만약 현재 구간의 길이가 더 짧다면
                answer[0], answer[1] = l+1, r # 갱신
            if answer[1] - answer[0] + 1 == idx: # 정답 구간의 길이가 최소 길이라면 break
                break
            gemIdx[gems[l]] -= 1 # 현재 구간에서 left에 있는 보석 제거
            if not gemIdx[gems[l]]: # 해당 보석이 이제 구간 안에 없다면 종류 개수에서 -1
                gemCheck -= 1
            l += 1 # 포인터 +1
        else:
            if r < n: # r이 n보다 작다면
                if not gemIdx[gems[r]]: # 다음 보석이 구간 안에 없다면
                    gemCheck += 1 # 종류 +1
                gemIdx[gems[r]] += 1 # 개수 +1
                r += 1 # 맨 오른쪽 포인터를 +1
            else:
                break
    
    return answer # 정답 반환