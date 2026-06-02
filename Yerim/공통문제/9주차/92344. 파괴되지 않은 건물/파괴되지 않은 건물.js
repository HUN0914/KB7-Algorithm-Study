function solution(board, skill) {
    const N = board.length;
    const M = board[0].length;
    
    // skill 돌면서 공격 회복 저장
    const graph = Array.from({ length: N + 1 }, () => Array(M + 1).fill(0));
    
    // console.log(graph);
    for (const [type, r1, c1, r2, c2, degree] of skill) {
        const value = type === 1 ? -degree : degree;
        
        // 네 꼭짓점에 저장
        graph[r1][c1] += value;
        graph[r1][c2 + 1] -= value;
        graph[r2 + 1][c1] -= value;
        graph[r2 + 1][c2 + 1] += value;
        
        // console.log(graph);
    }
    
    
    
    // 최종 누적합 계산
    for (let row = 0; row <= N; row++) {
        for (let col = 1; col <= M ; col++) {
            graph[row][col] += graph[row][col - 1];         
        }
    }

    for (let col = 0; col <= M; col++) {
        for (let row = 1; row <= N ; row++) {
            graph[row][col] += graph[row - 1][col];
        }
    }
    
    // 0보다 큰 것만 카운트
    let count = 0;
    
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < M; j++) {
            if ((board[i][j] + graph[i][j]) > 0) count++;
        }
    }
    
    return count;
}