function test(innitialState, queue) {
    let finalState = innitialState;

    for (let state of queue) {
        if (typeof state === 'function') {
            finalState = state(finalState);
        } else {
            finalState = state;
        }
    }
    
    return finalState;
}

console.log(test(0, [1,1,1]));
console.log(test(0, [n => n + 1, n => n + 1, n => n + 1]));
console.log(test(0, [1, n => n + 1]));
console.log(test(0, [1, n => n + 100, 1]));
