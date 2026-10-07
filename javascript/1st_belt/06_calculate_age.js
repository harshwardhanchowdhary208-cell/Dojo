// Question:
// Write calculateAge(present_year, year_of_birth).
// Calculate the age by subtracting year_of_birth from present_year,
// then print: You are <age> years old!
// Input is two lines: present year, then year of birth.
// Example: 2024 and 2003 -> You are 21 years old!

function calculateAge(present_year, year_of_birth) {
    const age = present_year - year_of_birth;
    console.log(`You are ${age} years old!`);
}

const fs = require("fs");
const lines = fs.readFileSync(0, "utf8").trim().split(/\s+/);
const present_year = parseInt(lines[0], 10);
const year_of_birth = parseInt(lines[1], 10);

calculateAge(present_year, year_of_birth);
