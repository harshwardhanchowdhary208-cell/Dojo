// Question:
// Read a line of input and print it in this exact format:
// You entered: <input>
// Example: Input: ProgrammingIsFun! -> Output: You entered: ProgrammingIsFun!

const fs = require("fs");
const input = fs.readFileSync(0, "utf8").trim();
console.log(`You entered: ${input}`);
