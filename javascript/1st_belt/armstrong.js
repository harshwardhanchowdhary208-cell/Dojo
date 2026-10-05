// Question: What problem does this code solve?
// Add your solution here.

const fs = require('fs');

function main() {
    // Read standard input and trim any whitespace
    const input = fs.readFileSync(0, 'utf-8').trim();
    if (!input) return;

    // Get the number as a string to count its digits
    const numStr = input.split(/\s+/)[0];
    const n = numStr.length;
    const targetNumber = parseInt(numStr, 10);

    // Calculate the sum of digits raised to the power of n
    let sum = 0;
    for (let i = 0; i < n; i++) {
        sum += Math.pow(parseInt(numStr[i], 10), n);
    }

    // Check if the sum equals the original number
    if (sum === targetNumber) {
        console.log("Armstrong");
    } else {
        console.log("Not Armstrong");
    }
}

main();
