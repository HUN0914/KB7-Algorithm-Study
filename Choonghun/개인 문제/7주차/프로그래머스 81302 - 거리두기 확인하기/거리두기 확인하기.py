def solution(places):
    answer = []
    def dfs(place):
        visited = [[0 for _ in range(5)] for __ in range(5)]
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    stack = []
                    stack.append((i,j,0))
                    visited[i][j] = 1
                    while len(stack) > 0:
                        x,y,t = stack.pop()
                        if t >= 2:
                            continue
                        for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nx,ny = a+x, b+y
                            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                                if place[nx][ny] == 'P':
                                    return 0
                                elif place[nx][ny] == 'O':
                                    visited[nx][ny] = 1
                                    stack.append((nx,ny,t+1))
        return 1
    
    for place in places:
        answer.append(dfs(place))
                                    
    return answer