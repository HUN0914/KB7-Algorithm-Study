const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const n = Number(input[0]);
const P = input.slice(1).map((line) => line.split(' ').map(Number));

let min = Infinity;
// 각 업무가 아침 업무(true)인지 저녁 업무(false)인지 구분
let isMorning = new Array(n).fill(false);

function dfs(index, count) {
    // 남은 업무를 합쳐도 n/2를 채울 수 없으면 종료
    if (count + (n - index) < n / 2) return;

    if (count === n / 2) {
        let diff = calculateDiff();
        // 이전 최솟값과 비교해서 더 적은 값을 최솟값에 저장
        min = Math.min(min, diff);
        return;
    }

    for (let i = index; i < n; i++) {
        isMorning[i] = true;
        dfs(i + 1, count + 1);
        isMorning[i] = false;
    }
}

function calculateDiff() {
    let morning = 0;
    let evening = 0;

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if (isMorning[i] && isMorning[j]) {
                // 둘 다 아침 업무인 경우
                morning += P[i][j] + P[j][i];
            } else if (!isMorning[i] && !isMorning[j]) {
                // 둘 다 저녁 업무인 경우
                evening += P[i][j] + P[j][i];
            }
        }
    }

    return Math.abs(morning - evening);
}

dfs(0, 0);

console.log(min);
