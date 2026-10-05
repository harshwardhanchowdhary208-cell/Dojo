// Question: What problem does this code solve?
// Add your solution here.

function isPrimeOptimized(num) {
    if (num <= 1) return false;
    if (num <= 3) return true; // 2 and 3 are prime

    // Exclude all even numbers and multiples of 3
    if (num % 2 === 0 || num % 3 === 0) return false;

    // Check odd numbers up to the square root, skipping multiples of 2 and 3
    for (let i = 5; i * i <= num; i += 6) {
        if (num % i === 0 || num % (i + 2) === 0) return false;
    }

    return true;
}
// or
function isPrime(num) {
    // 1. Numbers less than or equal to 1 are not prime
    if (num <= 1) return false;
    
    // 2. Check for factors up to the square root of the number
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) {
            return false; // Found a factor, so it is not prime
        }
    }
    
    return true; // No factors found, so it is prime
}

// Example usage:
console.log(isPrime(11)); // true
console.log(isPrime(4));  // false
console.log(isPrime(1));  // false
