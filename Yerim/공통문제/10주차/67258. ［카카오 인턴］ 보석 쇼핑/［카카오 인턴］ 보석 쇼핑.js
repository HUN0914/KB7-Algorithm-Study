function solution(gems) {
    // 구해야 하는 보석 개수
    const totalTypes = new Set(gems).size;
    
    // 현재 구간에 있는 보석 종류와 개수 저장
    const gemMap = new Map();
    
    let left = 0;
    
    // 정답 구간, 처음에는 전체
    let answer = [0, gems.length - 1];
    
    for (let right = 0; right < gems.length; right++) {
        const gem = gems[right];
        
        // 현재 구간에 보석 추가
        gemMap.set(gem, (gemMap.get(gem) || 0) + 1);
        
        // 현재 구간에 모든 종류의 보석이 들어있을 때
        while (gemMap.size === totalTypes) {
            // 현재 구간 길이랑 기존 길이 구간 비교
            // 현재 구간 길이가 더 짧으면 변경
            if (right - left < answer[1] - answer[0]) {
                answer = [left, right];
            }
            
            // 맨 앞 보석 제거
            const leftGem = gems[left];
            
            // 해당 보석 개수 감소
            gemMap.set(leftGem, gemMap.get(leftGem) - 1);
            
            // 보석 개수가 0개면 삭제
            if (gemMap.get(leftGem) === 0) {
                gemMap.delete(leftGem);
            }
            
            left++;
        }
    }
    
    return [answer[0] + 1, answer[1] + 1];
}