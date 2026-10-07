// Question: Check whether the list is sorted in ascending order.
// Add your solution here.

const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split(/\s+/);

let index = 0;
const n = parseInt(input[index++]);
let arr = [];

for (let i = 0; i < n; i++) {
    arr.push(parseInt(input[index++]));
}

// Check if each element is less than or equal to the next element
let isAscending = true;
for (let i = 0; i < n - 1; i++) {
    if (arr[i] > arr[i + 1]) {
        isAscending = false;
        break; // Stop early if we find any decreasing pair
    }
}

if (isAscending) {
    console.log("Yes");
} else {
    console.log("No");
}
