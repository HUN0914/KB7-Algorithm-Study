function solution(k, dungeons) {
    // 던전 순열 구하기
    const permutations = getPermutations(dungeons);
    
    const result = [];
    
    for (let i = 0; i < permutations.length; i++) {
        let fatigue = k;
        let count = 0;
        
        for (const dungeon of permutations[i]) {
            
            const [ required, cost ] = dungeon;
            
            if (fatigue < required) continue;
            
            fatigue -= cost;
            count++;
        }

        result.push(count);
    }
    
    return Math.max(...result);
}

function getPermutations(dungeons) {
    const result = [];
    const visited = Array(dungeons.length).fill(false);
    
    function dfs(path) {
        if (path.length === dungeons.length) {
            result.push([...path]);
            return;
        }
        
        for (let i = 0; i < dungeons.length; i++) {
            // 이미 추가한 던전이면 패스
            if (visited[i]) continue;
            
            visited[i] = true;
            path.push([...dungeons[i]]);
            
            dfs(path);
            
            path.pop();
            visited[i] = false;
        }
    }
    
    dfs([]);
    
    return result;
}