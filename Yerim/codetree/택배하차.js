const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);

// NxN인 이중 배열
const storage = Array.from({ length: N }, () => Array(N).fill(0));
const result = [];

for (let i = 1; i < M + 1; i++) {
    let [k, h, w, c] = input[i].split(' ').map(Number);

    // 첫 셋팅
    placeBox(k, h, w, c);
    down();
}

removeBoxes();

result.forEach(v => console.log(v));

function placeBox(k, h, w, c) {
    for (let row = 0; row < h; row++) {
        for (let col = c - 1; col < c + w - 1; col++) {
            storage[row][col] = k;
        }
    }
}

function findBoxes() {
    const boxInfo = {};

    for(let row = 0; row < N; row++) {
        for(let col = 0; col < N; col++) {
            let boxNum = storage[row][col];

            if (storage[row][col] === 0) continue;

            // 해당 번호 택배의 정보가 없는 경우
            if(!boxInfo[boxNum]){
                boxInfo[boxNum] = {
                    top: row,
                    bottom: row,
                    left: col,
                    right: col
                }
            } else { // 정보 있는 경우
                boxInfo[boxNum].top = Math.min(boxInfo[boxNum].top, row);
                boxInfo[boxNum].bottom = Math.max(boxInfo[boxNum].bottom, row);
                boxInfo[boxNum].left = Math.min(boxInfo[boxNum].left, col);
                boxInfo[boxNum].right = Math.max(boxInfo[boxNum].right, col);
            }
        }
    }

    return boxInfo;
}

function canDrop(boxes, boxNum) {
    const { bottom, left, right } = boxes[boxNum];

    // 택배의 바닥이 맨 아래면 떨 불가
    if (bottom === N - 1) return false;

    for (let col = left; col <= right; col++) {
        if (storage[bottom + 1][col] !== 0) {
            return false;
        }
    }

    return true;
}

function dropOneStep(boxes, boxNum) {
    const { top, bottom, left, right } = boxes[boxNum];

    for(let col = left; col <= right; col++) {
        storage[top][col] = 0;
        storage[bottom + 1][col] = boxNum;
    }
}

function down() {
    while(true) {
        const boxes = findBoxes();

        let moved = false;

        for(let boxNum in boxes) {
            boxNum = Number(boxNum);

            if(canDrop(boxes, boxNum)) {
                dropOneStep(boxes, boxNum);
                moved = true; 
                break;
            }
        }

        if (!moved) break;
    }

}

function removeBoxes() {
    while(result.length < M) {
        let boxNum = liftLeft();
        if (boxNum !== 0) result.push(boxNum);
        down();

        if (result.length >= M) break;

        boxNum = liftRight();
        if (boxNum !== 0) result.push(boxNum);
        down();
    }
}

function canLiftLeft(boxes, boxNum) {
    const { top, bottom, left } = boxes[boxNum];

    for (let row = top; row <= bottom; row++) {
        for (let col = 0; col < left; col++) {
            if (storage[row][col] !== 0) {
                return false;
            }
        }
    }

    return true;
}

function canLiftRight(boxes, boxNum) {
    const { top, bottom, right } = boxes[boxNum];

    for (let row = top; row <= bottom; row++) {
        for (let col = right + 1; col < N; col++) {
            if (storage[row][col] !== 0) {
                return false;
            }
        }
    }

    return true;
}

function liftLeft () {
    const boxes = findBoxes();
    const candidates = [];

    for (let boxNum in boxes) {
        boxNum = Number(boxNum);

        if(canLiftLeft(boxes, boxNum)) {
            candidates.push(boxNum);
        }
    }

    if (candidates.length === 0) return 0;

    // 후보 중에 숫자가 가장 작은 택배 빼기
    const min = Math.min(...candidates);
    removeBox(min);
    return min;
}

function liftRight () {
    const boxes = findBoxes();
    const candidates = [];

    for (let boxNum in boxes) {
        boxNum = Number(boxNum);

        if(canLiftRight(boxes, boxNum)) {
            candidates.push(boxNum);
        }
    }

    if (candidates.length === 0) return 0;

    const min = Math.min(...candidates);
    removeBox(min);
    return min;
}

function removeBox(target) {
    for (let row = 0; row < N; row++) {
        for (let col = 0; col < N; col++) {
            if (storage[row][col] === target) {
                storage[row][col] = 0;
            }
        }
    }
}
