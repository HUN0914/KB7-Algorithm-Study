class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        visited = [[0 for _ in range(n)] for __ in range(m)]
        answer = 0
        def dfs(x,y):
            if visited[x][y]:
                return visited[x][y]
            visited[x][y] = 1
            for i,j in [(-1,0),(1,0),(0,1),(0,-1)]:
                nx, ny = x+i, y+j
                if 0 <= nx < m and 0 <= ny < n and matrix[x][y] < matrix[nx][ny]:
                    visited[x][y] = max(visited[x][y], dfs(nx,ny)+1)
            return visited[x][y]
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    dfs(i,j)
                    answer = max(answer,visited[i][j])
        return answer