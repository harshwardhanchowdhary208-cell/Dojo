/*
Question:
Given a list of N integers, find the largest number in the list.
Print the largest element.

Input:
The first line contains an integer N representing the number of elements.
The second line contains N space-separated integers.

Output:
Print the largest number in the list.
*/

#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int x;
    cin >> x;
    int largest = x;

    for (int i = 1; i < n; i++) {
        cin >> x;
        if (x > largest) {
            largest = x;
        }
    }

    cout << largest;

    return 0;
}
