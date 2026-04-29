from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque()
    
    for i in range(len(priorities)):
        q.append((i, priorities[i]))
    
    # 멈추기 위해 사용
    find = True
    
    while find:
        max_value = max(q, key = lambda x : x[1])[1]
        front = q.popleft()
        
        if front[1] < max_value:
            q.append(front)
        else:
            answer += 1
            if front[0] == location:
                find = False
                
        
    return answer