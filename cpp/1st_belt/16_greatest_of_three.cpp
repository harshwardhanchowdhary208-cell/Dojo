/*
Question:
Write a program to determine the greatest of three given numbers:
num1, num2 and num3.

Example:
Input: 7 12 5
Output: 12

Explanation:
12 is greater than 7 and 5.
*/

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int num1, num2, num3;
    cin >> num1 >> num2 >> num3;

    cout << max(num1, max(num2, num3));

    return 0;
}
