// Question:
// Ask for a number, store it in a variable, and print it back.
// Required output format: You entered: <number>
// Example: Input: 252525 -> Output: You entered: 252525

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim();
console.log(`You entered: ${input}`);
