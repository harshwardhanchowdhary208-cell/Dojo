// Question: Round a number to its nearest integer value.
// Add your solution here.

const fs = require('fs');

function convertTemperature(temp, unit) {
    if (unit === 'C') {
        return ((temp * 9/5) + 32).toFixed(2);
    } else {
        return ((temp - 32) * 5/9).toFixed(2);
    }
}

// Read all inputs from standard input
const input = fs.readFileSync(0, 'utf-8');

// Split the input by lines and remove any leading/trailing whitespace
const lines = input.trim().split('\n');

// Parse temperature as a floating-point number and get the unit
const temp = parseFloat(lines[0].trim());
const unit = lines[1].trim();

// Perform the conversion and print the output
const result = convertTemperature(temp, unit);
console.log(result);
