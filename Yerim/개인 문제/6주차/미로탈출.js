function solution(maps) {
    const n = maps.length;
    const m = maps[0].length;
    
    const dr = [-1, 1, 0, 0]; // 상하좌우
    const dc = [0, 0, -1, 1];
    
    // S, L, E 위치 찾기
    let sr, sc, lr, lc, er, ec = 0;
    
    // S 위치
    for (let i = 0; i < n; i++) {
        // 문자열에 S가 포함되어 있으면
        if (maps[i].includes("S")) {
            sr = i;
            sc = maps[i].indexOf("S");
            break;
        }
    }
    
    // L 위치
    for (let i = 0; i < n; i++) {
        // 문자열에 L이 포함되어 있으면
        if (maps[i].includes("L")) {
            lr = i;
            lc = maps[i].indexOf("L");
            break;
        }
    }
    
    // E 위치
    for (let i = 0; i < n; i++) {
        // 문자열에 E가 포함되어 있으면
        if (maps[i].includes("E")) {
            er = i;
            ec = maps[i].indexOf("E");
            break;
        }
    }
    
    const queue = [[sr, sc]];
    
    const distance = Array.from({ length: n }, () => Array(m).fill(-1));
    
    distance[sr][sc] = 0;
    
    // 라벨까지 최소 거리 찾기
    while (queue.length) {
        const [r, c] = queue.shift();
        
        for (let i = 0; i < 4; i++) {
            const nr = r + dr[i];
            const nc = c + dc[i];
            
            // 범위 밖이면 패스
            if (nr >= n || nr < 0 || nc >= m || nc < 0) continue;
            
            // 벽이면 패스
            if (maps[nr][nc] === "X") continue;
            
            // 방문한적 있으면 패스
            if (distance[nr][nc] !== -1) continue;
            
            distance[nr][nc] = distance[r][c] + 1;
            queue.push([nr, nc]);
            
            // 다음 통로가 라벨이면 while문 종료
            if (maps[nr][nc] === "L") break;
        }
    }
    
    // 라벨까지 최소 거리 저장
    const labelDist = distance[lr][lc];
    
    // 거리 초기화
    const distance2 = Array.from({ length: n }, () => Array(m).fill(-1));
    
    distance2[lr][lc] = labelDist;
    
    const queue2 = [[lr, lc]];
    
    // 라벨까지 최소 거리 찾기
    while (queue2.length) {
        const [r, c] = queue2.shift();
        
        for (let i = 0; i < 4; i++) {
            const nr = r + dr[i];
            const nc = c + dc[i];
            
            // 범위 밖이면 패스
            if (nr >= n || nr < 0 || nc >= m || nc < 0) continue;
            
            // 벽이면 패스
            if (maps[nr][nc] === "X") continue;
            
            // 방문한적 있으면 패스
            if (distance2[nr][nc] !== -1) continue;
            
            distance2[nr][nc] = distance2[r][c] + 1;
            queue2.push([nr, nc]);
            
            // 다음 통로가 출구면 while문 종료
            if (maps[nr][nc] === "E") break;
        }
    }
        
    return distance[er][ec];
}