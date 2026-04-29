# 전선을 하나씩 끊으면서 bfs를 돌려서 한 쪽의 개수만 세면 된다!
from collections import deque

def solution(n, wires):
    answer = 1e9
    
    # bfs 함수
    def bfs(start, a):
        visited = [False] * (n+1)
        
        q = deque()
        q.append(start)
        visited[start] = True
        
        count = 1
        
        while q:
            now = q.popleft()
            
            for i in a[now]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
                    count += 1
                    
        return count
    
    answer_list = set()
    
    # 돌아가면서 링크를 끊어준다
    for i in range(n-1):
        arr = wires[:i] + wires[i+1:]
        
         # 전선 정보를 저장할 인접리스트
        link = [[] for _ in range(n+1)]
    
        # 돌아가면서 정보 저장
        for v1, v2 in arr:
            link[v1].append(v2)
            link[v2].append(v1)
        
        # 어차피 2개로 나뉘니까 for문 돌릴 필요없이 1만 돌리면 된다.
        answer_list.add(bfs(1, link))
    
    # 가장 차이가 적게 나는 정답 고르기
    for i in answer_list:
        answer = min(answer, abs(i - (n-i)))
    
    return answer