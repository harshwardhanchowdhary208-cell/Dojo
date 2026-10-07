// Question:
// Read two integers, num1 and num2, separated by a space.
// Print their addition, subtraction, multiplication, and integer division,
// each on a separate line, in that order.
// Example input: 5 3
// Output:
// 8
// 2
// 15
// 1

process.stdin.on("data", function (data) {
    const numbers = data.toString().trim().split(/\s+/).map(Number);
    const num1 = numbers[0];
    const num2 = numbers[1];

    console.log(num1 + num2);
    console.log(num1 - num2);
    console.log(num1 * num2);
    console.log(Math.trunc(num1 / num2));
});
