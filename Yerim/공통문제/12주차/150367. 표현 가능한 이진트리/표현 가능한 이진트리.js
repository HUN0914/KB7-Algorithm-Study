function solution(numbers) {
    const answer = [];
    
    // 문자열 이진수로 변환하기
    // 길이를 2^h-1로 맞춤
    // 가운데 값을 루트로 해서 재귀적으로 트리를 구성
    // 서브트리 중에 부모 = 0, 자식 = 1인 경우가 나오면 실패
    
    for (const num of numbers) {
        // 이진수로 변환
        let binary = num.toString(2);
        
        // 길이 찾기
        let size = 1;
        
        while (size < binary.length) {
            size = size * 2 + 1;
        }
        
        // 길이에 맞춰 앞에 0 붙이기
        binary = binary.padStart(size, "0");
        
        answer.push(check(binary) ? 1 : 0);
    }
    
    return answer;
}

function check(tree) {
    // 가운데 값을 루트로 설정
    const root = Math.floor(tree.length / 2);
    
    if (tree.length === 1) return true;
    
    const left = tree.slice(0, root);
    const right = tree.slice(root + 1);
    
    // 서브트리 중에 부모 = 0, 자식 = 1인 경우가 나오면 실패
    if (
        tree[root] === "0" &&
        (left.includes("1") || right.includes("1"))
    ) {
        return false;
    }
    
    return check(left) && check(right)
}