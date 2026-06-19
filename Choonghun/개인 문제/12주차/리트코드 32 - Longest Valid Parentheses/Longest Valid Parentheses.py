class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
            열고 닫히는 구간을 모두 더한 뒤
            투 포인터 개시
        """
        n = len(s)
        st = []
        answer = 0
        
        sets = []

        for i in range(n):
            if s[i] == '(':
                st.append(i)
            else:
                if st:
                    sets.append((st.pop(), i))
        
        sets.sort()
        if len(sets):
            l, r = sets[0]
            answer = r-l+1
            if len(sets) > 1:
                for i, j in sets:
                    if j <= r:
                        continue
                    elif i-1 <= r:
                        r = j
                    else:
                        l,r = i,j
                    answer = r-l+1 if r-l+1 > answer else answer 

        return answer