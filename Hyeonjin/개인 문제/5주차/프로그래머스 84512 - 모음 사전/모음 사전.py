def solution(word):
    
    alpha = ['A', 'E', 'I', 'O', 'U']
    dict = []
    
    def dfs(w):
        if len(w) > 0:
            dict.append(w)
        
        if len(w) == 5:
            return
        
        for a in alpha:
            dfs(w + a)
    
    dfs('')
    
    answer = dict.index(word) + 1
    
    return answer