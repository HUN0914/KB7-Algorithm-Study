def solution(s):
    n = len(s)
    group = len(s) // 2
    answer = []
    if not group:
        answer.append(1)
    for i in range(1,group+1):
        stack = []
        temp = ''
        for j in range(0,n,i):
            if j > 0 and s[j:j+i] != s[j-i:j]:
                if len(stack) > 1:
                    temp = temp + str(len(stack)) + stack.pop()
                elif len(stack) == 1:
                    temp = temp + stack.pop()
                stack.clear()
            stack.append(s[j:j+i])
        if stack:
            if len(stack) > 1:
                temp = temp + str(len(stack)) + stack.pop()
            elif len(stack) == 1:
                temp = temp + stack.pop()
        answer.append(len(temp))
    return min(answer)