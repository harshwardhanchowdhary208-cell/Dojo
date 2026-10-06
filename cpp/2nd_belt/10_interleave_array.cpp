/*
Question:
Given the array nums consisting of 2N elements in the form
[x1, x2, ..., xn, y1, y2, ..., yn], return the array in the form
[x1, y1, x2, y2, ..., xn, yn].

Input Format:
The first line of input contains the size of an array 2N.
The second line has the elements of the array.
The third line has the value of N.

Output Format:
The output consists of the array in the form
[x1, y1, x2, y2, ..., xn, yn].
*/

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int size;
    cin >> size;

    vector<int> nums(size);
    for (int i = 0; i < size; i++) {
        cin >> nums[i];
    }

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cout << nums[i] << " " << nums[i + n];
        if (i != n - 1) {
            cout << " ";
        }
    }

    return 0;
}
