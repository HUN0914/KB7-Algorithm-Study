function solution(n, cores) {
    
    // 코어 수보다 작업 개수가 더 작으면 n번째 코어가 정답
    if (n <= cores.length) {
        return n;
    }
    
    // 작업 시간 t를 이분 탐색으로 구하기
    let left = 1;
    let right = Math.max(...cores) * n;
    let t = 0;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        
        const work = processed(mid);
        
        // 작업을 다 끝낼 수 있는 시간이면 더 적은 시간에도 가능한지 확인
        if (work >= n) {
            t = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    // mid 초에서 처리되는 작업의 수
    function processed(mid) {
        let sum = 0;
        
        for (const core of cores) {
            const w = Math.floor(mid / core) + 1;
            sum += w;
        }
        
        return sum;
    }
    
    // t-1초까지 작업하고 남은 작업의 수
    let remain = n - processed(t - 1);
    
    for (let i = 0; i < cores.length; i++) {
        // t초에 작업 끝내는 코어 만나면
        if (t % cores[i] === 0) {
            remain--;
        }
        
        // remain만큼 다 만남 -> 코어 번호 반환
        if (remain === 0) {
            return i + 1;
        }
    }
}