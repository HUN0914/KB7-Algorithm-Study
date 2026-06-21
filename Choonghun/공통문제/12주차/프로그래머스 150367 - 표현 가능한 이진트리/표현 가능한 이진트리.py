import math
def solution(numbers):
    """
    7 -> 111
    42 -> 0101010 -> 
    5 -> 101
    63 -> 0111111
    111 -> 1101111
    95 -> 1011111
    리프 노드 외의 노드가 자식이 0일때 0이면 X
    """
    comp = [0] * 65 # 포화 이진트리는 노드개수 최대 63개 => 2**63 이유는 2^49 < 10^15 < 2^50, 0을 앞에 추가하면 63개까지 늘어난다.
    bins = [] # 십진수를 이진수로 변환후 저장할 배열
    cur = 1
    while cur < 65: # 포화 이진트리를 구성하는 노드의 개수는 1, 3, 7, 15, 31...
        comp[cur] = 1
        cur += cur+1

    def decTobin(n): # 십진수를 이진수(포화 이진트리)로 변환
        flag = 0 # 처음으로 1이 들어가면 flag를 1로 변환
        bin = []
        for i in range(54, -1, -1): 
            if n < 2**i:
                if flag: # flag가 1일때만 0을 이진수 배열에 삽입
                    bin.append(0)
            else:
                flag = 1 
                n -= 2**i 
                bin.append(1) 
        while not comp[len(bin)]: # 포화 이진트리로 만들기
            bin = [0] + bin
        return bin # 포화 이진트리 반환
    
    def dfs(cur, dep):
        if not answer[-1]: # 이미 불가능하다고 판별되었으면 return
            return
        if dep:
            left, right = cur-2**(dep-1), cur+2**(dep-1) # 자식 노드 번호 구하는 법
            if not bins[-1][cur] and (bins[-1][left] or bins[-1][right]): 
                # 현재 노드가 0인데 자식 노드 중에 하나라도 1이면 표현 불가능한 이진트리이다.
                answer[-1] = 0
            else:
                dfs(left, dep-1) # 다음 Search 진행
                dfs(right, dep-1)
        
    answer = []
    
    for n in numbers:
        answer.append(1) # 일단 1을 삽입
        bins.append(decTobin(n)) # 포화이진트리를 배열에 추가
        deg = int(math.log2(len(bins[-1]))) # 노드의 개수에 1을 더한 값의 log2에 정수만 가져오면 포화이진트리의 depth
        root = len(bins[-1]) // 2 # root는 노드 개수를 2로 나눈 몫
        # print(root,deg,bins[-1])
        dfs(root, deg) # dfs 진행 => 불가능한 트리면 0으로 바뀌게 된다.
    
    return answer # 정답 반환