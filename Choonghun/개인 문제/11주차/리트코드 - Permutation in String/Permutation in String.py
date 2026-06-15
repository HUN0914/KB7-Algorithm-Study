class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        data = {} # 정답 체크
        for i in range(len(s1)): 
            if s1[i] not in data:
                data[s1[i]] = 0
            data[s1[i]] += 1
        check = {}
        l,r = 0, 1 
        check[s2[l]] = 1 # 윈도우 범위 내 문자개수
        def checkPer(): # 순열 검증
            for c in check: # 현재 범위 내에서
                if c not in data: # s1에 없으면
                    return 0 if r < len(s2) else 1 # 0 반환 (r이 s2 길이를 벗어나면 1)
                if check[c] > data[c]: # s1에 있는 것보다 많으면
                    return 1 # 1반환
            for c in data: # 순열 내에서
                if c not in check or check[c] < data[c]: # 윈도우 내에 없거나 윈도우 내에 있는 값이 더 작다면
                    return 2 if r < len(s2) else 1 # 2 반환 (r이 s2 길이를 벗어나면 1)
            return 3 # 순열 발견했으면 3 반환
        
        while l < r:
            x = checkPer()
            if x == 1: # x == 1이면 왼쪽 포인터 한 칸 밀기
                check[s2[l]] -= 1 
                l += 1
            elif x == 0: # x == 0이면 윈도우를 r의 위치로 옮기고 초기화
                l = r
                r += 1
                check.clear()
                check[s2[l]] = 1
            elif x == 2: # x == 2면 오른쪽 포인터 한 칸 밀기
                if s2[r] not in check:
                    check[s2[r]] = 0
                check[s2[r]] += 1
                r += 1
            else: # x == 3이면 True 반환
                return True
        return False # 발견 못했으면 False 반환