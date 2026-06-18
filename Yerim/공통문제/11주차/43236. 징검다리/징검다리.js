function solution(distance, rocks, n) {
    
    let left = 1;
    let right = distance;
    let answer = 0;
    
    rocks.sort((a, b) => a - b);
    
    // 이분탐색 시작
    while (left <= right) {
        
        // 기준값 설정 : 
        const mid = Math.floor((left + right) / 2);
        
        let removeCnt = 0;
        let prev = 0; // 이전 바위 번호
        
        for (const rock of rocks) {
            // 결과 값이 가장 작은 거리여야 하기 때문에
            // 더 작은 거리값을 가지는 경우는 삭제
            if (rock - prev < mid) {
                removeCnt++;

                // 바위 제거했을 때는 이전 바위 번호 유지
            } else {
                prev = rock; // 다음 바위 번호로 넘어감
            }
        }
        
        // 맨 마지막 바위와의 거리 확인
        if ((distance - prev) < mid) {
            removeCnt++;
        }
        
        // 삭제한 바위의 개수가 n보다 같거나 작으면
        // 기준값 (mid) 보다 더 큰 값이 필요~~할 수도 있으니까 검사해봄
        if (removeCnt <= n) {
            answer = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return answer;
}