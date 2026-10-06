/*
Question:
The input consists of a single integer N.

Print "Armstrong" if the input number is an Armstrong number,
otherwise print "Not Armstrong".

Example:
Input: 153
Output: Armstrong

153 has 3 digits:
1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
*/

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int original = n;
    int digits = 0;
    int temp = n;

    if (temp == 0) {
        digits = 1;
    } else {
        while (temp != 0) {
            digits++;
            temp /= 10;
        }
    }

    long long sum = 0;
    temp = n;

    while (temp != 0) {
        int digit = temp % 10;
        long long power = 1;

        for (int i = 0; i < digits; i++) {
            power *= digit;
        }

        sum += power;
        temp /= 10;
    }

    if (sum == original) {
        cout << "Armstrong";
    } else {
        cout << "Not Armstrong";
    }

    return 0;
}
