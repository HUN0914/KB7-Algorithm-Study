function solution(n, paths, gates, summits) {
    const graph = Array.from({ length: n + 1 } , () => []);
    
    let maxCost = 0;
    
    for(const [a, b, cost] of paths) {
        graph[a].push([b, cost]);
        graph[b].push([a, cost]);
        
        maxCost = Math.max(maxCost, cost);
    }
    
    const gateSet = new Set(gates);
    const summitSet = new Set(summits);
    
    // limit 이하의 cost 길로만 갈 수 있는지 확인
    function canGo(limit) {
        const visited = new Array(n + 1).fill(false);
        const queue = [];
        let head = 0;
        
        for (const gate of gates) {
            visited[gate] = true;
            queue.push(gate);
        }
        
        while (head < queue.length) {
            const curNode = queue[head++];
            
            // 산봉우리 도착했으면 ture 반환
            if (summitSet.has(curNode)) return true;
            
            // 다음 갈 수 있는 곳 추가
            for (const [nextNode, cost] of graph[curNode]) {
                // 이미 방문했으면 패스
                if (visited[nextNode]) continue;
                // 다른 gate로 가는 건 금지
                if (gateSet.has(nextNode)) continue;
                // limit보다 큰 길은 못 감
                if (cost > limit) continue;
                
                visited[nextNode] = true;
                queue.push(nextNode);
            }
        }
        
        return false;
    }
    
    // 이분 탐색으로 최소 intensity 찾기
    let left = 1;
    let right = maxCost;
    
    let minIntensity = maxCost;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        // mid 값으로 summit까지 도달 가능하면
        if (canGo(mid)) {
            minIntensity = mid;
            
            // 더 작은 intensity 가능한지 확인
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    const visited = new Array(n + 1).fill(false);
    const queue = [];
    let head = 0;
    
    for (const gate of gates) {
        visited[gate] = true;
        queue.push(gate);
    }
    
    while (head < queue.length) {
        const curNode = queue[head++];
        
        // summit 도착하면 다음 탐색 계속 진행
        if (summitSet.has(curNode)) continue;
        
        for (const [nextNode, cost] of graph[curNode]) {
            if (visited[nextNode]) continue;
            
            if (gateSet.has(nextNode)) continue;
            
            // 최소 intensity보다 크면 이동 불가
            if (cost > minIntensity) continue;
            
            visited[nextNode] = true;
            queue.push(nextNode);
        }
    }
    
    // 산봉우리 번호가 작은 것부터 확인하려고 정렬
    summits.sort((a, b) => a - b);
    
    for (const summit of summits) {
        // summit 방문 했으면 true 되어 있음
        if (visited[summit]) {
            return [summit, minIntensity];
        }
    }
}