from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 큐 이동 횟수
    answer = 0
    
    # 현재 다리 위에 있는 트럭을 저장할 큐 (길이 고정)
    bridge = deque([0] * bridge_length)
    
    # 현재 무게
    total = 0
    
    # 현재 트럭 인덱스
    idx = 0
    
    while idx < len(truck_weights) or total > 0:
        answer += 1
        
        # 1. 다리 맨 앞 제거
        out = bridge.popleft()
        total -= out
        
        # 2. 다음 트럭을 넣을 수 있는지 확인
        if idx < len(truck_weights) and total + truck_weights[idx] <= weight:
            bridge.append(truck_weights[idx])
            total += truck_weights[idx]
            idx += 1
        else:
            bridge.append(0)
        
        
    return answer