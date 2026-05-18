function solution(numbers) {
    const permutations = getPermutations(numbers);
    
    const nums = getNumber(permutations);
    
    console.log(nums);
    
    return getPrimeCount(nums);
}

function getPermutations(numbers) {
    const visited = Array(numbers.length).fill(false);
    const result = [];
    
    function dfs(path) {
        if (path.length > 0) result.push([...path]);
        
        if (path.length === numbers.length) return;
        
        for (let i = 0; i < numbers.length; i++) {
            if (visited[i]) continue;
            
            path.push(numbers[i]);
            visited[i] = true;
            
            dfs(path);
            
            path.pop();
            visited[i] = false;
        }
    }
    
    dfs([]);
    
    return result;
}

function getNumber(permutations) {
    const set = new Set();
    
    for (const numStr of permutations) {
        let str = '';
        for (const ch of numStr) {
            str += ch
        }
        
        set.add(Number(str));
    }
    
    return [...set];
}

function getPrimeCount(nums) {
    let count = 0;
    
    for (const num of nums) {
        if (isPrime(num)) count++;
        
//         if (n < 2) continue;
    
//         let isPrime = true;
        
//         // n의 루트값까지 돌면서 확인
//         for (let i = 2; i <= Math.sqrt(n); i++) {
//             // 이 숫자들로 나누어 떨어지면 소수 아님
//             if (n % i === 0) {
//                 isPrime = false;
//                 break;
//             }
//         }
        
//         if (isPrime) count++;
    }
    
    return count;
}

function isPrime(n) {
    if (n < 2) return false
    
    // n의 루트값까지 돌면서 확인
    for (let i = 2; i <= Math.sqrt(n); i++) {
        // 이 숫자들로 나누어 떨어지면 소수 아님
        if (n % i === 0) return false;
    }
    
    return true;
}