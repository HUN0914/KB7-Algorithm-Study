function solution(n, weak, dist) {
    let min = Infinity;

    // 원형을 일자로 바꿔서 각 시작점마다 확인
    let newWeak = [...weak];

    for (let i = 0; i < weak.length; i++) {
        newWeak.push(weak[i] + n);
    }

    // 투입 순서 모두 구하기
    const permutations = getPermutations(dist);

    // 시작 취약점 바꿔가면서 최소값 찾기~~~~
    for (let start = 0; start < weak.length; start++) {
        for (const friends of permutations) {

            const count = simulate(start, friends, newWeak, weak.length);

            if (count !== -1) {
                min = Math.min(min, count);
            }
        }
    }

    // 취약 지점을 전부 점검할 수 없는 경우에는 -1을 return 
    return min === Infinity ? -1 : min;
}

function getPermutations(dist) {
    const result = [];
    const visited = new Array(dist.length).fill(false); // 이미 사용한 번호인지 확인용

    // 지금까지 선택한 값들의 순서
    function dfs(path) {
        // 다 골랐다!!
        if (path.length === dist.length) {
            // 만든 순열 저장하고 끝내기
            result.push([...path]);
            return;
        }

        for (let i = 0; i < dist.length; i++) {
            // 이미 사용했으면 패스
            if (visited[i]) continue;

            // 사용 표시
            visited[i] = true;
            // 현재 순서에 추가
            path.push(dist[i]);

            // 다음 자리 채우러 이동
            dfs(path);

            // 방금 넣은 값 제거하고 사용 안함 상태로 변경
            path.pop();
            visited[i] = false;
        }
    }

    dfs([]); // 빈 상태로 시작
    return result;
}

function simulate(start, friends, newWeak, weakLength) {
  let friendIndex = 0;

    // 첫 번째 친구가 커버할 수 있는 끝 위치
    let coverage = newWeak[start] + friends[friendIndex];

    // start부터 weakLength개만 확인
    for (let i = start; i < start + weakLength; i++) {
        // 현재 친구가 이 취약점을 커버 못하면 새 친구 투입
        if (newWeak[i] > coverage) {
            friendIndex++;

            // 더 투입할 친구 없으면 실패
            if (friendIndex >= friends.length) return -1;

            // 새 친구는 현재 취약점에서 출발 (이전 친구가 현재 취약점을 커버하지 못했으니까)
            coverage = newWeak[i] + friends[friendIndex];
        }
    }

    // index가 0으로 시작하니까 개수는 +1
    return friendIndex + 1;
}