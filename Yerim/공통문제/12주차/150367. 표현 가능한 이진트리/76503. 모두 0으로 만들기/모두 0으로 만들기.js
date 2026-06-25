function solution(a, edges) {
    // BigInt 사용
    // 다 더했을 때 0 안 되면 -1 리턴
    const sum = a.reduce((acc, cur) => acc + BigInt(cur), 0n);

    if (sum !== 0n) return -1;

    const graph = Array.from({ length: a.length }, () => []);

    for (const [e1, e2] of edges) {
        graph[e1].push(e2);
        graph[e2].push(e1);
    }

    let count = 0n;

    const stack = [[0, -1]];
    const order = [];

    // 0을 root로 잡고 순서 정하기
    // 가장 끝에 있는 leaf 노드부터 계산
    while (stack.length) {
        const [cur, parent] = stack.pop();

        // 순서 추가
        order.push([cur, parent]);

        for (const next of graph[cur]) {
            // 부모 아니면 자식
            if (next === parent) continue;

            stack.push([next, cur]);
        }
    }

    // 뒤에서부터 계산 시작 (맨앞이 root 뒤에가 leaf)
    // 자식부터 0으로 만들면서 위로 올라감
    for (let i = order.length - 1; i >= 0; i--) {
        const [child, parent] = order[i];

        // 자식이 root일 때 -> parent 없음!!
        if (parent === -1) continue;

        // 자식을 0 만드는 걸 기준으로 계산
        a[parent] += a[child];
        count += BigInt(Math.abs(a[child]));
        a[child] = 0;
    }

    return count;
}
