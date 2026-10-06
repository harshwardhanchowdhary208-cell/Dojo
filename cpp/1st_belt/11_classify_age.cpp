/*
Question:
Write a program that takes the age of a person as input and classifies
them into one of the following age groups:

0-12: "Child"
13-19: "Teenager"
20-64: "Adult"
65 and above: "Senior"

Input Format:
A single integer representing the age of the person.

Output Format:
A single line containing the age group classification as a string:
"Child", "Teenager", "Adult", or "Senior".
*/

#include <iostream>
#include <string>
using namespace std;

string classifyAge(int age) {
    if (age >= 0 && age <= 12) {
        return "Child";
    } else if (age <= 19) {
        return "Teenager";
    } else if (age <= 64) {
        return "Adult";
    } else {
        return "Senior";
    }
}

int main() {
    int age;
    cin >> age;

    cout << classifyAge(age);

    return 0;
}
