/*
Question:
You are provided with the following table. Based on the student's score,
print the appropriate grade.

Grading Metrics:
0-39: F
40-50: E
51-60: D
61-70: C
71-80: B
81-100: A

If an invalid score is provided outside the allowed range, print
"Invalid Input".
*/

#include <iostream>
using namespace std;

int main() {
    int score;
    cin >> score;

    if (score < 0 || score > 100) {
        cout << "Invalid Input";
    } else if (score <= 39) {
        cout << "F";
    } else if (score <= 50) {
        cout << "E";
    } else if (score <= 60) {
        cout << "D";
    } else if (score <= 70) {
        cout << "C";
    } else if (score <= 80) {
        cout << "B";
    } else {
        cout << "A";
    }

    return 0;
}
