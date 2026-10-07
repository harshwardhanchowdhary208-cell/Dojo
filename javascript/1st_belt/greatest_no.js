// Question: Find the greatest number among the given inputs.
// Add your solution here.

const fs = require('fs');

// Read input, split by whitespace, and convert each item to a Number
const numbers = fs.readFileSync(0, 'utf-8').trim().split(/\s+/).map(Number);
// the whole input could be also converted to number without using map and putting everything inside Number brackets

// Find the maximum value in the array
const greatest = Math.max(...numbers);

console.log(greatest);
