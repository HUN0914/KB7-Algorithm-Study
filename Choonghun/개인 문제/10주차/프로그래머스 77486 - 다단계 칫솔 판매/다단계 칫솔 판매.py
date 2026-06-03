import sys

def solution(enroll, referral, seller, amount):
    tree = {}
    result = {}
    visited = {}
    n = len(enroll)
    for name in enroll:
        tree[name] = []
        result[name] = 0
    
    for i in range(n):
        if referral[i] != "-":
            tree[enroll[i]].append(referral[i])
    
    answer = []
    
    def dfs(cur, fee):
        guarentee = fee // 10
        if fee:
            for parent in tree[cur]:
                dfs(parent, guarentee)
            result[cur] += fee-guarentee
    
    s = len(seller)
    for i in range(s):
        name, cnt = seller[i], amount[i]
        dfs(name, cnt*100)
    
    for name in enroll:
        answer.append(result[name])
    
    return answer