def solution(number, k):    
    # 스택
    stack = []
    
    for i in number:
        # 쌓다가 큰 숫자가 오면 작은 애들을 전부 제거 하기
        while stack and stack[-1] < i and k > 0:
            stack.pop()
            k -= 1
        
        # 위의 조건에 해당하지 않으면 일단 넣어
        stack.append(i)
    
    # 만약 k가 남았을 경우 뒤에서 부터 지워야함
    if k > 0:
        stack = stack[:-k]

    answer = ''.join(stack)
    
    return answer