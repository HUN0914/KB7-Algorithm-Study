def solution(brown, yellow):
    answer = []
    
    # 전체 넓이 = brown + yellow
    size = brown + yellow
    
    # 노란색 = (w-2) * (h-2)
    
    for h in range(1, size+1):
        if size % h == 0:
            w = size // h
            if yellow == (w-2) * (h-2):
                answer.append(w)
                answer.append(h)
                return answer