/*
Question:
You are given a list of integers. Your task is to check whether the list
is in ascending order.

A list is said to be in ascending order if every element is less than or
equal to the next element.

Print "Yes" if the list is in ascending order, otherwise print "No".

Input:
The first line contains an integer N — the number of elements in the list.
The second line contains N space-separated integers.
*/

#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    bool ascending = true;

    for (int i = 1; i < n; i++) {
        if (arr[i] < arr[i - 1]) {
            ascending = false;
            break;
        }
    }

    cout << (ascending ? "Yes" : "No");

    return 0;
}
