from collections import deque
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m = len(forest)
        n = len(forest[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append(forest[i][j])
        trees.sort()
        treeNum = len(trees)
        visited = [[0 for _ in range(n)] for _ in range(m)] # 방문 체크
        treeVisited = [10e9 for _ in range(treeNum+1)] # 방문한 나무인지
        que = deque([])
        visited[0][0] = 1
        if forest[0][0] == trees[0]: # 맨처음 나무가 가장 먼저 방문해야 할 나무인지
            visited[0][0] = 2
            treeVisited[0] = 1
            que.append((0,0,2,0))
        else:
            que.append((0,0,1,0))
        
        while len(que) > 0:
            x,y,idx,d = que.popleft()
            if treeVisited[idx] < d:
                # print("oh")
                continue
            for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx,ny = x+i, y+j
                if 0 <= nx < m and 0 <= ny < n and forest[nx][ny]: 
                    if forest[nx][ny] == trees[idx-1]: # 다음 노드가 다음 차례의 나무라면
                        if visited[nx][ny] < idx+1: # 방문 처리
                            if idx == treeNum:
                                return d+1
                            treeVisited[idx] = d+1
                            visited[nx][ny] = idx+1
                            que.clear() # 나머지 경우는 의미 없으므로 모두 비우고
                            que.append((nx,ny,idx+1,d+1)) # 추가
                            continue
                    else:
                        if visited[nx][ny] < idx: # 일반 길이거나 다른 차례의 나무일때
                            visited[nx][ny] = idx
                            que.append((nx,ny,idx,d+1))
        return -1
