/*
Question:
Write a program to generate and print the given number pattern.

For N = 5:
1
12
123
1234
12345

Input Format:
The input consists of a single integer N.

Output Format:
Print the number pattern as described.
*/

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << j;
        }
        cout << '\n';
    }

    return 0;
}
