function solution(n, costs) {
    // 비용 낮은 순으로 정렬
    costs.sort((a, b) => a[2]- b[2]);
    
    const parent = Array.from({ length: n }, (_, i) => i);
    
    function find(x) {
        if (parent[x] === x) return x;
        return parent[x] = find(parent[x]);
    }
    
    function union(a, b) {
        const rootA = find(a);
        const rootB = find(b);
        
        if (rootA === rootB) return false;
        
        parent[rootB] = rootA;
        return true;
    }
    
    let answer = 0;
    let count = 0;
    
    for (const [a, b, cost] of costs) {
        if(union(a, b)) {
            answer += cost;
            count++;
            
            if (count === n - 1) break;
        }
    }
    
    return answer;
    
    
}