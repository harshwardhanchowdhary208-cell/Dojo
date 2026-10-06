/*
Question:
Write a program to calculate and print the Greatest Common Divisor (GCD)
of two numbers. Note that if either number is zero, print the other number.

Input Format:
The input consists of two integers A and B.

Output Format:
Print the GCD of the two numbers.
*/

#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;

    a = abs(a);
    b = abs(b);

    while (b != 0) {
        int remainder = a % b;
        a = b;
        b = remainder;
    }

    cout << a;

    return 0;
}
