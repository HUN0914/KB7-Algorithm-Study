def solution(user_id, banned_id):
    """
    user_id에 중복은 없다, 길이는 1 이상 8이하, 배열의 크기도 1이상 8이하
    """
    BanNum = len(banned_id) # 밴 id 개수
    check = [0 for _ in range(2**len(user_id))] # 체크용 -> 비트마스킹 사용
    banned_case = [[] for _ in range(BanNum)] # 각 banned_id마다 적용 가능한 user_id의 인덱스를 저장할 2차원 배열
    def compare_word(alp, ban): # 각 자리수를 비교할 메서드
        if ban == '*': # ban 쪽이 *이면 True
            return True
        elif ban == alp: # 둘이 같아도 True
            return True
        return False # 그 외는 Faluse

    def binTodec(bin): # 0, 1로 이루어진 배열(이진수)를 십진수로 변환하는 메서드
        res = 0
        for i in range(len(bin)):
            res += bin[i] * 2**i
        return res
    
    for i in range(len(user_id)): #각 user_id에 대하여
        id = user_id[i]
        for j in range(len(banned_id)): # banned_id를 비교해서
            ban = banned_id[j]
            if len(id) != len(ban): # 길이가 다르면 패스
                continue
            flag = 1 # 패턴이 부합하는지 여부를 체크하기 위한 플래그
            for k in range(len(id)): # 각 자리수를 비교
                if not compare_word(id[k], ban[k]): # 다르면 flag를 0으로 바꾸고 break
                    flag = 0 
                    break
            if flag: # 패턴이 부합한다면 flag는 1이므로 해당 패턴에 대해 해당 id의 인덱스를 추가한다.
                banned_case[j].append(i)
    backtrack_check = [0 for _ in range(len(user_id))] # 백트랙을 진행하기 위한 체크 배열 (2진수 역할)
    def backtrack(cur): # 백트랙 함수
        if cur == len(banned_case): # 만약 끝에 도달하면
            check[binTodec(backtrack_check)] = 1 # 2진수를 10진수로 변환하고 체크 후 종료
            return
        
        for i in banned_case[cur]: # cur 번째 case에 대한 id가
            if not backtrack_check[i]: # 이미 밴 목록에 포함됐는지 체크
                backtrack_check[i] = 1 # 포함하고
                backtrack(cur+1) # 다음 패턴으로 넘어갔다가
                backtrack_check[i] = 0 # 다시 해제
    backtrack(0) # cur은 0부터
    return sum(check) # check는 0과 1로 이루어져 있으므로 가능한 경우의 수만큼 1이 있을 것이므로 sum(check)가 곧 정답

# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))