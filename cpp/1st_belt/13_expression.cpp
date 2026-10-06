/*
Question:
You are given four integers a, b, c and d. Your task is to evaluate:

result = a + b * c - d / a

Use the standard mathematical operator precedence, where multiplication
and division are performed before addition and subtraction. Perform
integer arithmetic throughout, so d / a uses integer division.

Input Format:
A single line containing four space-separated integers a, b, c and d.
*/

#include <iostream>
using namespace std;

int main() {
    long long a, b, c, d;
    cin >> a >> b >> c >> d;

    long long result = a + b * c - d / a;

    cout << result;

    return 0;
}
