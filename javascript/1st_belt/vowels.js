// Question: What problem does this code solve?
// Add your solution here.

const fs = require('fs');
const a = fs.readFileSync(0, 'utf-8').trim();

// Define a string containing all lowercase and uppercase vowels
const vowels = 'aeiouAEIOU';

// Get the first and last characters of the input string
const firstChar = a[0];
const lastChar = a[a.length - 1];

// Check if both characters are vowels
if (vowels.includes(firstChar) && vowels.includes(lastChar)) {
    console.log('Vowel');
} else {
    console.log('Not Vowel');
}
