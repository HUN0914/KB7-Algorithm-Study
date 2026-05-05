function solution(n, w, num) {
    let storage = {};

    for (i = 1; i <= n; i++) {
        const row = Math.ceil(i / w);
        const pos = ((i - 1) % w) + 1;

        const col = row % 2 === 1 ? pos : w - pos + 1;

        if (!storage[col]) storage[col] = [];
        storage[col].push(i);
    }

    const row = Math.ceil(num / w);
    const pos = ((num - 1) % w) + 1;
    const col = row % 2 === 1 ? pos : w - pos + 1;

    return storage[col].length - storage[col].indexOf(num);
}
