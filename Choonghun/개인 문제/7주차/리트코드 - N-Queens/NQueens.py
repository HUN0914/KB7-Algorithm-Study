class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        larr = {}
        rarr = {}
        row = [0 for _ in range(n)]
        col = [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                larr[i-j] = 0
                rarr[i+j] = 0
        
        stack = []
        answer = []
        def backtrack(ind):
            if ind == n:
                temp = []
                for i in range(n):
                    temp.append(''.join(['Q' if (i,j) in stack else '.' for j in range(n)]))
                answer.append(temp)
                return 
            for i in range(n):
                if not row[ind] and not col[i] and not larr[ind-i] and not rarr[i+ind]:
                    stack.append((ind,i))
                    row[ind], col[i], larr[ind-i], rarr[i+ind] = 1, 1, 1, 1
                    backtrack(ind+1)
                    row[ind], col[i], larr[ind-i], rarr[i+ind] = 0, 0, 0, 0
                    stack.pop()
        
        backtrack(0)
        return answer