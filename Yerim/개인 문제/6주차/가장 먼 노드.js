function solution(n, edge) {
    // 인접 리스트에 node 연결 정보들 저장
    const graph = Array.from({ length: n + 1 }, () => []);

    for (const [node1, node2] of edge) {
        graph[node1].push(node2);
        graph[node2].push(node1);
    }

    // 거리 계산
    const distance = bfs(1, graph);
    const max = Math.max(...distance);

    return distance.filter(v => v === max).length;
}

function bfs(start, graph) {
    const distance = Array(graph.length).fill(-1);
    const queue = [start];

    distance[start] = 0;

    while (queue.length) {
        const current = queue.shift();

        for (const next of graph[current]) {
            // 방문한 적 있으면 패스
            if (distance[next] !== -1) continue;

            distance[next] = distance[current] + 1;
            queue.push(next);
        }
    }

    return distance;
}
