from collections import deque
import heapq as hq

def solution(land, height):
    """
    BFS로 영역 확인하고, 각 영역 별로 사다리를 설치할 수 있는 곳을 파악하여 
    각 영역을 잇는 최소한의 높이의 사다리를 graph로 설정하여
    프림 알고리즘 진행
    """
    wid, hei = len(land), len(land[0])
    data = [[[-1, land[i][j]] for j in range(wid)] for i in range(hei)]
    land_num = 0
    for i in range(hei): #BFS 진행
        for j in range(wid):
            if data[i][j][0] < 0:
                data[i][j][0] = land_num # 영역 번호 매기기
                que = deque([(i,j)])
                while len(que) > 0:
                    x,y = que.popleft()
                    for a,b in [(-1,0), (1,0), (0,-1), (0,1)]:
                        nx,ny = x+a, y+b
                        if 0 <= nx < hei and 0 <= ny < wid and data[nx][ny][0] == -1 and abs(data[x][y][1] - data[nx][ny][1]) <= height:
                            data[nx][ny][0] = land_num
                            que.append((nx,ny))
                land_num += 1 # 큐가 비었으면 영역 번호 +1
    
    # graph = [[float("inf") for j in range(land_num)] for i in range(land_num)] 리스트 쓰지 마세용
    graph = [{} for _ in range(land_num)] #딕셔너리 쓰세용
    
    for i in range(hei): # 각 영역을 연결하는 가장 비용이 덜 드는 사다리 찾기
        for j in range(wid):
            area_1 = data[i][j][0]
            for a,b in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i+a, j+b
                if 0 <= ni < hei and 0 <= nj < wid:
                    area_2 = data[ni][nj][0]
                    cost = abs(data[ni][nj][1] - data[i][j][1]) # 사다리 비용
                    if area_1 != area_2: # area가 다르기 때문에 사다리가 필요하다.
                        if area_2 not in graph[area_1] or graph[area_1][area_2] > cost:
                            graph[area_1][area_2] = cost
                        if area_1 not in graph[area_2] or graph[area_2][area_1] > cost:
                            graph[area_2][area_1] = cost
                        
    
    # print("영역")
    # for x in data:
    #     print(x)
    # print("그래프")
    # for x in graph:
    #     print(x)    
    
    answer = 0
    q = []
    check = [0 for _ in range(land_num)]
    hq.heappush(q, (0, 0)) #비용, 현재 area
    while len(q) > 0: # 프림 알고리즘 진행
        f, cur = hq.heappop(q) # 현재 비용과 위치
        if not check[cur]: # 방문하지 않았다면 check
            check[cur] = 1 
            answer += f # 정답에 더해주고
            for next, cost in graph[cur].items(): # 방문하지 않은 다음 노드와 비용 넣어주기
                if not check[next]:
                    hq.heappush(q, (cost, next))
                    
    return answer
