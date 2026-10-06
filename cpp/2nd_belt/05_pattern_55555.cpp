/*
Question:
Write a program to generate and print the given number pattern.

For N = 5:
55555
4444
333
22
1

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

    for (int i = n; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            cout << i;
        }
        cout << '\n';
    }

    return 0;
}
