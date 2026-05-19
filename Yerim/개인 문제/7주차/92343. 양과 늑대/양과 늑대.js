function solution(info, edges) {
    const graph = Array.from({ length: info.length }, () => []);
    
    for (const [parent, child] of edges) {
        graph[parent].push(child);
    }
    
    let sheepCount = 0;
    
    function dfs(node, sheep, wolf, candidates) {
        if (info[node] === 0) {
            sheep++;
        } else {
            wolf++;
        }
        
        if (wolf >= sheep) return;
        
        sheepCount = Math.max(sheepCount, sheep);
        
        for (const next of candidates) {
            const nextCandidates = candidates.filter(v => v !== next);
            nextCandidates.push(...graph[next]);
            
            dfs(next, sheep, wolf, nextCandidates);
        }
    }
    
    dfs(0, 0, 0, graph[0]);
    
    return sheepCount;
}