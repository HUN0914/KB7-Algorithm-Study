function solution(signals) {
    
    let cycles = signals.map(s => s[0] + s[1] + s[2]);
    
    let totalLCM = cycles[0];
    
    for (let i = 1; i < cycles.length; i++) {
        totalLCM = lcm(totalLCM, cycles[i]);
    }
    
    for(let t = 1; t <= totalLCM; t++) {
        let isYellow = true;
        for(let i = 0; i < signals.length; i++) {
            const signal = signals[i];
            const cycle = cycles[i];
            
            const position = (t - 1) % cycle + 1;
            if(!(signal[0] < position  && position <= signal[0] + signal[1])) {
                isYellow = false;
                break;
            }
        }
        
        if (isYellow) return t;
    }
    return -1;
}

function gcd(a, b) {
    while(b !== 0) {
        [a, b] = [b, a % b];
    }
    
    return a
}

function lcm(a, b) {
    return (a * b) / gcd(a, b);
}