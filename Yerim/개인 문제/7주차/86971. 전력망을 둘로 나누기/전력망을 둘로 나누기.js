function solution(n, wires) {
    const result = [];
    
    for (let i = 0; i < wires.length; i++) {
        // 전력망 연결 정보 저장
        const wiresInfo = {};
        
        for (let j = 0; j < wires.length; j++) {
            if (i === j) continue;
            
            const [w1, w2] = wires[j];
            
            if (!wiresInfo[w1]) wiresInfo[w1] = [];
            if (!wiresInfo[w2]) wiresInfo[w2] = [];
            
            wiresInfo[w1].push(w2);
            wiresInfo[w2].push(w1);
        }
        
        const visited = Array(n + 1).fill(false);
        let count = 0;
        
        function dfs(wire) {
            visited[wire] = true;
            count++;
            
            for (const next of wiresInfo[wire] || []) {
                if (!visited[next]) dfs(next);
            }
        }
        
        dfs(1);
        
        result.push(Math.abs(count - (n - count)));
    }
    
    return Math.min(...result);
}