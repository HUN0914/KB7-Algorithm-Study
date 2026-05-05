function solution(message, spoiler_ranges) {
    const n = message.length;

    const revealStep = new Array(n).fill(0);

    for (let step = 0; step < spoiler_ranges.length; step++) {
        const [start, end] = spoiler_ranges[step];

        for (let pos = start; pos <= end; pos++) {
            revealStep[pos] = step + 1;
        }
    }

    const visibleWords = new Set();
    const wordsByStep = Array.from(
        { length: spoiler_ranges.length + 1 },
        () => [],
    );

    let i = 0;

    while (i < n) {
        if (message[i] === ' ') {
            i++;
            continue;
        }

        const start = i;

        while (i < n && message[i] !== ' ') {
            i++;
        }

        const end = i - 1;
        const word = message.slice(start, i);

        let maxStep = 0;

        for (let j = start; j <= end; j++) {
            maxStep = Math.max(maxStep, revealStep[j]);
        }

        if (maxStep === 0) {
            visibleWords.add(word);
        } else {
            wordsByStep[maxStep].push(word);
        }
    }

    let answer = 0;
    const revealedWords = new Set();

    for (let step = 1; step < wordsByStep.length; step++) {
        for (const word of wordsByStep[step]) {
            if (!visibleWords.has(word) && !revealedWords.has(word)) {
                answer++;
            }

            revealedWords.add(word);
        }
    }

    return answer;
}
