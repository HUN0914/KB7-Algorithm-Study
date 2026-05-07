def solution(operations):
    que = []
    for op in operations:
        com, num = op.split()
        num = int(num)
        if com == "I": # 삽입
            que.append(num) 
            i = len(que)-1
            while i > 0: # 정렬
                if que[i-1] > que[i]:
                    que[i],que[i-1] = que[i-1], que[i]
                else:
                    break
                i-=1
        else: # pop
            if len(que) > 0:
                if num == 1: # 최댓값 pop
                    que.pop()
                else: # 최솟값 pop
                    que.pop(0)
    
    if len(que) > 0: # 큐에 값이 있으면
        answer = [que[-1], que[0]] #최댓값, 최솟값
    else: # 없으면
        answer = [0,0]
    return answer