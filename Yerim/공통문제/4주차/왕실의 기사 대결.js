const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').trim().split('\n');

const [L, N, Q] = input[0].split(' ').map(Number);

const chessboard = Array.from({ length: L }, () => Array(L).fill(0)); // 벽, 함정 저장
const knightboard = Array.from({ length: L }, () => Array(L).fill(0)); // 기사 저장
const knightInfo = {};
const dr = [-1, 0, 1, 0]; // 위 오른쪽 아래 왼쪽
const dc = [0, 1, 0, -1];

// 체스판 정보 저장
for (let i = 1; i <= L; i++) {
    const row = input[i].split(' ').map(Number);

    for (let j = 0; j < L; j++) {
        chessboard[i - 1][j] = row[j];
    }
}

// 기사 체스판에 올리기
for (let i = L + 1; i <= L + N; i++) {
    const [r, c, h, w, k] = input[i].split(' ').map(Number);

    for (let row = r - 1; row <= r + h - 2; row++) {
        for (let col = c - 1; col <= c + w - 2; col++) {
            knightboard[row][col] = i - L;
        }
    }

    knightInfo[i - L] = {
        top: r - 1,
        bottom: r + h - 2,
        left: c - 1,
        right: c + w - 2,
        stamina: k,
        damage: 0,
    };
}

for (let i = L + N + 1; i <= L + N + Q; i++) {
    const [knight, d] = input[i].split(' ').map(Number);

    // 명령 들어온 기사 체력 확인
    if (knightInfo[knight].stamina <= 0) continue;

    // 이동한 기사들 저장
    const pushed = new Set();

    // 해당 방향으로 이동 못하면 패스
    if (!checkMove(knight, d, pushed)) continue;

    // 이동
    move(pushed, d);

    // 명령받은 기사 제외하고 대미지 적용
    damage(pushed, knight);

    // 체력 0이면 체스판에서 제거
    updateKnightBoard();
}

// 체스판에 남아있는 기사들이 입은 대미지 계산
const result = sumDamage();
console.log(result);

// 해당 방향으로 이동할 수 있는지 확인 boolean
function checkMove(knight, d, pushed) {
    pushed.add(knight);

    const { top, bottom, left, right } = knightInfo[knight];

    const nextTop = top + dr[d];
    const nextBottom = bottom + dr[d];
    const nextLeft = left + dc[d];
    const nextRight = right + dc[d];

    for (let row = nextTop; row <= nextBottom; row++) {
        for (let col = nextLeft; col <= nextRight; col++) {
            // 체스판 밖이면 이동 X
            if (row < 0 || row >= L || col < 0 || col >= L) {
                return false;
            }

            // 벽이면 이동 X
            if (chessboard[row][col] === 2) return false;

            // 다른 기사가 있으면 그 기사도 밀 수 있는지 확인
            const nextKnight = knightboard[row][col];

            // 0 아니어야 됨, 지금이랑 다른 기사여야 되고 밀린 적 없어야 됨
            if (
                nextKnight !== 0 &&
                nextKnight !== knight &&
                !pushed.has(nextKnight)
            ) {
                if (!checkMove(nextKnight, d, pushed)) return false;
            }
        }
    }

    return true;
}

// 기사 위치 정보를 업데이트
function move(pushed, d) {
    for (const knight of pushed) {
        const info = knightInfo[knight];

        info.top += dr[d];
        info.bottom += dr[d];
        info.left += dc[d];
        info.right += dc[d];
    }
}

function damage(pushed, knight) {
    for (const pushedKnight of pushed) {
        if (pushedKnight === knight) continue;

        const { top, bottom, left, right } = knightInfo[pushedKnight];

        for (let row = top; row <= bottom; row++) {
            for (let col = left; col <= right; col++) {
                if (chessboard[row][col] === 1) {
                    knightInfo[pushedKnight].damage++;
                    knightInfo[pushedKnight].stamina--;
                }
            }
        }
    }
}

function updateKnightBoard() {
    // knightboard 초기화
    for (let row = 0; row < L; row++) {
        knightboard[row].fill(0);
    }

    for (let knight = 1; knight <= N; knight++) {
        const info = knightInfo[knight];

        // 체력 없는 애들은 패스
        if (info.stamina <= 0) continue;

        const { top, bottom, left, right } = info;

        // 정보를 바탕으로 다시 기사 올리기
        for (let row = top; row <= bottom; row++) {
            for (let col = left; col <= right; col++) {
                knightboard[row][col] = knight;
            }
        }
    }
}

function sumDamage() {
    let sum = 0;

    for (let knight = 1; knight <= N; knight++) {
        const info = knightInfo[knight];

        if (info.stamina <= 0) continue;

        sum += info.damage;
    }

    return sum;
}
