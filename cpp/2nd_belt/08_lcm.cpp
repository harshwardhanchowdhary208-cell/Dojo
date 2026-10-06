/*
Question:
Write a program to calculate and print the Least Common Multiple (LCM)
of two numbers. If either number is zero, the LCM of the two numbers is
also zero.

Input Format:
The input consists of two integers A and B.

Output Format:
The output consists of the LCM of the two numbers.

Example:
Input: 4 6
Output: 12
*/

#include <iostream>
#include <cstdlib>
using namespace std;

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    long long a, b;
    cin >> a >> b;

    if (a == 0 || b == 0) {
        cout << 0;
    } else {
        cout << llabs((a / gcd(llabs(a), llabs(b))) * b);
    }

    return 0;
}
