def solution(s):
    # 띄어쓰기 기준으로 나누기 (공백 문자가 여러개 나올 수 있음을 주의)
    arr = list(s.split(" "))

    for i in range(len(arr)):
        # 만약 공백 문자라면 넘어가야함
        if len(arr[i]) == 0:
            continue
        
        # 문자열의 하나만 바꾸는 것이 불가능해서 리스트로 바꿔서 계산
        word = list(arr[i])
            
        # 첫번째는 대문자 처리
        word[0] = word[0].upper()
        
        # 나머지는 소문자 처리
        for j in range(1, len(word)):
            word[j] = word[j].lower()
        
        arr[i] = "".join(word)
    
    answer = " ".join(arr)
    
    return answer