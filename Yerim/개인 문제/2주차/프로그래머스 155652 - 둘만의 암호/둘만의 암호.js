function solution(s, skip, index) {
    let result = [];

    for (let i = 0; i < s.length; i++) {
        let cnt = 0;
        let current = s[i];

        while (cnt < index) {
            current = String.fromCharCode(
                ((current.charCodeAt(0) - 97 + 1) % 26) + 97,
            );

            if (!skip.includes(current)) {
                cnt++;
            }
        }

        result.push(current);
    }

    return result.join('');
}
