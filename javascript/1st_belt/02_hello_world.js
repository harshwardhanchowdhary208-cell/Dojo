// Question:
// Write instructions so the computer greets us with "Hello World!".
// Example input: Hello World! -> Output: Hello World!

process.stdin.on("data", function (data) {
    const input = data.toString().trim();
    console.log(input);
});
